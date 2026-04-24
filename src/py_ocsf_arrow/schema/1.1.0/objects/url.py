"""Auto-generated Arrow schema for OCSF object 'url'.

OCSF version 1.1.0.
"""

import pyarrow as pa


def get_url_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'url'."""
    return pa.schema(
        [
            pa.field("categories", pa.list_(pa.string()), nullable=True),
            pa.field("category_ids", pa.list_(pa.int32()), nullable=True),
            pa.field("hostname", pa.string(), nullable=True),
            pa.field("path", pa.string(), nullable=True),
            pa.field("port", pa.int32(), nullable=True),
            pa.field("query_string", pa.string(), nullable=True),
            pa.field("resource_type", pa.string(), nullable=True),
            pa.field("scheme", pa.string(), nullable=True),
            pa.field("subdomain", pa.string(), nullable=True),
            pa.field("url_string", pa.string(), nullable=True),
        ]
    )


URL_SCHEMA = get_url_schema()
