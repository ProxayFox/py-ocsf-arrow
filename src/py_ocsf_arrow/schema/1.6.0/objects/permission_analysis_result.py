"""Auto-generated Arrow schema for OCSF object 'permission_analysis_result'.

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


KEY_VALUE_OBJECT_SCHEMA = _load_dep("key_value_object").KEY_VALUE_OBJECT_SCHEMA


def get_permission_analysis_result_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'permission_analysis_result'."""
    return pa.schema(
        [
            pa.field(
                "condition_keys",
                pa.list_(pa.struct(list(KEY_VALUE_OBJECT_SCHEMA))),
                nullable=True,
            ),
            pa.field("granted_privileges", pa.list_(pa.string()), nullable=True),
            pa.field("unused_privileges_count", pa.int32(), nullable=True),
            pa.field("unused_services_count", pa.int32(), nullable=True),
        ]
    )


PERMISSION_ANALYSIS_RESULT_SCHEMA = get_permission_analysis_result_schema()
