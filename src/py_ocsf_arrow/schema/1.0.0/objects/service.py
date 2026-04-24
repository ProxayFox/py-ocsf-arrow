"""Auto-generated Arrow schema for OCSF object 'service'.

OCSF version 1.0.0.
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
