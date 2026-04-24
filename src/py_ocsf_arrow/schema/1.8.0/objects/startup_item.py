"""Auto-generated Arrow schema for OCSF object 'startup_item'.

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


JOB_SCHEMA = _load_dep("job").JOB_SCHEMA
KERNEL_DRIVER_SCHEMA = _load_dep("kernel_driver").KERNEL_DRIVER_SCHEMA
PROCESS_SCHEMA = _load_dep("process").PROCESS_SCHEMA


def get_startup_item_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'startup_item'."""
    return pa.schema(
        [
            pa.field("driver", pa.struct(list(KERNEL_DRIVER_SCHEMA)), nullable=True),
            pa.field("job", pa.struct(list(JOB_SCHEMA)), nullable=True),
            pa.field("name", pa.string(), nullable=False),
            pa.field("process", pa.struct(list(PROCESS_SCHEMA)), nullable=True),
            pa.field("run_mode_ids", pa.list_(pa.int32()), nullable=True),
            pa.field("run_modes", pa.list_(pa.string()), nullable=True),
            pa.field("run_state", pa.string(), nullable=True),
            pa.field("run_state_id", pa.int32(), nullable=True),
            pa.field("start_type", pa.string(), nullable=True),
            pa.field("start_type_id", pa.int32(), nullable=False),
            pa.field("type", pa.string(), nullable=True),
            pa.field("type_id", pa.int32(), nullable=True),
            pa.field("win_service", pa.string(), nullable=True),
        ]
    )


STARTUP_ITEM_SCHEMA = get_startup_item_schema()
