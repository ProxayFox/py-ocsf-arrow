"""Auto-generated Arrow schema for OCSF object 'scan'.

OCSF version 1.5.0.
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
