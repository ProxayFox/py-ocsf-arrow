from __future__ import annotations

import json
import re
from argparse import ArgumentParser
from pathlib import Path

import pyarrow as pa

from ocsf.api.client import OcsfApiClient
from py_ocsf_arrow import SchemaGenerator
from py_ocsf_arrow.base import CACHE_DIR

# ---------------------------------------------------------------------------
# Scalar Arrow type renderer
# ---------------------------------------------------------------------------

_SCALAR_RENDERERS: list[tuple] = [
    (lambda t: t == pa.bool8(), "pa.bool8()"),
    (pa.types.is_boolean, "pa.bool_()"),
    (pa.types.is_int8, "pa.int8()"),
    (pa.types.is_int16, "pa.int16()"),
    (pa.types.is_int32, "pa.int32()"),
    (pa.types.is_int64, "pa.int64()"),
    (pa.types.is_uint8, "pa.uint8()"),
    (pa.types.is_uint16, "pa.uint16()"),
    (pa.types.is_uint32, "pa.uint32()"),
    (pa.types.is_uint64, "pa.uint64()"),
    (pa.types.is_float16, "pa.float16()"),
    (pa.types.is_float32, "pa.float32()"),
    (pa.types.is_float64, "pa.float64()"),
    (pa.types.is_string, "pa.string()"),
    (pa.types.is_large_string, "pa.large_string()"),
    (pa.types.is_binary, "pa.binary()"),
    (pa.types.is_large_binary, "pa.large_binary()"),
]


def _render_scalar_arrow_type(arrow_type: pa.DataType) -> str:
    for predicate, expr in _SCALAR_RENDERERS:
        if predicate(arrow_type):
            return expr
    raise ValueError(f"Cannot render scalar Arrow type: {arrow_type}")


# ---------------------------------------------------------------------------
# OCSF-attribute-aware type expression renderer
#
# Works on raw OCSF attribute metadata rather than resolved Arrow types so
# that object names are never lost.  Object references become imports and
# `pa.struct(list(NAME_SCHEMA))` expressions rather than inlined structs.
# ---------------------------------------------------------------------------


def _is_extension_object(ocsf_type: str) -> bool:
    """Return True for objects that belong to an OCSF extension (name contains '/')."""
    return "/" in ocsf_type


def _render_attr_type_expr(
    ocsf_type: str,
    is_array: bool,
    type_map: dict[str, pa.DataType],
    schema_objects: dict,
    direct_deps: set[str],
    allowed_object_deps: set[str] | None = None,
) -> str:
    """Return a Python expression for the Arrow type of one OCSF attribute.

    If the type is a known OCSF object and is present in *allowed_object_deps*
    (or *allowed_object_deps* is None), it is added to *direct_deps* and
    rendered as a struct reference.  Disallowed, extension, or unknown types
    fall back to ``pa.string()``.
    """
    if ocsf_type in type_map:
        base_expr = _render_scalar_arrow_type(type_map[ocsf_type])
    elif (
        ocsf_type in schema_objects
        and not _is_extension_object(ocsf_type)
        and (allowed_object_deps is None or ocsf_type in allowed_object_deps)
    ):
        direct_deps.add(ocsf_type)
        base_expr = f"pa.struct(list({ocsf_type.upper()}_SCHEMA))"
    else:
        base_expr = "pa.string()"

    return f"pa.list_({base_expr})" if is_array else base_expr


# ---------------------------------------------------------------------------
# Dependency discovery
# ---------------------------------------------------------------------------


def _discover_all_objects(
    start_names: set[str],
    schema_objects: dict,
    type_map: dict[str, pa.DataType],
    ignored_attrs: set[str],
) -> dict[str, set[str]]:
    """DFS from *start_names* returning {object_name: set_of_direct_object_deps}.

    Back-edges (cycles) are silently dropped so each object file stays
    import-cycle free; the affected field falls back to ``pa.string()``.
    """
    dep_graph: dict[str, set[str]] = {}

    def _dfs(name: str, ancestors: frozenset[str]) -> None:
        if name in dep_graph or name not in schema_objects:
            return

        # Include self in ancestors before scanning attributes so that both
        # self-references (e.g. analytic.related_analytics: analytic) and
        # true back-edges through longer cycles are excluded from direct deps.
        self_and_ancestors = ancestors | {name}

        direct: set[str] = set()
        for attr_name, attr in schema_objects[name].attributes.items():
            if attr_name in ignored_attrs:
                continue
            t = attr.type
            if (
                t not in type_map
                and t in schema_objects
                and not _is_extension_object(t)
                and t not in self_and_ancestors  # breaks self-loops and back-edges
            ):
                direct.add(t)

        dep_graph[name] = direct
        for dep in direct:
            _dfs(dep, self_and_ancestors)

    for name in start_names:
        _dfs(name, frozenset())

    return dep_graph


# ---------------------------------------------------------------------------
# File renderers
# ---------------------------------------------------------------------------


def _render_fields_block(
    attributes: dict,
    type_map: dict[str, pa.DataType],
    schema_objects: dict,
    ignored_attrs: set[str],
    direct_deps: set[str],
    allowed_object_deps: set[str] | None = None,
) -> str:
    lines = []
    for attr_name, attr in sorted(attributes.items()):
        if attr_name in ignored_attrs:
            continue
        is_array = bool(getattr(attr, "is_array", False))
        type_expr = _render_attr_type_expr(
            attr.type,
            is_array,
            type_map,
            schema_objects,
            direct_deps,
            allowed_object_deps,
        )
        nullable = attr.requirement != "required"
        field_line = (
            f"pa.field({json.dumps(attr_name)}, {type_expr}, nullable={nullable}),"
        )
        # Ruff wants 12-space indent (3 levels: function body → list → item).
        # Wrap long lines across multiple arguments.
        if len(field_line) + 12 <= 88:
            lines.append(f"            {field_line}")
        else:
            lines.append(
                f"            pa.field(\n"
                f"                {json.dumps(attr_name)},\n"
                f"                {type_expr},\n"
                f"                nullable={nullable},\n"
                f"            ),"
            )
    return "\n".join(lines)


def _imports_block(direct_deps: set[str], objects_path_expr: str) -> str:
    """Return the import preamble for a generated schema file.

    Because version directories contain dots (e.g. ``1.8.0``), normal dotted
    imports are impossible.  Instead, dependency schemas are loaded at module
    level via ``importlib.util.spec_from_file_location`` using a file-system
    path relative to ``__file__``.

    *objects_path_expr* is a Python expression that evaluates to the ``Path``
    of the objects directory — for object files this is
    ``Path(__file__).parent``, for class files it navigates up to the version
    root and into ``objects/``.
    """
    lines = ["import pyarrow as pa"]
    if not direct_deps:
        return "\n".join(lines)

    lines = [
        "import importlib.util",
        "from pathlib import Path",
        "",
        "import pyarrow as pa",
        "",
        f"_OBJECTS_DIR = {objects_path_expr}",
        "",
        "",
        "def _load_dep(name: str):",
        '    spec = importlib.util.spec_from_file_location(name, _OBJECTS_DIR / f"{name}.py")',
        "    assert spec is not None and spec.loader is not None",
        "    mod = importlib.util.module_from_spec(spec)",
        "    spec.loader.exec_module(mod)",
        "    return mod",
        "",
        "",
    ]

    for dep in sorted(direct_deps):
        line = f'{dep.upper()}_SCHEMA = _load_dep("{dep}").{dep.upper()}_SCHEMA'
        if len(line) > 88:
            line = (
                f"{dep.upper()}_SCHEMA = _load_dep(\n"
                f'    "{dep}"\n'
                f").{dep.upper()}_SCHEMA"
            )
        lines.append(line)

    return "\n".join(lines)


def _render_object_file(
    object_name: str,
    generator: SchemaGenerator,
    version: str,
    allowed_deps: set[str],
    ignored_attrs: set[str] | None = None,
) -> str:
    ocsf_obj = generator.schema.objects[object_name]
    type_map = generator._type_mapper.OCSF_TO_ARROW
    ignored = ignored_attrs if ignored_attrs is not None else generator._ignored_attr
    direct_deps: set[str] = set()

    fields_block = _render_fields_block(
        ocsf_obj.attributes,
        type_map,
        generator.schema.objects,
        ignored,
        direct_deps,
        allowed_object_deps=allowed_deps,
    )

    fn_name = f"get_{object_name}_schema"
    const_name = f"{object_name.upper()}_SCHEMA"

    # Object files import siblings from the same directory.
    objects_path_expr = "Path(__file__).parent"

    if fields_block.strip():
        schema_body = (
            f"    return pa.schema(\n        [\n{fields_block}\n        ]\n    )\n"
        )
    else:
        schema_body = "    return pa.schema([])\n"

    const_line = f"{const_name} = {fn_name}()\n"
    if len(const_line.rstrip()) > 88:
        const_line = f"{const_name} = (\n    {fn_name}()\n)\n"

    return (
        f'"""Auto-generated Arrow schema for OCSF object \'{object_name}\'.\n\n'
        f"OCSF version {version}.\n"
        '"""\n\n'
        f"{_imports_block(direct_deps, objects_path_expr)}\n\n\n"
        f"def {fn_name}() -> pa.Schema:\n"
        f'    """Return the Arrow schema for OCSF object \'{object_name}\'."""\n'
        f"{schema_body}\n\n"
        f"{const_line}"
    )


def _render_class_file(
    class_name: str,
    generator: SchemaGenerator,
    version: str,
    ignored_attrs: set[str] | None = None,
) -> str:
    event_class = generator.schema.classes[class_name]
    type_map = generator._type_mapper.OCSF_TO_ARROW
    ignored = ignored_attrs if ignored_attrs is not None else generator._ignored_attr
    direct_deps: set[str] = set()

    fields_block = _render_fields_block(
        event_class.attributes,
        type_map,
        generator.schema.objects,
        ignored,
        direct_deps,
        allowed_object_deps=None,  # no restriction at the class level
    )

    fn_name = f"get_{class_name}_schema"
    const_name = f"{class_name.upper()}_SCHEMA"

    # Class files live at categories/<cat>/<uid>_<name>.py — objects dir is
    # two levels up at the version root.
    objects_path_expr = 'Path(__file__).resolve().parents[2] / "objects"'

    if fields_block.strip():
        schema_body = (
            f"    return pa.schema(\n        [\n{fields_block}\n        ]\n    )\n"
        )
    else:
        schema_body = "    return pa.schema([])\n"

    const_line = f"{const_name} = {fn_name}()\n"
    if len(const_line.rstrip()) > 88:
        const_line = f"{const_name} = (\n    {fn_name}()\n)\n"

    return (
        f'"""Auto-generated Arrow schema for OCSF class \'{class_name}\'.\n\n'
        f"OCSF version {version}.\n"
        '"""\n\n'
        f"{_imports_block(direct_deps, objects_path_expr)}\n\n\n"
        f"def {fn_name}() -> pa.Schema:\n"
        f'    """Return the Arrow schema for OCSF class \'{class_name}\'."""\n'
        f"{schema_body}\n\n"
        f"{const_line}"
    )


# ---------------------------------------------------------------------------
# Category layout helpers
# ---------------------------------------------------------------------------


def _sanitize_dir_name(name: str) -> str:
    """Lowercase *name* and replace non-alphanumeric runs with underscores."""
    return re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")


def _dir_to_package(directory: Path, src_root: Path = Path("src")) -> str:
    """Convert a file-system path to a dotted Python package name."""
    try:
        rel = directory.relative_to(src_root)
    except ValueError:
        rel = directory
    return ".".join(rel.parts)


def _render_category_init(
    class_entries: list[tuple[int, str]],
    package_name: str,
) -> str:
    """Return Python source for a category ``__init__.py`` that lazy-loads class files."""
    lines: list[str] = [
        '"""Auto-generated OCSF category schema exports.',
        "",
        "Class files have numeric-prefixed names which Python cannot import with",
        "a normal ``import`` statement.  They are loaded via ``importlib`` and",
        "exposed as a stable API from this package.",
        '"""',
        "",
        "from __future__ import annotations",
        "",
        "from functools import lru_cache",
        "from importlib.util import module_from_spec, spec_from_file_location",
        "from pathlib import Path",
        "from types import ModuleType",
    ]

    all_names: list[str] = []

    for full_uid, class_name in sorted(class_entries):
        filename = f"{full_uid}_{class_name}.py"
        loader = f"_load_{class_name}_module"
        getter = f"get_{class_name}_schema"
        const = f"{class_name.upper()}_SCHEMA"
        internal = f"{package_name}._{full_uid}_{class_name}"

        # Detect lines that would exceed 88 chars and wrap them.
        module_path_line = f'    module_path = Path(__file__).with_name("{filename}")'
        if len(module_path_line) > 88:
            module_path_lines = [
                "    module_path = Path(__file__).with_name(",
                f'        "{filename}"',
                "    )",
            ]
        else:
            module_path_lines = [module_path_line]

        const_line = f"{const} = {getter}()"
        if len(const_line) > 88:
            const_lines = [
                f"{const} = (",
                f"    {getter}()",
                ")",
            ]
        else:
            const_lines = [const_line]

        lines.extend(
            [
                "",
                "",
                "@lru_cache(maxsize=1)",
                f"def {loader}() -> ModuleType:",
                *module_path_lines,
                "    spec = spec_from_file_location(",
                f'        "{internal}",',
                "        module_path,",
                "    )",
                "    if spec is None or spec.loader is None:",
                '        raise ImportError(f"Unable to load schema module from {module_path}")',
                "    module = module_from_spec(spec)",
                *(
                    [
                        f'    module.__package__ = "{package_name}"',
                    ]
                    if len(f'    module.__package__ = "{package_name}"') <= 88
                    else [
                        "    module.__package__ = (",
                        f'        "{package_name}"',
                        "    )",
                    ]
                ),
                "    spec.loader.exec_module(module)",
                "    return module",
                "",
                "",
                f"def {getter}():",
                f'    """Return the generated Arrow schema for OCSF class {full_uid}."""',
            ]
        )

        return_expr = f"{loader}().{getter}()"
        return_line = f"    return {return_expr}"
        # ruff wraps return statements only when the indented inner line
        # fits within 88 chars (otherwise wrapping doesn't help).
        inner_line = f"        {return_expr}"
        if len(return_line) > 88 and len(inner_line) <= 88:
            lines.extend(
                [
                    "    return (",
                    f"        {return_expr}",
                    "    )",
                ]
            )
        else:
            lines.append(return_line)

        lines.extend(
            [
                "",
                "",
                *const_lines,
            ]
        )

        all_names.append(getter)
        all_names.append(const)

    lines.extend(
        [
            "",
            "",
            "__all__ = [",
        ]
    )
    for name in all_names:
        lines.append(f'    "{name}",')
    lines.extend(
        [
            "]",
            "",
        ]
    )

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Profile metadata
# ---------------------------------------------------------------------------

_EXT_TO_PROFILES: dict[str, list[str]] = {
    "linux": ["linux/linux_users"],
    "macos": ["macos/macos_users"],
    "win": [],
}


def _write_profile_metadata(
    version_dir: Path,
    schema,
) -> None:
    """Write ``_profiles.json`` so :class:`SchemaLoader` can filter at load time."""
    profiles: dict[str, list[str]] = {}
    if schema.profiles:
        for name, profile in schema.profiles.items():
            profiles[name] = (
                sorted(profile.attributes.keys()) if profile.attributes else []
            )

    extension_profiles: dict[str, list[str]] = {}
    if schema.extensions:
        for ext_name in schema.extensions:
            extension_profiles[ext_name] = _EXT_TO_PROFILES.get(ext_name, [ext_name])

    metadata = {
        "profiles": profiles,
        "extension_profiles": extension_profiles,
    }
    path = version_dir / "_profiles.json"
    content = json.dumps(metadata, indent=2, sort_keys=True) + "\n"
    _write_if_changed(path, content)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def _is_stable_version(version: str) -> bool:
    """Return True if *version* is a stable release (no -rc or -dev suffix)."""
    return "-rc" not in version and "-dev" not in version


def _write_if_changed(path: Path, content: str) -> bool:
    """Write *content* to *path* only if it differs from the current contents.

    Returns True if the file was written, False if it was already up to date.
    """
    try:
        if path.read_text(encoding="utf-8") == content:
            return False
    except FileNotFoundError:
        pass
    path.write_text(content, encoding="utf-8")
    return True


def _generate_version(
    version_str: str,
    version_dir: Path,
    class_name_filter: str | None,
    client: OcsfApiClient,
) -> None:
    """Generate object and class schema files for one OCSF version."""
    generator = SchemaGenerator.init(version=version_str, client=client)
    version = generator.version

    objects_dir = version_dir / "objects"
    categories_dir = version_dir / "categories"

    type_map = generator._type_mapper.OCSF_TO_ARROW
    schema_objects = generator.schema.objects
    # Include all profile/extension attributes in generated files;
    # filtering happens at load time via SchemaLoader.
    ignored: set[str] = set()

    _write_profile_metadata(version_dir, generator.schema)

    # Build category UID -> dir-name mapping.
    cat_info: dict[int, str] = {}
    categories = generator.schema.categories
    assert categories is not None, "OCSF schema has no categories"
    for cat in categories.values():
        assert cat.uid is not None
        cat_info[cat.uid] = f"{cat.uid}_{_sanitize_dir_name(cat.caption)}"

    # Group classes by category, optionally filtering by --class-name.
    category_classes: dict[str, list[tuple[int, str]]] = {}
    all_class_names: set[str] = set()

    for cls in generator.schema.classes.values():
        if class_name_filter and cls.name != class_name_filter:
            continue
        if cls.uid is None:
            continue
        cat_uid = cls.uid // 1000
        cat_dir_name = cat_info.get(cat_uid)
        if cat_dir_name is None:
            continue  # skip base_event or other uncategorized classes
        category_classes.setdefault(cat_dir_name, []).append((cls.uid, cls.name))
        all_class_names.add(cls.name)

    if not all_class_names:
        print(f"  no classes found matching --class-name={class_name_filter!r}")
        return

    # Discover all transitively required objects across all selected classes.
    top_level_object_deps: set[str] = set()
    for class_name in all_class_names:
        event_class = generator.schema.classes[class_name]
        for attr in event_class.attributes.values():
            if attr.type not in type_map and attr.type in schema_objects:
                top_level_object_deps.add(attr.type)

    dep_graph = _discover_all_objects(
        top_level_object_deps, schema_objects, type_map, ignored
    )

    # Write object files.
    written = 0
    skipped = 0
    objects_dir.mkdir(parents=True, exist_ok=True)
    init_file = objects_dir / "__init__.py"
    if not init_file.exists():
        init_file.write_text('"""Auto-generated OCSF object schema modules."""\n')

    for obj_name in sorted(dep_graph):
        obj_file = objects_dir / f"{obj_name}.py"
        content = _render_object_file(
            obj_name,
            generator,
            version,
            allowed_deps=dep_graph[obj_name],
            ignored_attrs=ignored,
        )
        if _write_if_changed(obj_file, content):
            written += 1
        else:
            skipped += 1

    # Write class files grouped by category.
    categories_dir.mkdir(parents=True, exist_ok=True)
    cat_init = categories_dir / "__init__.py"
    if not cat_init.exists():
        cat_init.write_text('"""Auto-generated OCSF category schema packages."""\n')

    for cat_dir_name, entries in sorted(category_classes.items()):
        cat_dir = categories_dir / cat_dir_name
        cat_dir.mkdir(parents=True, exist_ok=True)

        for full_uid, class_name in sorted(entries):
            class_file = cat_dir / f"{full_uid}_{class_name}.py"
            content = _render_class_file(
                class_name, generator, version, ignored_attrs=ignored
            )
            if _write_if_changed(class_file, content):
                written += 1
            else:
                skipped += 1

        # Generate __init__.py for this category.
        cat_package = _dir_to_package(cat_dir)
        init_content = _render_category_init(entries, cat_package)
        if _write_if_changed(cat_dir / "__init__.py", init_content):
            written += 1
        else:
            skipped += 1

    # Write version-level __init__.py.
    version_init = version_dir / "__init__.py"
    if not version_init.exists():
        version_init.write_text(f'"""Auto-generated OCSF schema v{version}."""\n')

    print(
        f"  version {version}: {len(dep_graph)} objects, "
        f"{len(all_class_names)} classes "
        f"({written} written, {skipped} unchanged)"
    )


def build_parser() -> ArgumentParser:
    parser = ArgumentParser(
        description=(
            "Generate versioned Python schema modules from OCSF classes, "
            "organized by category.  Each version gets its own isolated tree "
            "under <schema-dir>/<version>/."
        )
    )
    parser.add_argument(
        "--class-name",
        default=None,
        help="OCSF class name to render (default: all classes)",
    )
    parser.add_argument(
        "--version",
        default="all",
        help=(
            'OCSF schema version to generate: a version string (e.g. "1.8.0"), '
            '"default" for the latest stable, or "all" for every stable release '
            "(default: all)"
        ),
    )
    parser.add_argument(
        "--schema-dir",
        default="src/py_ocsf_arrow/schema",
        help="Root schema directory (default: src/py_ocsf_arrow/schema)",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()

    schema_dir = Path(args.schema_dir)
    schema_dir.mkdir(parents=True, exist_ok=True)
    schema_init = schema_dir / "__init__.py"
    if not schema_init.exists():
        schema_init.write_text(
            '"""Schema modules generated from OCSF class definitions."""\n'
        )

    client = OcsfApiClient(cache_dir=CACHE_DIR)

    # Resolve which versions to generate.
    if args.version == "all":
        versions = [v for v in client.get_versions() if _is_stable_version(v)]
    elif args.version == "default":
        versions = [client.get_default_version()]
    else:
        versions = [args.version]

    print(f"Generating schemas for {len(versions)} version(s): {versions}")

    for version_str in sorted(versions):
        version_dir = schema_dir / version_str
        _generate_version(version_str, version_dir, args.class_name, client)

    print("\nDone.")


if __name__ == "__main__":
    main()
