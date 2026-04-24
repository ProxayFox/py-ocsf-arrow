"""Auto-generated Arrow schema for OCSF object 'unmanned_system_operating_area'.

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


LOCATION_SCHEMA = _load_dep("location").LOCATION_SCHEMA


def get_unmanned_system_operating_area_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'unmanned_system_operating_area'."""
    return pa.schema(
        [
            pa.field("aerial_height", pa.string(), nullable=True),
            pa.field("altitude_ceiling", pa.string(), nullable=True),
            pa.field("altitude_floor", pa.string(), nullable=True),
            pa.field("city", pa.string(), nullable=True),
            pa.field("continent", pa.string(), nullable=True),
            pa.field("coordinates", pa.list_(pa.float32()), nullable=True),
            pa.field("count", pa.int32(), nullable=True),
            pa.field("country", pa.string(), nullable=True),
            pa.field("desc", pa.string(), nullable=True),
            pa.field("end_time", pa.int64(), nullable=True),
            pa.field("end_time_dt", pa.string(), nullable=True),
            pa.field("geodetic_altitude", pa.string(), nullable=True),
            pa.field("geodetic_vertical_accuracy", pa.string(), nullable=True),
            pa.field("geohash", pa.string(), nullable=True),
            pa.field("horizontal_accuracy", pa.string(), nullable=True),
            pa.field("is_on_premises", pa.bool8(), nullable=True),
            pa.field("isp", pa.string(), nullable=True),
            pa.field("lat", pa.float32(), nullable=True),
            pa.field(
                "locations",
                pa.list_(pa.struct(list(LOCATION_SCHEMA))),
                nullable=True,
            ),
            pa.field("long", pa.float32(), nullable=True),
            pa.field("postal_code", pa.string(), nullable=True),
            pa.field("pressure_altitude", pa.string(), nullable=True),
            pa.field("provider", pa.string(), nullable=True),
            pa.field("radius", pa.string(), nullable=True),
            pa.field("region", pa.string(), nullable=True),
            pa.field("start_time", pa.int64(), nullable=True),
            pa.field("start_time_dt", pa.string(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("type_id", pa.int32(), nullable=True),
        ]
    )


UNMANNED_SYSTEM_OPERATING_AREA_SCHEMA = get_unmanned_system_operating_area_schema()
