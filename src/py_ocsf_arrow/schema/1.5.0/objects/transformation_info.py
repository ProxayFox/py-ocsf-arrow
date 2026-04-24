"""Auto-generated Arrow schema for OCSF object 'transformation_info'.

Generated from version 1.5.0 at 2026-04-24T03:47:41+00:00.
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


PRODUCT_SCHEMA = _load_dep("product").PRODUCT_SCHEMA


def get_transformation_info_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'transformation_info'."""
    return pa.schema(
        [
            pa.field("lang", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("product", pa.struct(list(PRODUCT_SCHEMA)), nullable=True),
            pa.field("time", pa.int64(), nullable=True),
            pa.field("time_dt", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("url_string", pa.string(), nullable=True),
        ]
    )


TRANSFORMATION_INFO_SCHEMA = get_transformation_info_schema()
