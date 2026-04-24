"""Auto-generated Arrow schema for OCSF object 'san'.

OCSF version 1.5.0.
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
