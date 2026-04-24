"""Auto-generated Arrow schema for OCSF object 'job'.

OCSF version 1.4.0.
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


FILE_SCHEMA = _load_dep("file").FILE_SCHEMA
USER_SCHEMA = _load_dep("user").USER_SCHEMA


def get_job_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'job'."""
    return pa.schema(
        [
            pa.field("cmd_line", pa.string(), nullable=True),
            pa.field("created_time", pa.int64(), nullable=True),
            pa.field("created_time_dt", pa.string(), nullable=True),
            pa.field("desc", pa.string(), nullable=True),
            pa.field("file", pa.struct(list(FILE_SCHEMA)), nullable=False),
            pa.field("last_run_time", pa.int64(), nullable=True),
            pa.field("last_run_time_dt", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=False),
            pa.field("next_run_time", pa.int64(), nullable=True),
            pa.field("next_run_time_dt", pa.string(), nullable=True),
            pa.field("run_state", pa.string(), nullable=True),
            pa.field("run_state_id", pa.int32(), nullable=True),
            pa.field("user", pa.struct(list(USER_SCHEMA)), nullable=True),
        ]
    )


JOB_SCHEMA = get_job_schema()
