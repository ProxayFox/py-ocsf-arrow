"""Auto-generated Arrow schema for OCSF object 'aircraft'.

OCSF version 1.5.0.
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


LOCATION_SCHEMA = _load_dep("location").LOCATION_SCHEMA


def get_aircraft_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'aircraft'."""
    return pa.schema(
        [
            pa.field("location", pa.struct(list(LOCATION_SCHEMA)), nullable=True),
            pa.field("model", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("serial_number", pa.string(), nullable=True),
            pa.field("speed", pa.string(), nullable=True),
            pa.field("speed_accuracy", pa.string(), nullable=True),
            pa.field("track_direction", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("uid_alt", pa.string(), nullable=True),
            pa.field("vertical_speed", pa.string(), nullable=True),
        ]
    )


AIRCRAFT_SCHEMA = get_aircraft_schema()
