"""Auto-generated Arrow schema for OCSF object 'span'.

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


SERVICE_SCHEMA = _load_dep("service").SERVICE_SCHEMA


def get_span_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'span'."""
    return pa.schema(
        [
            pa.field("duration", pa.int64(), nullable=True),
            pa.field("end_time", pa.int64(), nullable=False),
            pa.field("end_time_dt", pa.string(), nullable=True),
            pa.field("message", pa.string(), nullable=True),
            pa.field("operation", pa.string(), nullable=True),
            pa.field("parent_uid", pa.string(), nullable=True),
            pa.field("service", pa.struct(list(SERVICE_SCHEMA)), nullable=True),
            pa.field("start_time", pa.int64(), nullable=False),
            pa.field("start_time_dt", pa.string(), nullable=True),
            pa.field("status_code", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=False),
        ]
    )


SPAN_SCHEMA = get_span_schema()
