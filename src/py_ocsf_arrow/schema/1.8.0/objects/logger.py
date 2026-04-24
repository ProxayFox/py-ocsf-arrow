"""Auto-generated Arrow schema for OCSF object 'logger'.

OCSF version 1.8.0.
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


DEVICE_SCHEMA = _load_dep("device").DEVICE_SCHEMA
PRODUCT_SCHEMA = _load_dep("product").PRODUCT_SCHEMA


def get_logger_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'logger'."""
    return pa.schema(
        [
            pa.field("device", pa.struct(list(DEVICE_SCHEMA)), nullable=True),
            pa.field("event_uid", pa.string(), nullable=True),
            pa.field("is_truncated", pa.bool8(), nullable=True),
            pa.field("log_format", pa.string(), nullable=True),
            pa.field("log_level", pa.string(), nullable=True),
            pa.field("log_name", pa.string(), nullable=True),
            pa.field("log_provider", pa.string(), nullable=True),
            pa.field("log_version", pa.string(), nullable=True),
            pa.field("logged_time", pa.int64(), nullable=True),
            pa.field("logged_time_dt", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("product", pa.struct(list(PRODUCT_SCHEMA)), nullable=True),
            pa.field("transmit_time", pa.int64(), nullable=True),
            pa.field("transmit_time_dt", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("untruncated_size", pa.int32(), nullable=True),
            pa.field("version", pa.string(), nullable=True),
        ]
    )


LOGGER_SCHEMA = get_logger_schema()
