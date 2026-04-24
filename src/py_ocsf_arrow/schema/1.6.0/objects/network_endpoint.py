"""Auto-generated Arrow schema for OCSF object 'network_endpoint'.

Generated from version 1.6.0 at 2026-04-24T03:47:41+00:00.
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


AGENT_SCHEMA = _load_dep("agent").AGENT_SCHEMA
AUTONOMOUS_SYSTEM_SCHEMA = _load_dep("autonomous_system").AUTONOMOUS_SYSTEM_SCHEMA
DEVICE_HW_INFO_SCHEMA = _load_dep("device_hw_info").DEVICE_HW_INFO_SCHEMA
LOCATION_SCHEMA = _load_dep("location").LOCATION_SCHEMA
OS_SCHEMA = _load_dep("os").OS_SCHEMA
USER_SCHEMA = _load_dep("user").USER_SCHEMA


def get_network_endpoint_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'network_endpoint'."""
    return pa.schema(
        [
            pa.field(
                "agent_list", pa.list_(pa.struct(list(AGENT_SCHEMA))), nullable=True
            ),
            pa.field(
                "autonomous_system",
                pa.struct(list(AUTONOMOUS_SYSTEM_SCHEMA)),
                nullable=True,
            ),
            pa.field("domain", pa.string(), nullable=True),
            pa.field("hostname", pa.string(), nullable=True),
            pa.field("hw_info", pa.struct(list(DEVICE_HW_INFO_SCHEMA)), nullable=True),
            pa.field("instance_uid", pa.string(), nullable=True),
            pa.field("interface_name", pa.string(), nullable=True),
            pa.field("interface_uid", pa.string(), nullable=True),
            pa.field("intermediate_ips", pa.list_(pa.string()), nullable=True),
            pa.field("ip", pa.string(), nullable=True),
            pa.field("isp", pa.string(), nullable=True),
            pa.field("isp_org", pa.string(), nullable=True),
            pa.field("location", pa.struct(list(LOCATION_SCHEMA)), nullable=True),
            pa.field("mac", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("os", pa.struct(list(OS_SCHEMA)), nullable=True),
            pa.field("owner", pa.struct(list(USER_SCHEMA)), nullable=True),
            pa.field("port", pa.int32(), nullable=True),
            pa.field("subnet_uid", pa.string(), nullable=True),
            pa.field("svc_name", pa.string(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("type_id", pa.int32(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("vlan_uid", pa.string(), nullable=True),
            pa.field("vpc_uid", pa.string(), nullable=True),
            pa.field("zone", pa.string(), nullable=True),
        ]
    )


NETWORK_ENDPOINT_SCHEMA = get_network_endpoint_schema()
