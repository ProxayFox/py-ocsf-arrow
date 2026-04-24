"""Auto-generated Arrow schema for OCSF object 'unmanned_aerial_system'.

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


DEVICE_HW_INFO_SCHEMA = _load_dep("device_hw_info").DEVICE_HW_INFO_SCHEMA
LOCATION_SCHEMA = _load_dep("location").LOCATION_SCHEMA


def get_unmanned_aerial_system_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'unmanned_aerial_system'."""
    return pa.schema(
        [
            pa.field("hw_info", pa.struct(list(DEVICE_HW_INFO_SCHEMA)), nullable=True),
            pa.field("location", pa.struct(list(LOCATION_SCHEMA)), nullable=True),
            pa.field("model", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("serial_number", pa.string(), nullable=True),
            pa.field("speed", pa.string(), nullable=True),
            pa.field("speed_accuracy", pa.string(), nullable=True),
            pa.field("track_direction", pa.string(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("type_id", pa.int32(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("uid_alt", pa.string(), nullable=True),
            pa.field("uuid", pa.string(), nullable=True),
            pa.field("vertical_speed", pa.string(), nullable=True),
        ]
    )


UNMANNED_AERIAL_SYSTEM_SCHEMA = get_unmanned_aerial_system_schema()
