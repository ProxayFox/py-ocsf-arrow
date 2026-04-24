"""Auto-generated Arrow schema for OCSF object 'image'.

OCSF version 1.2.0.
"""

import pyarrow as pa


def get_image_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'image'."""
    return pa.schema(
        [
            pa.field("labels", pa.list_(pa.string()), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("path", pa.string(), nullable=True),
            pa.field("tag", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=False),
        ]
    )


IMAGE_SCHEMA = get_image_schema()
