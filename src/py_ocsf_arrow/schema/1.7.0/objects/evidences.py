"""Auto-generated Arrow schema for OCSF object 'evidences'.

Generated from version 1.7.0 at 2026-04-24T03:47:42+00:00.
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


DATABASE_SCHEMA = _load_dep("database").DATABASE_SCHEMA
DATABUCKET_SCHEMA = _load_dep("databucket").DATABUCKET_SCHEMA
DNS_QUERY_SCHEMA = _load_dep("dns_query").DNS_QUERY_SCHEMA
EMAIL_SCHEMA = _load_dep("email").EMAIL_SCHEMA
FILE_SCHEMA = _load_dep("file").FILE_SCHEMA
HTTP_REQUEST_SCHEMA = _load_dep("http_request").HTTP_REQUEST_SCHEMA
HTTP_RESPONSE_SCHEMA = _load_dep("http_response").HTTP_RESPONSE_SCHEMA
JA4_FINGERPRINT_SCHEMA = _load_dep("ja4_fingerprint").JA4_FINGERPRINT_SCHEMA
JOB_SCHEMA = _load_dep("job").JOB_SCHEMA
NETWORK_CONNECTION_INFO_SCHEMA = _load_dep(
    "network_connection_info"
).NETWORK_CONNECTION_INFO_SCHEMA
NETWORK_ENDPOINT_SCHEMA = _load_dep("network_endpoint").NETWORK_ENDPOINT_SCHEMA
PROCESS_SCHEMA = _load_dep("process").PROCESS_SCHEMA
RESOURCE_DETAILS_SCHEMA = _load_dep("resource_details").RESOURCE_DETAILS_SCHEMA
SCRIPT_SCHEMA = _load_dep("script").SCRIPT_SCHEMA
TLS_SCHEMA = _load_dep("tls").TLS_SCHEMA
URL_SCHEMA = _load_dep("url").URL_SCHEMA
USER_SCHEMA = _load_dep("user").USER_SCHEMA


def get_evidences_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'evidences'."""
    return pa.schema(
        [
            pa.field(
                "connection_info",
                pa.struct(list(NETWORK_CONNECTION_INFO_SCHEMA)),
                nullable=True,
            ),
            pa.field("data", pa.string(), nullable=True),
            pa.field("database", pa.struct(list(DATABASE_SCHEMA)), nullable=True),
            pa.field("databucket", pa.struct(list(DATABUCKET_SCHEMA)), nullable=True),
            pa.field(
                "dst_endpoint", pa.struct(list(NETWORK_ENDPOINT_SCHEMA)), nullable=True
            ),
            pa.field("email", pa.struct(list(EMAIL_SCHEMA)), nullable=True),
            pa.field("file", pa.struct(list(FILE_SCHEMA)), nullable=True),
            pa.field(
                "http_request", pa.struct(list(HTTP_REQUEST_SCHEMA)), nullable=True
            ),
            pa.field(
                "http_response", pa.struct(list(HTTP_RESPONSE_SCHEMA)), nullable=True
            ),
            pa.field(
                "ja4_fingerprint_list",
                pa.list_(pa.struct(list(JA4_FINGERPRINT_SCHEMA))),
                nullable=True,
            ),
            pa.field("job", pa.struct(list(JOB_SCHEMA)), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("process", pa.struct(list(PROCESS_SCHEMA)), nullable=True),
            pa.field("query", pa.struct(list(DNS_QUERY_SCHEMA)), nullable=True),
            pa.field("reg_key", pa.string(), nullable=True),
            pa.field("reg_value", pa.string(), nullable=True),
            pa.field(
                "resources",
                pa.list_(pa.struct(list(RESOURCE_DETAILS_SCHEMA))),
                nullable=True,
            ),
            pa.field("script", pa.struct(list(SCRIPT_SCHEMA)), nullable=True),
            pa.field(
                "src_endpoint", pa.struct(list(NETWORK_ENDPOINT_SCHEMA)), nullable=True
            ),
            pa.field("tls", pa.struct(list(TLS_SCHEMA)), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("url", pa.struct(list(URL_SCHEMA)), nullable=True),
            pa.field("user", pa.struct(list(USER_SCHEMA)), nullable=True),
            pa.field("win_service", pa.string(), nullable=True),
        ]
    )


EVIDENCES_SCHEMA = get_evidences_schema()
