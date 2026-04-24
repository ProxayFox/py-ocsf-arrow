"""Auto-generated Arrow schema for OCSF object 'tls_extension'.

Generated from version 1.2.0 at 2026-04-24T03:47:40+00:00.
"""

import pyarrow as pa


def get_tls_extension_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'tls_extension'."""
    return pa.schema(
        [
            pa.field("data", pa.string(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("type_id", pa.int32(), nullable=False),
        ]
    )


TLS_EXTENSION_SCHEMA = get_tls_extension_schema()
