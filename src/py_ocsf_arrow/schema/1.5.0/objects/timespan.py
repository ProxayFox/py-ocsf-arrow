"""Auto-generated Arrow schema for OCSF object 'timespan'.

OCSF version 1.5.0.
"""

import pyarrow as pa


def get_timespan_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'timespan'."""
    return pa.schema(
        [
            pa.field("duration", pa.int64(), nullable=True),
            pa.field("duration_days", pa.int32(), nullable=True),
            pa.field("duration_hours", pa.int32(), nullable=True),
            pa.field("duration_mins", pa.int32(), nullable=True),
            pa.field("duration_months", pa.int32(), nullable=True),
            pa.field("duration_secs", pa.int32(), nullable=True),
            pa.field("duration_weeks", pa.int32(), nullable=True),
            pa.field("duration_years", pa.int32(), nullable=True),
            pa.field("end_time", pa.int64(), nullable=True),
            pa.field("end_time_dt", pa.string(), nullable=True),
            pa.field("start_time", pa.int64(), nullable=True),
            pa.field("start_time_dt", pa.string(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("type_id", pa.int32(), nullable=True),
        ]
    )


TIMESPAN_SCHEMA = get_timespan_schema()
