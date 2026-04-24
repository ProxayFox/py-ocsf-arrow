"""Auto-generated Arrow schema for OCSF object 'trait'.

Generated from version 1.8.0 at 2026-04-24T03:47:42+00:00.
"""

import pyarrow as pa


def get_trait_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'trait'."""
    return pa.schema(
        [
            pa.field("category", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("values", pa.list_(pa.string()), nullable=True),
        ]
    )


TRAIT_SCHEMA = get_trait_schema()
