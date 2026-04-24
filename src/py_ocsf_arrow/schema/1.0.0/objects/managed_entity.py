"""Auto-generated Arrow schema for OCSF object 'managed_entity'.

Generated from version 1.0.0 at 2026-04-24T03:47:40+00:00.
"""

import pyarrow as pa


def get_managed_entity_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'managed_entity'."""
    return pa.schema(
        [
            pa.field("data", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("version", pa.string(), nullable=True),
        ]
    )


MANAGED_ENTITY_SCHEMA = get_managed_entity_schema()
