"""Auto-generated Arrow schema for OCSF object 'epss'.

Generated from version 1.7.0 at 2026-04-24T03:47:42+00:00.
"""

import pyarrow as pa


def get_epss_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'epss'."""
    return pa.schema(
        [
            pa.field("created_time", pa.int64(), nullable=True),
            pa.field("created_time_dt", pa.string(), nullable=True),
            pa.field("percentile", pa.float32(), nullable=True),
            pa.field("score", pa.string(), nullable=False),
            pa.field("version", pa.string(), nullable=True),
        ]
    )


EPSS_SCHEMA = get_epss_schema()
