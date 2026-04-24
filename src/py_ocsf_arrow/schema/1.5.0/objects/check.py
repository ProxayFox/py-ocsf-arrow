"""Auto-generated Arrow schema for OCSF object 'check'.

Generated from version 1.5.0 at 2026-04-24T03:47:41+00:00.
"""

import pyarrow as pa


def get_check_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'check'."""
    return pa.schema(
        [
            pa.field("desc", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("severity", pa.string(), nullable=True),
            pa.field("severity_id", pa.int32(), nullable=True),
            pa.field("standards", pa.list_(pa.string()), nullable=True),
            pa.field("status", pa.string(), nullable=True),
            pa.field("status_id", pa.int32(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("version", pa.string(), nullable=True),
        ]
    )


CHECK_SCHEMA = get_check_schema()
