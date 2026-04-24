"""Auto-generated Arrow schema for OCSF object 'process'.

OCSF version 1.1.0.
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


CONTAINER_SCHEMA = _load_dep("container").CONTAINER_SCHEMA
FILE_SCHEMA = _load_dep("file").FILE_SCHEMA
GROUP_SCHEMA = _load_dep("group").GROUP_SCHEMA
OBJECT_SCHEMA = _load_dep("object").OBJECT_SCHEMA
SESSION_SCHEMA = _load_dep("session").SESSION_SCHEMA
USER_SCHEMA = _load_dep("user").USER_SCHEMA


def get_process_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'process'."""
    return pa.schema(
        [
            pa.field("auid", pa.int32(), nullable=True),
            pa.field("cmd_line", pa.string(), nullable=True),
            pa.field("container", pa.struct(list(CONTAINER_SCHEMA)), nullable=True),
            pa.field("created_time", pa.int64(), nullable=True),
            pa.field("created_time_dt", pa.string(), nullable=True),
            pa.field("egid", pa.int32(), nullable=True),
            pa.field("euid", pa.int32(), nullable=True),
            pa.field("file", pa.struct(list(FILE_SCHEMA)), nullable=True),
            pa.field("group", pa.struct(list(GROUP_SCHEMA)), nullable=True),
            pa.field("integrity", pa.string(), nullable=True),
            pa.field("integrity_id", pa.int32(), nullable=True),
            pa.field("lineage", pa.list_(pa.string()), nullable=True),
            pa.field("loaded_modules", pa.list_(pa.string()), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("namespace_pid", pa.int32(), nullable=True),
            pa.field("parent_process", pa.string(), nullable=True),
            pa.field("pid", pa.int32(), nullable=True),
            pa.field("sandbox", pa.string(), nullable=True),
            pa.field("session", pa.struct(list(SESSION_SCHEMA)), nullable=True),
            pa.field("terminated_time", pa.int64(), nullable=True),
            pa.field("terminated_time_dt", pa.string(), nullable=True),
            pa.field("tid", pa.int32(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("user", pa.struct(list(USER_SCHEMA)), nullable=True),
            pa.field("xattributes", pa.struct(list(OBJECT_SCHEMA)), nullable=True),
        ]
    )


PROCESS_SCHEMA = get_process_schema()
