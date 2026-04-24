"""Auto-generated Arrow schema for OCSF object 'network_connection_info'.

Generated from version 1.3.0 at 2026-04-24T03:47:40+00:00.
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


SESSION_SCHEMA = _load_dep("session").SESSION_SCHEMA


def get_network_connection_info_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'network_connection_info'."""
    return pa.schema(
        [
            pa.field("boundary", pa.string(), nullable=True),
            pa.field("boundary_id", pa.int32(), nullable=True),
            pa.field("direction", pa.string(), nullable=True),
            pa.field("direction_id", pa.int32(), nullable=False),
            pa.field("protocol_name", pa.string(), nullable=True),
            pa.field("protocol_num", pa.int32(), nullable=True),
            pa.field("protocol_ver", pa.string(), nullable=True),
            pa.field("protocol_ver_id", pa.int32(), nullable=True),
            pa.field("session", pa.struct(list(SESSION_SCHEMA)), nullable=True),
            pa.field("tcp_flags", pa.int32(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
        ]
    )


NETWORK_CONNECTION_INFO_SCHEMA = get_network_connection_info_schema()
