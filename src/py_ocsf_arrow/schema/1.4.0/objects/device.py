"""Auto-generated Arrow schema for OCSF object 'device'.

Generated from version 1.4.0 at 2026-04-24T03:47:41+00:00.
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
DEVICE_HW_INFO_SCHEMA = _load_dep("device_hw_info").DEVICE_HW_INFO_SCHEMA
GROUP_SCHEMA = _load_dep("group").GROUP_SCHEMA
IMAGE_SCHEMA = _load_dep("image").IMAGE_SCHEMA
LOCATION_SCHEMA = _load_dep("location").LOCATION_SCHEMA
NETWORK_INTERFACE_SCHEMA = _load_dep("network_interface").NETWORK_INTERFACE_SCHEMA
ORGANIZATION_SCHEMA = _load_dep("organization").ORGANIZATION_SCHEMA
OS_SCHEMA = _load_dep("os").OS_SCHEMA
USER_SCHEMA = _load_dep("user").USER_SCHEMA


def get_device_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'device'."""
    return pa.schema(
        [
            pa.field(
                "agent_list", pa.list_(pa.struct(list(AGENT_SCHEMA))), nullable=True
            ),
            pa.field("autoscale_uid", pa.string(), nullable=True),
            pa.field("boot_time", pa.int64(), nullable=True),
            pa.field("boot_time_dt", pa.string(), nullable=True),
            pa.field("created_time", pa.int64(), nullable=True),
            pa.field("created_time_dt", pa.string(), nullable=True),
            pa.field("desc", pa.string(), nullable=True),
            pa.field("domain", pa.string(), nullable=True),
            pa.field("first_seen_time", pa.int64(), nullable=True),
            pa.field("first_seen_time_dt", pa.string(), nullable=True),
            pa.field("groups", pa.list_(pa.struct(list(GROUP_SCHEMA))), nullable=True),
            pa.field("hostname", pa.string(), nullable=True),
            pa.field("hw_info", pa.struct(list(DEVICE_HW_INFO_SCHEMA)), nullable=True),
            pa.field("hypervisor", pa.string(), nullable=True),
            pa.field("image", pa.struct(list(IMAGE_SCHEMA)), nullable=True),
            pa.field("imei", pa.string(), nullable=True),
            pa.field("imei_list", pa.list_(pa.string()), nullable=True),
            pa.field("instance_uid", pa.string(), nullable=True),
            pa.field("interface_name", pa.string(), nullable=True),
            pa.field("interface_uid", pa.string(), nullable=True),
            pa.field("ip", pa.string(), nullable=True),
            pa.field("is_compliant", pa.bool8(), nullable=True),
            pa.field("is_managed", pa.bool8(), nullable=True),
            pa.field("is_personal", pa.bool8(), nullable=True),
            pa.field("is_trusted", pa.bool8(), nullable=True),
            pa.field("last_seen_time", pa.int64(), nullable=True),
            pa.field("last_seen_time_dt", pa.string(), nullable=True),
            pa.field("location", pa.struct(list(LOCATION_SCHEMA)), nullable=True),
            pa.field("mac", pa.string(), nullable=True),
            pa.field("model", pa.string(), nullable=True),
            pa.field("modified_time", pa.int64(), nullable=True),
            pa.field("modified_time_dt", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field(
                "network_interfaces",
                pa.list_(pa.struct(list(NETWORK_INTERFACE_SCHEMA))),
                nullable=True,
            ),
            pa.field("org", pa.struct(list(ORGANIZATION_SCHEMA)), nullable=True),
            pa.field("os", pa.struct(list(OS_SCHEMA)), nullable=True),
            pa.field("os_machine_uuid", pa.string(), nullable=True),
            pa.field("owner", pa.struct(list(USER_SCHEMA)), nullable=True),
            pa.field("region", pa.string(), nullable=True),
            pa.field("subnet", pa.string(), nullable=True),
            pa.field("subnet_uid", pa.string(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("type_id", pa.int32(), nullable=False),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("uid_alt", pa.string(), nullable=True),
            pa.field("vendor_name", pa.string(), nullable=True),
            pa.field("vlan_uid", pa.string(), nullable=True),
            pa.field("vpc_uid", pa.string(), nullable=True),
            pa.field("zone", pa.string(), nullable=True),
        ]
    )


DEVICE_SCHEMA = get_device_schema()
