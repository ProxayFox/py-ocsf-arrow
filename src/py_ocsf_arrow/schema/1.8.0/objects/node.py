"""Auto-generated Arrow schema for OCSF object 'node'.

Generated from version 1.8.0 at 2026-04-24T03:47:42+00:00.
"""

import pyarrow as pa


def get_node_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'node'."""
    return pa.schema(
        [
            pa.field("data", pa.string(), nullable=True),
            pa.field("desc", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=False),
        ]
    )


NODE_SCHEMA = get_node_schema()
