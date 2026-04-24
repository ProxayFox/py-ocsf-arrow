"""Auto-generated Arrow schema for OCSF object 'query_info'.

Generated from version 1.4.0 at 2026-04-24T03:47:41+00:00.
"""

import pyarrow as pa


def get_query_info_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'query_info'."""
    return pa.schema(
        [
            pa.field("bytes", pa.int64(), nullable=True),
            pa.field("data", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("query_string", pa.string(), nullable=False),
            pa.field("query_time", pa.int64(), nullable=True),
            pa.field("query_time_dt", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
        ]
    )


QUERY_INFO_SCHEMA = get_query_info_schema()
