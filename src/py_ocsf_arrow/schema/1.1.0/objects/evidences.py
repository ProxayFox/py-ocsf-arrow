"""Auto-generated Arrow schema for OCSF object 'evidences'.

OCSF version 1.1.0.
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


ACTOR_SCHEMA = _load_dep("actor").ACTOR_SCHEMA
API_SCHEMA = _load_dep("api").API_SCHEMA
DNS_QUERY_SCHEMA = _load_dep("dns_query").DNS_QUERY_SCHEMA
FILE_SCHEMA = _load_dep("file").FILE_SCHEMA
NETWORK_CONNECTION_INFO_SCHEMA = _load_dep(
    "network_connection_info"
).NETWORK_CONNECTION_INFO_SCHEMA
NETWORK_ENDPOINT_SCHEMA = _load_dep("network_endpoint").NETWORK_ENDPOINT_SCHEMA
PROCESS_SCHEMA = _load_dep("process").PROCESS_SCHEMA


def get_evidences_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'evidences'."""
    return pa.schema(
        [
            pa.field("actor", pa.struct(list(ACTOR_SCHEMA)), nullable=True),
            pa.field("api", pa.struct(list(API_SCHEMA)), nullable=True),
            pa.field(
                "connection_info",
                pa.struct(list(NETWORK_CONNECTION_INFO_SCHEMA)),
                nullable=True,
            ),
            pa.field("data", pa.string(), nullable=True),
            pa.field(
                "dst_endpoint",
                pa.struct(list(NETWORK_ENDPOINT_SCHEMA)),
                nullable=True,
            ),
            pa.field("file", pa.struct(list(FILE_SCHEMA)), nullable=True),
            pa.field("process", pa.struct(list(PROCESS_SCHEMA)), nullable=True),
            pa.field("query", pa.struct(list(DNS_QUERY_SCHEMA)), nullable=True),
            pa.field(
                "src_endpoint",
                pa.struct(list(NETWORK_ENDPOINT_SCHEMA)),
                nullable=True,
            ),
        ]
    )


EVIDENCES_SCHEMA = get_evidences_schema()
