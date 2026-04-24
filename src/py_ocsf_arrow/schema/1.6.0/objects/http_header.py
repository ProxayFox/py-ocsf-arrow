"""Auto-generated Arrow schema for OCSF object 'http_header'.

Generated from version 1.6.0 at 2026-04-24T03:47:41+00:00.
"""

import pyarrow as pa


def get_http_header_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'http_header'."""
    return pa.schema(
        [
            pa.field("name", pa.string(), nullable=False),
            pa.field("value", pa.string(), nullable=False),
        ]
    )


HTTP_HEADER_SCHEMA = get_http_header_schema()
