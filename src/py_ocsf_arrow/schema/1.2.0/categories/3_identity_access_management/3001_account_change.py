"""Auto-generated Arrow schema for OCSF class 'account_change'.

OCSF version 1.2.0.
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


ACTOR_SCHEMA = _load_dep("actor").ACTOR_SCHEMA
API_SCHEMA = _load_dep("api").API_SCHEMA
CLOUD_SCHEMA = _load_dep("cloud").CLOUD_SCHEMA
DEVICE_SCHEMA = _load_dep("device").DEVICE_SCHEMA
ENRICHMENT_SCHEMA = _load_dep("enrichment").ENRICHMENT_SCHEMA
HTTP_REQUEST_SCHEMA = _load_dep("http_request").HTTP_REQUEST_SCHEMA
METADATA_SCHEMA = _load_dep("metadata").METADATA_SCHEMA
NETWORK_ENDPOINT_SCHEMA = _load_dep("network_endpoint").NETWORK_ENDPOINT_SCHEMA
OBJECT_SCHEMA = _load_dep("object").OBJECT_SCHEMA
OBSERVABLE_SCHEMA = _load_dep("observable").OBSERVABLE_SCHEMA
POLICY_SCHEMA = _load_dep("policy").POLICY_SCHEMA
USER_SCHEMA = _load_dep("user").USER_SCHEMA


def get_account_change_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF class 'account_change'."""
    return pa.schema(
        [
            pa.field("activity_id", pa.int32(), nullable=False),
            pa.field("activity_name", pa.string(), nullable=True),
            pa.field("actor", pa.struct(list(ACTOR_SCHEMA)), nullable=True),
            pa.field("api", pa.struct(list(API_SCHEMA)), nullable=True),
            pa.field("category_name", pa.string(), nullable=True),
            pa.field("category_uid", pa.int32(), nullable=False),
            pa.field("class_name", pa.string(), nullable=True),
            pa.field("class_uid", pa.int32(), nullable=False),
            pa.field("cloud", pa.struct(list(CLOUD_SCHEMA)), nullable=False),
            pa.field("count", pa.int32(), nullable=True),
            pa.field("device", pa.struct(list(DEVICE_SCHEMA)), nullable=True),
            pa.field("duration", pa.int32(), nullable=True),
            pa.field("end_time", pa.int64(), nullable=True),
            pa.field("end_time_dt", pa.string(), nullable=True),
            pa.field(
                "enrichments",
                pa.list_(pa.struct(list(ENRICHMENT_SCHEMA))),
                nullable=True,
            ),
            pa.field(
                "http_request",
                pa.struct(list(HTTP_REQUEST_SCHEMA)),
                nullable=True,
            ),
            pa.field("message", pa.string(), nullable=True),
            pa.field("metadata", pa.struct(list(METADATA_SCHEMA)), nullable=False),
            pa.field(
                "observables",
                pa.list_(pa.struct(list(OBSERVABLE_SCHEMA))),
                nullable=True,
            ),
            pa.field("policy", pa.struct(list(POLICY_SCHEMA)), nullable=True),
            pa.field("raw_data", pa.string(), nullable=True),
            pa.field("severity", pa.string(), nullable=True),
            pa.field("severity_id", pa.int32(), nullable=False),
            pa.field(
                "src_endpoint",
                pa.struct(list(NETWORK_ENDPOINT_SCHEMA)),
                nullable=True,
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
            pa.field("type_uid", pa.int64(), nullable=False),
            pa.field("unmapped", pa.struct(list(OBJECT_SCHEMA)), nullable=True),
            pa.field("user", pa.struct(list(USER_SCHEMA)), nullable=False),
            pa.field("user_result", pa.struct(list(USER_SCHEMA)), nullable=True),
        ]
    )


ACCOUNT_CHANGE_SCHEMA = get_account_change_schema()
