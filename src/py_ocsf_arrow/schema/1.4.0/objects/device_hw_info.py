"""Auto-generated Arrow schema for OCSF object 'device_hw_info'.

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


DISPLAY_SCHEMA = _load_dep("display").DISPLAY_SCHEMA
KEYBOARD_INFO_SCHEMA = _load_dep("keyboard_info").KEYBOARD_INFO_SCHEMA


def get_device_hw_info_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'device_hw_info'."""
    return pa.schema(
        [
            pa.field("bios_date", pa.string(), nullable=True),
            pa.field("bios_manufacturer", pa.string(), nullable=True),
            pa.field("bios_ver", pa.string(), nullable=True),
            pa.field("chassis", pa.string(), nullable=True),
            pa.field("cpu_architecture", pa.string(), nullable=True),
            pa.field("cpu_architecture_id", pa.int32(), nullable=True),
            pa.field("cpu_bits", pa.int32(), nullable=True),
            pa.field("cpu_cores", pa.int32(), nullable=True),
            pa.field("cpu_count", pa.int32(), nullable=True),
            pa.field("cpu_speed", pa.int32(), nullable=True),
            pa.field("cpu_type", pa.string(), nullable=True),
            pa.field("desktop_display", pa.struct(list(DISPLAY_SCHEMA)), nullable=True),
            pa.field(
                "keyboard_info", pa.struct(list(KEYBOARD_INFO_SCHEMA)), nullable=True
            ),
            pa.field("ram_size", pa.int32(), nullable=True),
            pa.field("serial_number", pa.string(), nullable=True),
            pa.field("uuid", pa.string(), nullable=True),
            pa.field("vendor_name", pa.string(), nullable=True),
        ]
    )


DEVICE_HW_INFO_SCHEMA = get_device_hw_info_schema()
