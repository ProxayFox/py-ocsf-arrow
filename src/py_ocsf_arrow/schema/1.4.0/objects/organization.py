"""Auto-generated Arrow schema for OCSF object 'organization'.

Generated from version 1.4.0 at 2026-04-24T03:47:41+00:00.
"""

import pyarrow as pa


def get_organization_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'organization'."""
    return pa.schema(
        [
            pa.field("name", pa.string(), nullable=True),
            pa.field("ou_name", pa.string(), nullable=True),
            pa.field("ou_uid", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
        ]
    )


ORGANIZATION_SCHEMA = get_organization_schema()
