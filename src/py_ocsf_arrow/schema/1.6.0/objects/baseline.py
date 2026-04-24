"""Auto-generated Arrow schema for OCSF object 'baseline'.

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


OBSERVATION_SCHEMA = _load_dep("observation").OBSERVATION_SCHEMA


def get_baseline_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'baseline'."""
    return pa.schema(
        [
            pa.field("observation_parameter", pa.string(), nullable=False),
            pa.field("observation_type", pa.string(), nullable=True),
            pa.field(
                "observations",
                pa.list_(pa.struct(list(OBSERVATION_SCHEMA))),
                nullable=False,
            ),
            pa.field("observed_pattern", pa.string(), nullable=True),
        ]
    )


BASELINE_SCHEMA = get_baseline_schema()
