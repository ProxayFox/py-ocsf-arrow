"""Auto-generated Arrow schema for OCSF object 'service'.

Generated from version 1.0.0 at 2026-04-24T03:47:40+00:00.
"""

import pyarrow as pa


def get_service_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'service'."""
    return pa.schema(
        [
            pa.field("labels", pa.list_(pa.string()), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("version", pa.string(), nullable=True),
        ]
    )


SERVICE_SCHEMA = get_service_schema()
