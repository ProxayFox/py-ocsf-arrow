"""Auto-generated Arrow schema for OCSF object 'web_resource'.

OCSF version 1.1.0.
"""

import pyarrow as pa


def get_web_resource_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'web_resource'."""
    return pa.schema(
        [
            pa.field("data", pa.string(), nullable=True),
            pa.field("desc", pa.string(), nullable=True),
            pa.field("labels", pa.list_(pa.string()), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("url_string", pa.string(), nullable=True),
        ]
    )


WEB_RESOURCE_SCHEMA = get_web_resource_schema()
