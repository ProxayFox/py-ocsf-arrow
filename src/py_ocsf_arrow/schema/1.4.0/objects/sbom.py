"""Auto-generated Arrow schema for OCSF object 'sbom'.

Generated from version 1.4.0 at 2026-04-24T03:47:41+00:00.
"""

import importlib.util
from pathlib import Path

import pyarrow as pa

_OBJECTS_DIR = Path(__file__).parent


def _load_dep(name: str):
    spec = importlib.util.spec_from_file_location(name, _OBJECTS_DIR / f"{name}.py")
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


PACKAGE_SCHEMA = _load_dep("package").PACKAGE_SCHEMA
PRODUCT_SCHEMA = _load_dep("product").PRODUCT_SCHEMA
SOFTWARE_COMPONENT_SCHEMA = _load_dep("software_component").SOFTWARE_COMPONENT_SCHEMA


def get_sbom_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'sbom'."""
    return pa.schema(
        [
            pa.field("created_time", pa.int64(), nullable=True),
            pa.field("created_time_dt", pa.string(), nullable=True),
            pa.field("package", pa.struct(list(PACKAGE_SCHEMA)), nullable=False),
            pa.field("product", pa.struct(list(PRODUCT_SCHEMA)), nullable=True),
            pa.field(
                "software_components",
                pa.list_(pa.struct(list(SOFTWARE_COMPONENT_SCHEMA))),
                nullable=False,
            ),
        ]
    )


SBOM_SCHEMA = get_sbom_schema()
