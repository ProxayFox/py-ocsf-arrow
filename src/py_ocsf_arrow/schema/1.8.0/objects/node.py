"""Auto-generated Arrow schema for OCSF object 'node'.

OCSF version 1.8.0.
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
