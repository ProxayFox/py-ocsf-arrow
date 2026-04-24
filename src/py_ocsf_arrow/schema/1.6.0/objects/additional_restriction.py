"""Auto-generated Arrow schema for OCSF object 'additional_restriction'.

Generated from version 1.6.0 at 2026-04-24T03:47:41+00:00.
"""

import pyarrow as pa


def get_additional_restriction_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'additional_restriction'."""
    return pa.schema(
        [
            pa.field("status", pa.string(), nullable=True),
            pa.field("status_id", pa.int32(), nullable=True),
        ]
    )


ADDITIONAL_RESTRICTION_SCHEMA = get_additional_restriction_schema()
