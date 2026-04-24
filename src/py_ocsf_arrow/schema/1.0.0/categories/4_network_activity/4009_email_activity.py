"""Auto-generated Arrow schema for OCSF class 'email_activity'.

Generated from version 1.0.0 at 2026-04-24T03:47:40+00:00.
"""

import importlib.util
from pathlib import Path

import pyarrow as pa

_OBJECTS_DIR = Path(__file__).resolve().parents[2] / "objects"


def _load_dep(name: str):
    spec = importlib.util.spec_from_file_location(name, _OBJECTS_DIR / f"{name}.py")
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


EMAIL_SCHEMA = _load_dep("email").EMAIL_SCHEMA
EMAIL_AUTH_SCHEMA = _load_dep("email_auth").EMAIL_AUTH_SCHEMA
ENRICHMENT_SCHEMA = _load_dep("enrichment").ENRICHMENT_SCHEMA
METADATA_SCHEMA = _load_dep("metadata").METADATA_SCHEMA
NETWORK_ENDPOINT_SCHEMA = _load_dep("network_endpoint").NETWORK_ENDPOINT_SCHEMA
OBJECT_SCHEMA = _load_dep("object").OBJECT_SCHEMA
OBSERVABLE_SCHEMA = _load_dep("observable").OBSERVABLE_SCHEMA


def get_email_activity_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF class 'email_activity'."""
    return pa.schema(
        [
            pa.field("activity_id", pa.int32(), nullable=True),
            pa.field("activity_name", pa.string(), nullable=True),
            pa.field("attempt", pa.int32(), nullable=True),
            pa.field("banner", pa.string(), nullable=True),
            pa.field("category_name", pa.string(), nullable=True),
            pa.field("category_uid", pa.int32(), nullable=False),
            pa.field("class_name", pa.string(), nullable=True),
            pa.field("class_uid", pa.int32(), nullable=False),
            pa.field("count", pa.int32(), nullable=True),
            pa.field("direction", pa.string(), nullable=True),
            pa.field("direction_id", pa.int32(), nullable=False),
            pa.field(
                "dst_endpoint", pa.struct(list(NETWORK_ENDPOINT_SCHEMA)), nullable=True
            ),
            pa.field("duration", pa.int32(), nullable=True),
            pa.field("email", pa.struct(list(EMAIL_SCHEMA)), nullable=False),
            pa.field("email_auth", pa.struct(list(EMAIL_AUTH_SCHEMA)), nullable=True),
            pa.field("end_time", pa.int64(), nullable=True),
            pa.field("end_time_dt", pa.string(), nullable=True),
            pa.field(
                "enrichments",
                pa.list_(pa.struct(list(ENRICHMENT_SCHEMA))),
                nullable=True,
            ),
            pa.field("message", pa.string(), nullable=True),
            pa.field("metadata", pa.struct(list(METADATA_SCHEMA)), nullable=False),
            pa.field(
                "observables",
                pa.list_(pa.struct(list(OBSERVABLE_SCHEMA))),
                nullable=True,
            ),
            pa.field("raw_data", pa.string(), nullable=True),
            pa.field("severity", pa.string(), nullable=True),
            pa.field("severity_id", pa.int32(), nullable=False),
            pa.field("smtp_hello", pa.string(), nullable=True),
            pa.field(
                "src_endpoint", pa.struct(list(NETWORK_ENDPOINT_SCHEMA)), nullable=True
            ),
            pa.field("start_time", pa.int64(), nullable=True),
            pa.field("start_time_dt", pa.string(), nullable=True),
            pa.field("status", pa.string(), nullable=True),
            pa.field("status_code", pa.string(), nullable=True),
            pa.field("status_detail", pa.string(), nullable=True),
            pa.field("status_id", pa.int32(), nullable=True),
            pa.field("time", pa.int64(), nullable=False),
            pa.field("time_dt", pa.string(), nullable=True),
            pa.field("timezone_offset", pa.int32(), nullable=True),
            pa.field("type_name", pa.string(), nullable=True),
            pa.field("type_uid", pa.int32(), nullable=False),
            pa.field("unmapped", pa.struct(list(OBJECT_SCHEMA)), nullable=True),
        ]
    )


EMAIL_ACTIVITY_SCHEMA = get_email_activity_schema()
