"""Auto-generated Arrow schema for OCSF object 'san'.

Generated from version 1.1.0 at 2026-04-24T03:47:40+00:00.
"""

import pyarrow as pa


def get_san_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'san'."""
    return pa.schema(
        [
            pa.field("name", pa.string(), nullable=False),
            pa.field("type", pa.string(), nullable=False),
        ]
    )


SAN_SCHEMA = get_san_schema()
