"""Auto-generated Arrow schema for OCSF object 'http_cookie'.

OCSF version 1.1.0.
"""

import pyarrow as pa


def get_http_cookie_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'http_cookie'."""
    return pa.schema(
        [
            pa.field("domain", pa.string(), nullable=True),
            pa.field("expiration_time", pa.int64(), nullable=True),
            pa.field("expiration_time_dt", pa.string(), nullable=True),
            pa.field("http_only", pa.bool8(), nullable=True),
            pa.field("is_http_only", pa.bool8(), nullable=True),
            pa.field("is_secure", pa.bool8(), nullable=True),
            pa.field("name", pa.string(), nullable=False),
            pa.field("path", pa.string(), nullable=True),
            pa.field("samesite", pa.string(), nullable=True),
            pa.field("secure", pa.bool8(), nullable=True),
            pa.field("value", pa.string(), nullable=False),
        ]
    )


HTTP_COOKIE_SCHEMA = get_http_cookie_schema()
