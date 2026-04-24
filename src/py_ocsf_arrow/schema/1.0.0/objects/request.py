"""Auto-generated Arrow schema for OCSF object 'request'.

Generated from version 1.0.0 at 2026-04-24T03:47:40+00:00.
"""

import pyarrow as pa


def get_request_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'request'."""
    return pa.schema(
        [
            pa.field("flags", pa.list_(pa.string()), nullable=True),
            pa.field("uid", pa.string(), nullable=False),
        ]
    )


REQUEST_SCHEMA = get_request_schema()
