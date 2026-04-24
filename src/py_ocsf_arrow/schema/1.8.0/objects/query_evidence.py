"""Auto-generated Arrow schema for OCSF object 'query_evidence'.

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


FILE_SCHEMA = _load_dep("file").FILE_SCHEMA
JOB_SCHEMA = _load_dep("job").JOB_SCHEMA
KERNEL_SCHEMA = _load_dep("kernel").KERNEL_SCHEMA
MODULE_SCHEMA = _load_dep("module").MODULE_SCHEMA
NETWORK_CONNECTION_INFO_SCHEMA = _load_dep(
    "network_connection_info"
).NETWORK_CONNECTION_INFO_SCHEMA
NETWORK_INTERFACE_SCHEMA = _load_dep("network_interface").NETWORK_INTERFACE_SCHEMA
PERIPHERAL_DEVICE_SCHEMA = _load_dep("peripheral_device").PERIPHERAL_DEVICE_SCHEMA
PROCESS_SCHEMA = _load_dep("process").PROCESS_SCHEMA
SERVICE_SCHEMA = _load_dep("service").SERVICE_SCHEMA
SESSION_SCHEMA = _load_dep("session").SESSION_SCHEMA
STARTUP_ITEM_SCHEMA = _load_dep("startup_item").STARTUP_ITEM_SCHEMA
USER_SCHEMA = _load_dep("user").USER_SCHEMA


def get_query_evidence_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'query_evidence'."""
    return pa.schema(
        [
            pa.field(
                "connection_info",
                pa.struct(list(NETWORK_CONNECTION_INFO_SCHEMA)),
                nullable=True,
            ),
            pa.field("file", pa.struct(list(FILE_SCHEMA)), nullable=True),
            pa.field("folder", pa.struct(list(FILE_SCHEMA)), nullable=True),
            pa.field("job", pa.struct(list(JOB_SCHEMA)), nullable=True),
            pa.field("kernel", pa.struct(list(KERNEL_SCHEMA)), nullable=True),
            pa.field("module", pa.struct(list(MODULE_SCHEMA)), nullable=True),
            pa.field(
                "network_interfaces",
                pa.list_(pa.struct(list(NETWORK_INTERFACE_SCHEMA))),
                nullable=True,
            ),
            pa.field(
                "peripheral_device",
                pa.struct(list(PERIPHERAL_DEVICE_SCHEMA)),
                nullable=True,
            ),
            pa.field("process", pa.struct(list(PROCESS_SCHEMA)), nullable=True),
            pa.field("query_type", pa.string(), nullable=True),
            pa.field("query_type_id", pa.int32(), nullable=False),
            pa.field("reg_key", pa.string(), nullable=True),
            pa.field("reg_value", pa.string(), nullable=True),
            pa.field("service", pa.struct(list(SERVICE_SCHEMA)), nullable=True),
            pa.field("session", pa.struct(list(SESSION_SCHEMA)), nullable=True),
            pa.field(
                "startup_item", pa.struct(list(STARTUP_ITEM_SCHEMA)), nullable=True
            ),
            pa.field("state", pa.string(), nullable=True),
            pa.field("tcp_state_id", pa.int32(), nullable=True),
            pa.field("user", pa.struct(list(USER_SCHEMA)), nullable=True),
            pa.field("users", pa.list_(pa.struct(list(USER_SCHEMA))), nullable=True),
        ]
    )


QUERY_EVIDENCE_SCHEMA = get_query_evidence_schema()
