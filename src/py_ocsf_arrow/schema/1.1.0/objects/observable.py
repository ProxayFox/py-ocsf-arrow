"""Auto-generated Arrow schema for OCSF object 'observable'.

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


REPUTATION_SCHEMA = _load_dep("reputation").REPUTATION_SCHEMA


def get_observable_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'observable'."""
    return pa.schema(
        [
            pa.field("name", pa.string(), nullable=False),
            pa.field("reputation", pa.struct(list(REPUTATION_SCHEMA)), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("type_id", pa.int32(), nullable=False),
            pa.field("value", pa.string(), nullable=True),
        ]
    )


OBSERVABLE_SCHEMA = get_observable_schema()
