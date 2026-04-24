"""Auto-generated Arrow schema for OCSF object 'scan'.

Generated from version 1.3.0 at 2026-04-24T03:47:40+00:00.
"""

import pyarrow as pa


def get_scan_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'scan'."""
    return pa.schema(
        [
            pa.field("name", pa.string(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("type_id", pa.int32(), nullable=False),
            pa.field("uid", pa.string(), nullable=True),
        ]
    )


SCAN_SCHEMA = get_scan_schema()
