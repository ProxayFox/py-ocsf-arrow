"""Auto-generated Arrow schema for OCSF object 'service_privilege_analysis'.

OCSF version 1.8.0.
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


PRIVILEGE_ATTACK_INFO_SCHEMA = _load_dep(
    "privilege_attack_info"
).PRIVILEGE_ATTACK_INFO_SCHEMA


def get_service_privilege_analysis_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'service_privilege_analysis'."""
    return pa.schema(
        [
            pa.field("all_privileges_unused", pa.bool8(), nullable=True),
            pa.field("analyzed_privileges_count", pa.int32(), nullable=True),
            pa.field("execute_count", pa.int32(), nullable=True),
            pa.field("last_used_time", pa.int64(), nullable=True),
            pa.field("last_used_time_dt", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=False),
            pa.field(
                "privilege_attack_info_list",
                pa.list_(pa.struct(list(PRIVILEGE_ATTACK_INFO_SCHEMA))),
                nullable=True,
            ),
            pa.field("read_count", pa.int32(), nullable=True),
            pa.field("unused_privileges_count", pa.int32(), nullable=True),
            pa.field("write_count", pa.int32(), nullable=True),
        ]
    )


SERVICE_PRIVILEGE_ANALYSIS_SCHEMA = get_service_privilege_analysis_schema()
