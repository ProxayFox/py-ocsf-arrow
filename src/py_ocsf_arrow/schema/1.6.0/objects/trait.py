"""Auto-generated Arrow schema for OCSF object 'trait'.

OCSF version 1.6.0.
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
