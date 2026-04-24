"""Load generated Arrow schemas from versioned schema modules.

Generated schemas live under ``src/py_ocsf_arrow/schema/<version>/`` and
cannot be imported with normal Python ``import`` statements because version
directories contain dots (e.g. ``1.8.0``) and class files start with numeric
UIDs (e.g. ``2002_vulnerability_finding.py``).

This module provides :class:`SchemaLoader` and the convenience helpers
:func:`load_class_schema` / :func:`load_object_schema` so you never have to
write the ``importlib.util.spec_from_file_location`` boilerplate yourself.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
from types import ModuleType

import pyarrow as pa


# ---------------------------------------------------------------------------
# Package-level schema directory
# ---------------------------------------------------------------------------

SCHEMA_DIR = Path(__file__).parent / "schema"


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _looks_like_version(name: str) -> bool:
    """Return True if *name* looks like a semver-style version string."""
    return bool(name) and name[0].isdigit() and "." in name


def _version_key(v: str) -> tuple[int, ...]:
    """Return a tuple suitable for semver-style sorting of ``v``."""
    try:
        return tuple(int(x) for x in v.split("."))
    except ValueError:
        return (0,)


def _resolve_version(version: str, schema_dir: Path) -> str:
    """Resolve *version* to an installed version string.

    * ``"default"`` – picks the highest installed stable version.
    * Any other string – validated against the installed directories.
    """
    if version == "default":
        candidates = sorted(
            (
                d.name
                for d in schema_dir.iterdir()
                if d.is_dir()
                and _looks_like_version(d.name)
                and "-rc" not in d.name
                and "-dev" not in d.name
            ),
            key=_version_key,
        )
        if not candidates:
            raise FileNotFoundError(
                f"No generated schema versions found under {schema_dir}. "
                "Run `just generate` first."
            )
        return candidates[-1]

    version_dir = schema_dir / version
    if not version_dir.is_dir():
        raise FileNotFoundError(
            f"No generated schema for version '{version}' at {version_dir}. "
            f"Run `just generate {version}` to generate it."
        )
    return version


def _load_module_from_path(path: Path, module_name: str, package: str) -> ModuleType:
    """Load *path* as a module named *module_name* with *package* set."""
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load module from {path}")
    module = importlib.util.module_from_spec(spec)
    module.__package__ = package
    spec.loader.exec_module(module)
    return module


# ---------------------------------------------------------------------------
# Profile metadata helpers
# ---------------------------------------------------------------------------

ProfileMetadata = dict[str, dict[str, list[str]]]


def _load_profile_metadata(version_dir: Path) -> ProfileMetadata:
    """Load ``_profiles.json`` from a generated version directory."""
    path = version_dir / "_profiles.json"
    if not path.exists():
        raise FileNotFoundError(
            f"Profile metadata not found at {path}. "
            f"Re-generate schemas with `just generate` to create it."
        )
    return json.loads(path.read_text(encoding="utf-8"))


def _compute_ignored_attrs(
    ext: list[str] | None,
    prf: list[str] | None,
    metadata: ProfileMetadata,
) -> set[str]:
    """Compute which attributes to exclude, mirroring ``OCSFArrow.init()`` semantics.

    * ``ext=None`` / ``prf=None`` → exclude **all** profile attributes (base only).
    * ``ext=[]`` / ``prf=[]`` → same as ``None`` — exclude all.
    * ``ext=["linux"]`` / ``prf=["cloud"]`` → include only those; exclude the rest.
    """
    all_profiles: dict[str, list[str]] = metadata["profiles"]
    ext_profile_map: dict[str, list[str]] = metadata.get("extension_profiles", {})

    # Determine which profiles to *ignore* (same inversion as base.py _items()).
    def _profiles_to_ignore(
        items: list[str] | None, available: dict[str, list[str]], label: str
    ) -> list[str]:
        if items is None or len(items) == 0:
            return list(available.keys())
        invalid = [i for i in items if i not in available]
        if invalid:
            raise ValueError(
                f"{label}(s) {invalid} not found. Available: {sorted(available.keys())}"
            )
        return [name for name in available.keys() if name not in items]

    ignored_ext_names = _profiles_to_ignore(ext, ext_profile_map, "Extension")
    ignored_prf_names = _profiles_to_ignore(prf, all_profiles, "Profile")

    # Map ignored extensions → their implied profile names.
    ext_implied: list[str] = []
    for ext_name in ignored_ext_names:
        ext_implied.extend(ext_profile_map.get(ext_name, []))

    all_ignored_profile_names = set(ignored_prf_names) | set(ext_implied)

    # Collect all attribute names contributed by the ignored profiles.
    ignored_attrs: set[str] = set()
    for profile_name in all_ignored_profile_names:
        if profile_name in all_profiles:
            ignored_attrs.update(all_profiles[profile_name])

    return ignored_attrs


def _filter_schema(schema: pa.Schema, ignored_attrs: set[str]) -> pa.Schema:
    """Return *schema* with top-level fields in *ignored_attrs* removed."""
    if not ignored_attrs:
        return schema
    return pa.schema([f for f in schema if f.name not in ignored_attrs])


# ---------------------------------------------------------------------------
# SchemaLoader
# ---------------------------------------------------------------------------


class SchemaLoader:
    """Load generated Arrow schemas from versioned schema modules.

    Parameters
    ----------
    version:
        The OCSF schema version to load from (e.g. ``"1.8.0"``).  Pass
        ``"default"`` (the default) to use the highest installed stable version.
    ext:
        Extension include-list.  ``None`` (default) or ``[]`` excludes all
        extension-contributed profile attributes.  Pass e.g. ``["linux"]`` to
        keep only Linux extension attributes.
    prf:
        Profile include-list.  ``None`` (default) or ``[]`` excludes all
        profile attributes (base schema only).  Pass e.g. ``["cloud"]`` to
        include only cloud profile attributes.
    schema_dir:
        Override the root schema directory.  Defaults to the ``schema/``
        directory inside the installed ``py_ocsf_arrow`` package.

    Examples
    --------
    Base schema (no profiles):

    >>> loader = SchemaLoader("1.8.0")
    >>> schema = loader.load_class("vulnerability_finding")

    Include specific profiles:

    >>> loader = SchemaLoader("1.8.0", prf=["cloud", "host"])
    >>> schema = loader.load_class("vulnerability_finding")

    Include all profiles:

    >>> all_profiles = SchemaLoader("1.8.0").available_profiles()
    >>> loader = SchemaLoader("1.8.0", prf=all_profiles)
    """

    def __init__(
        self,
        version: str = "default",
        ext: list[str] | None = None,
        prf: list[str] | None = None,
        schema_dir: Path | None = None,
    ) -> None:
        self._schema_dir = schema_dir or SCHEMA_DIR
        self.version = _resolve_version(version, self._schema_dir)
        self._version_dir = self._schema_dir / self.version
        self._category_cache: dict[str, ModuleType] = {}

        # Load profile metadata and compute the set of attributes to filter.
        meta_path = self._version_dir / "_profiles.json"
        if meta_path.exists():
            self._profile_metadata: ProfileMetadata | None = _load_profile_metadata(
                self._version_dir
            )
            self._ignored_attrs = _compute_ignored_attrs(
                ext, prf, self._profile_metadata
            )
        elif ext is not None or prf is not None:
            raise FileNotFoundError(
                f"Profile metadata not found at {meta_path}. "
                f"Re-generate schemas with `just generate` to enable profile filtering."
            )
        else:
            # No metadata and no filtering requested — backwards-compatible mode.
            self._profile_metadata = None
            self._ignored_attrs = set()

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    @property
    def _categories_dir(self) -> Path:
        return self._version_dir / "categories"

    @property
    def _objects_dir(self) -> Path:
        return self._version_dir / "objects"

    def _find_class_category(self, class_name: str) -> Path:
        """Return the category directory that owns *class_name*.

        Files are named ``<uid>_<class_name>.py``; we parse the stem rather
        than using glob patterns to avoid spurious substring matches.
        """
        for cat_dir in sorted(self._categories_dir.iterdir()):
            if not cat_dir.is_dir():
                continue
            for f in cat_dir.glob("*.py"):
                if f.name == "__init__.py":
                    continue
                parts = f.stem.split("_", 1)
                if len(parts) == 2 and parts[0].isdigit() and parts[1] == class_name:
                    return cat_dir
        raise KeyError(
            f"Class '{class_name}' not found in version {self.version}. "
            f"Run `loader.available_classes()` to see what is available."
        )

    def _load_category(self, cat_dir: Path) -> ModuleType:
        """Load and cache the ``__init__.py`` for *cat_dir*."""
        key = cat_dir.name
        if key not in self._category_cache:
            safe_version = self.version.replace(".", "_")
            pkg = f"_py_ocsf_arrow_{safe_version}_{key}"
            self._category_cache[key] = _load_module_from_path(
                cat_dir / "__init__.py", pkg, pkg
            )
        return self._category_cache[key]

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def load_class(self, class_name: str) -> pa.Schema:
        """Load the generated Arrow schema for an OCSF class.

        Profile attributes are filtered based on the ``ext`` / ``prf``
        parameters passed at construction time.

        Parameters
        ----------
        class_name:
            OCSF class name, e.g. ``"vulnerability_finding"``.

        Returns
        -------
        pa.Schema

        Raises
        ------
        KeyError
            If *class_name* is not found in the installed version.
        """
        cat_dir = self._find_class_category(class_name)
        module = self._load_category(cat_dir)
        getter = f"get_{class_name}_schema"
        if not hasattr(module, getter):
            raise KeyError(
                f"Class '{class_name}' was found on disk but '{getter}' is missing "
                f"from the category module.  Try re-generating: `just generate {self.version}`."
            )
        schema = getattr(module, getter)()
        return _filter_schema(schema, self._ignored_attrs)

    def load_object(self, object_name: str) -> pa.Schema:
        """Load the generated Arrow schema for an OCSF object.

        Parameters
        ----------
        object_name:
            OCSF object name, e.g. ``"cve"``.

        Returns
        -------
        pa.Schema

        Raises
        ------
        KeyError
            If *object_name* is not found in the installed version.
        """
        obj_path = self._objects_dir / f"{object_name}.py"
        if not obj_path.exists():
            raise KeyError(
                f"Object '{object_name}' not found in version {self.version}. "
                f"Run `loader.available_objects()` to see what is available."
            )
        safe_version = self.version.replace(".", "_")
        pkg = f"_py_ocsf_arrow_{safe_version}_objects"
        module = _load_module_from_path(obj_path, f"{pkg}_{object_name}", pkg)
        getter = f"get_{object_name}_schema"
        return getattr(module, getter)()

    def available_classes(self) -> list[str]:
        """Return the names of all available class schemas for this version."""
        classes: list[str] = []
        for cat_dir in sorted(self._categories_dir.iterdir()):
            if not cat_dir.is_dir():
                continue
            for f in sorted(cat_dir.glob("*.py")):
                if f.name == "__init__.py":
                    continue
                parts = f.stem.split("_", 1)
                if len(parts) == 2 and parts[0].isdigit():
                    classes.append(parts[1])
        return classes

    def available_objects(self) -> list[str]:
        """Return the names of all available object schemas for this version."""
        return sorted(
            f.stem for f in self._objects_dir.glob("*.py") if f.name != "__init__.py"
        )

    @classmethod
    def available_versions(cls, schema_dir: Path | None = None) -> list[str]:
        """Return installed stable schema versions, sorted newest-first.

        Parameters
        ----------
        schema_dir:
            Defaults to the package-level schema directory.
        """
        root = schema_dir or SCHEMA_DIR
        if not root.is_dir():
            return []
        candidates = sorted(
            (
                d.name
                for d in root.iterdir()
                if d.is_dir()
                and _looks_like_version(d.name)
                and "-rc" not in d.name
                and "-dev" not in d.name
            ),
            key=_version_key,
            reverse=True,
        )
        return candidates

    def available_profiles(self) -> list[str]:
        """Return the profile names available for this version."""
        if self._profile_metadata is None:
            return []
        return sorted(self._profile_metadata["profiles"].keys())

    def available_extensions(self) -> list[str]:
        """Return the extension names available for this version."""
        if self._profile_metadata is None:
            return []
        return sorted(self._profile_metadata.get("extension_profiles", {}).keys())


# ---------------------------------------------------------------------------
# Module-level convenience helpers
# ---------------------------------------------------------------------------


def load_class_schema(
    class_name: str,
    version: str = "default",
    ext: list[str] | None = None,
    prf: list[str] | None = None,
) -> pa.Schema:
    """Load a generated Arrow schema for an OCSF class.

    Parameters
    ----------
    class_name:
        OCSF class name, e.g. ``"vulnerability_finding"``.
    version:
        OCSF schema version (e.g. ``"1.8.0"``), or ``"default"`` for the
        latest installed stable version.
    ext:
        Extension include-list (see :class:`SchemaLoader`).
    prf:
        Profile include-list (see :class:`SchemaLoader`).

    Examples
    --------
    >>> schema = load_class_schema("vulnerability_finding", version="1.8.0")
    """
    return SchemaLoader(version, ext=ext, prf=prf).load_class(class_name)


def load_object_schema(object_name: str, version: str = "default") -> pa.Schema:
    """Load a generated Arrow schema for an OCSF object.

    Parameters
    ----------
    object_name:
        OCSF object name, e.g. ``"cve"``.
    version:
        OCSF schema version (e.g. ``"1.8.0"``), or ``"default"`` for the
        latest installed stable version.

    Examples
    --------
    >>> schema = load_object_schema("cve", version="1.8.0")
    """
    return SchemaLoader(version).load_object(object_name)
