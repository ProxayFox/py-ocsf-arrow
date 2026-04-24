"""Auto-generated Arrow schema for OCSF object 'access_analysis_result'.

Generated from version 1.7.0 at 2026-04-24T03:47:42+00:00.
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


ADDITIONAL_RESTRICTION_SCHEMA = _load_dep(
    "additional_restriction"
).ADDITIONAL_RESTRICTION_SCHEMA
KEY_VALUE_OBJECT_SCHEMA = _load_dep("key_value_object").KEY_VALUE_OBJECT_SCHEMA
USER_SCHEMA = _load_dep("user").USER_SCHEMA


def get_access_analysis_result_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'access_analysis_result'."""
    return pa.schema(
        [
            pa.field("access_level", pa.string(), nullable=True),
            pa.field("access_type", pa.string(), nullable=True),
            pa.field(
                "accessors", pa.list_(pa.struct(list(USER_SCHEMA))), nullable=False
            ),
            pa.field(
                "additional_restrictions",
                pa.list_(pa.struct(list(ADDITIONAL_RESTRICTION_SCHEMA))),
                nullable=True,
            ),
            pa.field(
                "condition_keys",
                pa.list_(pa.struct(list(KEY_VALUE_OBJECT_SCHEMA))),
                nullable=True,
            ),
            pa.field("granted_privileges", pa.list_(pa.string()), nullable=True),
        ]
    )


ACCESS_ANALYSIS_RESULT_SCHEMA = get_access_analysis_result_schema()
