"""Auto-generated Arrow schema for OCSF object 'edge'.

Generated from version 1.8.0 at 2026-04-24T03:47:42+00:00.
"""

import pyarrow as pa


def get_edge_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'edge'."""
    return pa.schema(
        [
            pa.field("data", pa.string(), nullable=True),
            pa.field("is_directed", pa.bool8(), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("relation", pa.string(), nullable=True),
            pa.field("source", pa.string(), nullable=False),
            pa.field("target", pa.string(), nullable=False),
            pa.field("uid", pa.string(), nullable=True),
        ]
    )


EDGE_SCHEMA = get_edge_schema()
