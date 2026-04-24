"""Auto-generated Arrow schema for OCSF object 'discovery_details'.

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


OCCURRENCE_DETAILS_SCHEMA = _load_dep("occurrence_details").OCCURRENCE_DETAILS_SCHEMA


def get_discovery_details_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'discovery_details'."""
    return pa.schema(
        [
            pa.field("count", pa.int32(), nullable=True),
            pa.field(
                "occurrence_details",
                pa.struct(list(OCCURRENCE_DETAILS_SCHEMA)),
                nullable=True,
            ),
            pa.field(
                "occurrences",
                pa.list_(pa.struct(list(OCCURRENCE_DETAILS_SCHEMA))),
                nullable=True,
            ),
            pa.field("type", pa.string(), nullable=True),
            pa.field("value", pa.string(), nullable=True),
        ]
    )


DISCOVERY_DETAILS_SCHEMA = get_discovery_details_schema()
