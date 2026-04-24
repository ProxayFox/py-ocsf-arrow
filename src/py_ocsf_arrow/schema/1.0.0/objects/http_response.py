"""Auto-generated Arrow schema for OCSF object 'http_response'.

Generated from version 1.0.0 at 2026-04-24T03:47:40+00:00.
"""

import pyarrow as pa


def get_http_response_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'http_response'."""
    return pa.schema(
        [
            pa.field("code", pa.int32(), nullable=False),
            pa.field("content_type", pa.string(), nullable=True),
            pa.field("latency", pa.int32(), nullable=True),
            pa.field("length", pa.int32(), nullable=True),
            pa.field("message", pa.string(), nullable=True),
            pa.field("status", pa.string(), nullable=True),
        ]
    )


HTTP_RESPONSE_SCHEMA = get_http_response_schema()
