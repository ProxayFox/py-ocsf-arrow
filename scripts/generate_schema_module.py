from __future__ import annotations

import json
from argparse import ArgumentParser
from datetime import datetime, timezone
from pathlib import Path

import pyarrow as pa

from py_ocsf_arrow import SchemaGenerator

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
        lines.append(
            f"        pa.field({json.dumps(attr_name)}, {type_expr}, nullable={nullable}),"
        )
    return "\n".join(lines)


def _imports_block(direct_deps: set[str], package: str) -> str:
    lines = ["import pyarrow as pa"]
    for dep in sorted(direct_deps):
        lines.append(f"from {package}.{dep} import {dep.upper()}_SCHEMA")
    return "\n".join(lines)


def _render_object_file(
    object_name: str,
    generator: SchemaGenerator,
    version: str,
    timestamp: str,
    objects_package: str,
    allowed_deps: set[str],
) -> str:
    ocsf_obj = generator.schema.objects[object_name]
    type_map = generator._type_mapper.OCSF_TO_ARROW
    ignored = generator._ignored_attr
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

    return (
        f'"""Auto-generated Arrow schema for OCSF object \'{object_name}\'.\n\n'
        f"Generated from version {version} at {timestamp}.\n"
        '"""\n\n'
        f"{_imports_block(direct_deps, objects_package)}\n\n\n"
        f"def {fn_name}() -> pa.Schema:\n"
        f'    """Return the Arrow schema for OCSF object \'{object_name}\'."""\n'
        "    return pa.schema(\n"
        "        [\n"
        f"{fields_block}\n"
        "        ]\n"
        "    )\n\n\n"
        f"{const_name} = {fn_name}()\n"
    )


def _render_class_file(
    class_name: str,
    generator: SchemaGenerator,
    version: str,
    timestamp: str,
    objects_package: str,
) -> str:
    event_class = generator.schema.classes[class_name]
    type_map = generator._type_mapper.OCSF_TO_ARROW
    ignored = generator._ignored_attr
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

    return (
        f'"""Auto-generated Arrow schema for OCSF class \'{class_name}\'.\n\n'
        f"Generated from version {version} at {timestamp}.\n"
        '"""\n\n'
        f"{_imports_block(direct_deps, objects_package)}\n\n\n"
        f"def {fn_name}() -> pa.Schema:\n"
        f'    """Return the Arrow schema for OCSF class \'{class_name}\'."""\n'
        "    return pa.schema(\n"
        "        [\n"
        f"{fields_block}\n"
        "        ]\n"
        "    )\n\n\n"
        f"{const_name} = {fn_name}()\n"
    )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def build_parser() -> ArgumentParser:
    parser = ArgumentParser(
        description=(
            "Generate split Python schema modules from an OCSF class. "
            "Each referenced OCSF object gets its own file under --objects-dir; "
            "the class file imports from those objects rather than inlining."
        )
    )
    parser.add_argument(
        "--class-name",
        default="vulnerability_finding",
        help="OCSF class name to render (default: vulnerability_finding)",
    )
    parser.add_argument(
        "--version",
        default="default",
        help="OCSF schema version (default: default)",
    )
    parser.add_argument(
        "--output",
        default="src/py_ocsf_arrow/schema/findings/2002_vulnerability_finding.py",
        help="Output path for the class schema file",
    )
    parser.add_argument(
        "--objects-dir",
        default="src/py_ocsf_arrow/schema/objects",
        help="Directory to write per-object schema files (default: src/py_ocsf_arrow/schema/objects)",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()

    generator = SchemaGenerator.init(version=args.version)
    version = generator.version
    timestamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat()

    type_map = generator._type_mapper.OCSF_TO_ARROW
    schema_objects = generator.schema.objects
    ignored = generator._ignored_attr
    event_class = generator.schema.classes[args.class_name]

    # Discover which top-level attributes of the class are objects.
    top_level_object_deps: set[str] = set()
    for attr in event_class.attributes.values():
        if attr.type not in type_map and attr.type in schema_objects:
            top_level_object_deps.add(attr.type)

    # BFS to discover all transitively required objects.
    dep_graph = _discover_all_objects(
        top_level_object_deps, schema_objects, type_map, ignored
    )

    # Derive Python package name from the objects directory.
    objects_dir = Path(args.objects_dir)
    src_root = Path("src")
    try:
        rel = objects_dir.relative_to(src_root)
        objects_package = ".".join(rel.parts)
    except ValueError:
        objects_package = ".".join(objects_dir.parts)

    # Write object files.
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
            timestamp,
            objects_package,
            allowed_deps=dep_graph[obj_name],
        )
        obj_file.write_text(content, encoding="utf-8")
        print(f"  wrote object: {obj_file}")

    # Write class file.
    class_output = Path(args.output)
    class_output.parent.mkdir(parents=True, exist_ok=True)
    content = _render_class_file(
        args.class_name, generator, version, timestamp, objects_package
    )
    class_output.write_text(content, encoding="utf-8")
    print(f"wrote class:  {class_output}")
    print(f"total objects written: {len(dep_graph)}")


if __name__ == "__main__":
    main()
