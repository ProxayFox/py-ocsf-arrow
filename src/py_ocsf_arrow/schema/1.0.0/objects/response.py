"""Auto-generated Arrow schema for OCSF object 'response'.

Generated from version 1.0.0 at 2026-04-24T03:47:40+00:00.
"""

import pyarrow as pa


def get_response_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'response'."""
    return pa.schema(
        [
            pa.field("code", pa.int32(), nullable=True),
            pa.field("error", pa.string(), nullable=True),
            pa.field("error_message", pa.string(), nullable=True),
            pa.field("flags", pa.list_(pa.string()), nullable=True),
            pa.field("message", pa.string(), nullable=True),
        ]
    )


RESPONSE_SCHEMA = get_response_schema()
