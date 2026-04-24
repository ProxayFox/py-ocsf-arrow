"""Auto-generated Arrow schema for OCSF object 'observable'.

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


REPUTATION_SCHEMA = _load_dep("reputation").REPUTATION_SCHEMA


def get_observable_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'observable'."""
    return pa.schema(
        [
            pa.field("event_uid", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("reputation", pa.struct(list(REPUTATION_SCHEMA)), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("type_id", pa.int32(), nullable=False),
            pa.field("type_uid", pa.int64(), nullable=True),
            pa.field("value", pa.string(), nullable=True),
        ]
    )


OBSERVABLE_SCHEMA = get_observable_schema()
