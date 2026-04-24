"""Auto-generated Arrow schema for OCSF object 'encryption_details'.

Generated from version 1.5.0 at 2026-04-24T03:47:41+00:00.
"""

import pyarrow as pa


def get_encryption_details_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'encryption_details'."""
    return pa.schema(
        [
            pa.field("algorithm", pa.string(), nullable=True),
            pa.field("algorithm_id", pa.int32(), nullable=True),
            pa.field("key_length", pa.int32(), nullable=True),
            pa.field("key_uid", pa.string(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
        ]
    )


ENCRYPTION_DETAILS_SCHEMA = get_encryption_details_schema()
