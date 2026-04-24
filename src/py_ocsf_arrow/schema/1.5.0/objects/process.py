"""Auto-generated Arrow schema for OCSF object 'process'.

Generated from version 1.5.0 at 2026-04-24T03:47:41+00:00.
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


ENVIRONMENT_VARIABLE_SCHEMA = _load_dep(
    "environment_variable"
).ENVIRONMENT_VARIABLE_SCHEMA
FILE_SCHEMA = _load_dep("file").FILE_SCHEMA
OBJECT_SCHEMA = _load_dep("object").OBJECT_SCHEMA
PROCESS_ENTITY_SCHEMA = _load_dep("process_entity").PROCESS_ENTITY_SCHEMA
SESSION_SCHEMA = _load_dep("session").SESSION_SCHEMA
USER_SCHEMA = _load_dep("user").USER_SCHEMA


def get_process_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'process'."""
    return pa.schema(
        [
            pa.field(
                "ancestry",
                pa.list_(pa.struct(list(PROCESS_ENTITY_SCHEMA))),
                nullable=True,
            ),
            pa.field("cmd_line", pa.string(), nullable=True),
            pa.field("cpid", pa.string(), nullable=True),
            pa.field("created_time", pa.int64(), nullable=True),
            pa.field("created_time_dt", pa.string(), nullable=True),
            pa.field(
                "environment_variables",
                pa.list_(pa.struct(list(ENVIRONMENT_VARIABLE_SCHEMA))),
                nullable=True,
            ),
            pa.field("file", pa.struct(list(FILE_SCHEMA)), nullable=True),
            pa.field("integrity", pa.string(), nullable=True),
            pa.field("integrity_id", pa.int32(), nullable=True),
            pa.field("lineage", pa.list_(pa.string()), nullable=True),
            pa.field("loaded_modules", pa.list_(pa.string()), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("parent_process", pa.string(), nullable=True),
            pa.field("path", pa.string(), nullable=True),
            pa.field("pid", pa.int32(), nullable=True),
            pa.field("sandbox", pa.string(), nullable=True),
            pa.field("session", pa.struct(list(SESSION_SCHEMA)), nullable=True),
            pa.field("terminated_time", pa.int64(), nullable=True),
            pa.field("terminated_time_dt", pa.string(), nullable=True),
            pa.field("tid", pa.int32(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("user", pa.struct(list(USER_SCHEMA)), nullable=True),
            pa.field("working_directory", pa.string(), nullable=True),
            pa.field("xattributes", pa.struct(list(OBJECT_SCHEMA)), nullable=True),
        ]
    )


PROCESS_SCHEMA = get_process_schema()
