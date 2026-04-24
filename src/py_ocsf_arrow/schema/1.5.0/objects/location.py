"""Auto-generated Arrow schema for OCSF object 'location'.

OCSF version 1.5.0.
"""

import pyarrow as pa


def get_location_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'location'."""
    return pa.schema(
        [
            pa.field("aerial_height", pa.string(), nullable=True),
            pa.field("city", pa.string(), nullable=True),
            pa.field("continent", pa.string(), nullable=True),
            pa.field("coordinates", pa.list_(pa.float32()), nullable=True),
            pa.field("country", pa.string(), nullable=True),
            pa.field("desc", pa.string(), nullable=True),
            pa.field("geodetic_altitude", pa.string(), nullable=True),
            pa.field("geodetic_vertical_accuracy", pa.string(), nullable=True),
            pa.field("geohash", pa.string(), nullable=True),
            pa.field("horizontal_accuracy", pa.string(), nullable=True),
            pa.field("is_on_premises", pa.bool8(), nullable=True),
            pa.field("isp", pa.string(), nullable=True),
            pa.field("lat", pa.float32(), nullable=True),
            pa.field("long", pa.float32(), nullable=True),
            pa.field("postal_code", pa.string(), nullable=True),
            pa.field("pressure_altitude", pa.string(), nullable=True),
            pa.field("provider", pa.string(), nullable=True),
            pa.field("region", pa.string(), nullable=True),
        ]
    )


LOCATION_SCHEMA = get_location_schema()
