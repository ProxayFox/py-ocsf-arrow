"""Auto-generated Arrow schema for OCSF object 'observation'.

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


TIMESPAN_SCHEMA = _load_dep("timespan").TIMESPAN_SCHEMA


def get_observation_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'observation'."""
    return pa.schema(
        [
            pa.field("count", pa.int32(), nullable=True),
            pa.field("timespan", pa.struct(list(TIMESPAN_SCHEMA)), nullable=True),
            pa.field("value", pa.string(), nullable=False),
        ]
    )


OBSERVATION_SCHEMA = get_observation_schema()
