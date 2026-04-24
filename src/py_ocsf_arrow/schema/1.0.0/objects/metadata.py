"""Auto-generated Arrow schema for OCSF object 'metadata'.

Generated from version 1.0.0 at 2026-04-24T03:47:40+00:00.
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


EXTENSION_SCHEMA = _load_dep("extension").EXTENSION_SCHEMA
PRODUCT_SCHEMA = _load_dep("product").PRODUCT_SCHEMA


def get_metadata_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'metadata'."""
    return pa.schema(
        [
            pa.field("correlation_uid", pa.string(), nullable=True),
            pa.field("event_code", pa.string(), nullable=True),
            pa.field("extension", pa.struct(list(EXTENSION_SCHEMA)), nullable=True),
            pa.field("labels", pa.list_(pa.string()), nullable=True),
            pa.field("log_name", pa.string(), nullable=True),
            pa.field("log_provider", pa.string(), nullable=True),
            pa.field("log_version", pa.string(), nullable=True),
            pa.field("logged_time", pa.int64(), nullable=True),
            pa.field("logged_time_dt", pa.string(), nullable=True),
            pa.field("modified_time", pa.int64(), nullable=True),
            pa.field("modified_time_dt", pa.string(), nullable=True),
            pa.field("original_time", pa.string(), nullable=True),
            pa.field("processed_time", pa.int64(), nullable=True),
            pa.field("processed_time_dt", pa.string(), nullable=True),
            pa.field("product", pa.struct(list(PRODUCT_SCHEMA)), nullable=False),
            pa.field("profiles", pa.list_(pa.string()), nullable=True),
            pa.field("sequence", pa.int32(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("version", pa.string(), nullable=False),
        ]
    )


METADATA_SCHEMA = get_metadata_schema()
