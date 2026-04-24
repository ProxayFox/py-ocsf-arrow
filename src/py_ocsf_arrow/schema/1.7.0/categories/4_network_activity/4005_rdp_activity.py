"""Auto-generated Arrow schema for OCSF class 'rdp_activity'.

Generated from version 1.7.0 at 2026-04-24T03:47:42+00:00.
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


DISPLAY_SCHEMA = _load_dep("display").DISPLAY_SCHEMA
ENRICHMENT_SCHEMA = _load_dep("enrichment").ENRICHMENT_SCHEMA
FILE_SCHEMA = _load_dep("file").FILE_SCHEMA
FINGERPRINT_SCHEMA = _load_dep("fingerprint").FINGERPRINT_SCHEMA
JA4_FINGERPRINT_SCHEMA = _load_dep("ja4_fingerprint").JA4_FINGERPRINT_SCHEMA
KEYBOARD_INFO_SCHEMA = _load_dep("keyboard_info").KEYBOARD_INFO_SCHEMA
METADATA_SCHEMA = _load_dep("metadata").METADATA_SCHEMA
NETWORK_CONNECTION_INFO_SCHEMA = _load_dep(
    "network_connection_info"
).NETWORK_CONNECTION_INFO_SCHEMA
NETWORK_ENDPOINT_SCHEMA = _load_dep("network_endpoint").NETWORK_ENDPOINT_SCHEMA
NETWORK_PROXY_SCHEMA = _load_dep("network_proxy").NETWORK_PROXY_SCHEMA
NETWORK_TRAFFIC_SCHEMA = _load_dep("network_traffic").NETWORK_TRAFFIC_SCHEMA
OBJECT_SCHEMA = _load_dep("object").OBJECT_SCHEMA
OBSERVABLE_SCHEMA = _load_dep("observable").OBSERVABLE_SCHEMA
REQUEST_SCHEMA = _load_dep("request").REQUEST_SCHEMA
RESPONSE_SCHEMA = _load_dep("response").RESPONSE_SCHEMA
TLS_SCHEMA = _load_dep("tls").TLS_SCHEMA
USER_SCHEMA = _load_dep("user").USER_SCHEMA


def get_rdp_activity_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF class 'rdp_activity'."""
    return pa.schema(
        [
            pa.field("activity_id", pa.int32(), nullable=False),
            pa.field("activity_name", pa.string(), nullable=True),
            pa.field("app_name", pa.string(), nullable=True),
            pa.field("capabilities", pa.list_(pa.string()), nullable=True),
            pa.field("category_name", pa.string(), nullable=True),
            pa.field("category_uid", pa.int32(), nullable=False),
            pa.field("certificate_chain", pa.list_(pa.string()), nullable=True),
            pa.field("class_name", pa.string(), nullable=True),
            pa.field("class_uid", pa.int32(), nullable=False),
            pa.field(
                "connection_info",
                pa.struct(list(NETWORK_CONNECTION_INFO_SCHEMA)),
                nullable=True,
            ),
            pa.field("count", pa.int32(), nullable=True),
            pa.field(
                "cumulative_traffic",
                pa.struct(list(NETWORK_TRAFFIC_SCHEMA)),
                nullable=True,
            ),
            pa.field(
                "dst_endpoint", pa.struct(list(NETWORK_ENDPOINT_SCHEMA)), nullable=True
            ),
            pa.field("duration", pa.int64(), nullable=True),
            pa.field("end_time", pa.int64(), nullable=True),
            pa.field("end_time_dt", pa.string(), nullable=True),
            pa.field(
                "enrichments",
                pa.list_(pa.struct(list(ENRICHMENT_SCHEMA))),
                nullable=True,
            ),
            pa.field("file", pa.struct(list(FILE_SCHEMA)), nullable=True),
            pa.field("identifier_cookie", pa.string(), nullable=True),
            pa.field(
                "ja4_fingerprint_list",
                pa.list_(pa.struct(list(JA4_FINGERPRINT_SCHEMA))),
                nullable=True,
            ),
            pa.field(
                "keyboard_info", pa.struct(list(KEYBOARD_INFO_SCHEMA)), nullable=True
            ),
            pa.field("message", pa.string(), nullable=True),
            pa.field("metadata", pa.struct(list(METADATA_SCHEMA)), nullable=False),
            pa.field(
                "observables",
                pa.list_(pa.struct(list(OBSERVABLE_SCHEMA))),
                nullable=True,
            ),
            pa.field("observation_point", pa.string(), nullable=True),
            pa.field("observation_point_id", pa.int32(), nullable=True),
            pa.field("protocol_ver", pa.string(), nullable=True),
            pa.field("proxy", pa.struct(list(NETWORK_PROXY_SCHEMA)), nullable=True),
            pa.field("raw_data", pa.string(), nullable=True),
            pa.field(
                "raw_data_hash", pa.struct(list(FINGERPRINT_SCHEMA)), nullable=True
            ),
            pa.field("raw_data_size", pa.int64(), nullable=True),
            pa.field("remote_display", pa.struct(list(DISPLAY_SCHEMA)), nullable=True),
            pa.field("request", pa.struct(list(REQUEST_SCHEMA)), nullable=True),
            pa.field("response", pa.struct(list(RESPONSE_SCHEMA)), nullable=True),
            pa.field("severity", pa.string(), nullable=True),
            pa.field("severity_id", pa.int32(), nullable=False),
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
            pa.field("tls", pa.struct(list(TLS_SCHEMA)), nullable=True),
            pa.field("traffic", pa.struct(list(NETWORK_TRAFFIC_SCHEMA)), nullable=True),
            pa.field("type_name", pa.string(), nullable=True),
            pa.field("type_uid", pa.int64(), nullable=False),
            pa.field("unmapped", pa.struct(list(OBJECT_SCHEMA)), nullable=True),
            pa.field("user", pa.struct(list(USER_SCHEMA)), nullable=True),
        ]
    )


RDP_ACTIVITY_SCHEMA = get_rdp_activity_schema()
