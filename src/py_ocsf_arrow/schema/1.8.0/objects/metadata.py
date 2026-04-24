"""Auto-generated Arrow schema for OCSF object 'metadata'.

Generated from version 1.8.0 at 2026-04-24T03:47:42+00:00.
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
KEY_VALUE_OBJECT_SCHEMA = _load_dep("key_value_object").KEY_VALUE_OBJECT_SCHEMA
LOGGER_SCHEMA = _load_dep("logger").LOGGER_SCHEMA
PRODUCT_SCHEMA = _load_dep("product").PRODUCT_SCHEMA
REPORTER_SCHEMA = _load_dep("reporter").REPORTER_SCHEMA
TIMESPAN_SCHEMA = _load_dep("timespan").TIMESPAN_SCHEMA
TRANSFORMATION_INFO_SCHEMA = _load_dep("transformation_info").TRANSFORMATION_INFO_SCHEMA


def get_metadata_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'metadata'."""
    return pa.schema(
        [
            pa.field("correlation_uid", pa.string(), nullable=True),
            pa.field("debug", pa.list_(pa.string()), nullable=True),
            pa.field("event_code", pa.string(), nullable=True),
            pa.field("extension", pa.struct(list(EXTENSION_SCHEMA)), nullable=True),
            pa.field(
                "extensions", pa.list_(pa.struct(list(EXTENSION_SCHEMA))), nullable=True
            ),
            pa.field("is_truncated", pa.bool8(), nullable=True),
            pa.field("labels", pa.list_(pa.string()), nullable=True),
            pa.field("log_format", pa.string(), nullable=True),
            pa.field("log_level", pa.string(), nullable=True),
            pa.field("log_name", pa.string(), nullable=True),
            pa.field("log_provider", pa.string(), nullable=True),
            pa.field("log_source", pa.string(), nullable=True),
            pa.field("log_version", pa.string(), nullable=True),
            pa.field("logged_time", pa.int64(), nullable=True),
            pa.field("logged_time_dt", pa.string(), nullable=True),
            pa.field(
                "loggers", pa.list_(pa.struct(list(LOGGER_SCHEMA))), nullable=True
            ),
            pa.field("modified_time", pa.int64(), nullable=True),
            pa.field("modified_time_dt", pa.string(), nullable=True),
            pa.field("original_event_uid", pa.string(), nullable=True),
            pa.field("original_time", pa.string(), nullable=True),
            pa.field("processed_time", pa.int64(), nullable=True),
            pa.field("processed_time_dt", pa.string(), nullable=True),
            pa.field("product", pa.struct(list(PRODUCT_SCHEMA)), nullable=False),
            pa.field("profiles", pa.list_(pa.string()), nullable=True),
            pa.field("reporter", pa.struct(list(REPORTER_SCHEMA)), nullable=True),
            pa.field("sequence", pa.int32(), nullable=True),
            pa.field("source", pa.string(), nullable=True),
            pa.field(
                "tags",
                pa.list_(pa.struct(list(KEY_VALUE_OBJECT_SCHEMA))),
                nullable=True,
            ),
            pa.field("tenant_uid", pa.string(), nullable=True),
            pa.field(
                "total_queued_duration", pa.struct(list(TIMESPAN_SCHEMA)), nullable=True
            ),
            pa.field(
                "transformation_info_list",
                pa.list_(pa.struct(list(TRANSFORMATION_INFO_SCHEMA))),
                nullable=True,
            ),
            pa.field("transmit_time", pa.int64(), nullable=True),
            pa.field("transmit_time_dt", pa.string(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("untruncated_size", pa.int32(), nullable=True),
            pa.field("version", pa.string(), nullable=False),
        ]
    )


METADATA_SCHEMA = get_metadata_schema()
