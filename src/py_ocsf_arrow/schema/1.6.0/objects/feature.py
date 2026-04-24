"""Auto-generated Arrow schema for OCSF object 'feature'.

Generated from version 1.6.0 at 2026-04-24T03:47:41+00:00.
"""

import pyarrow as pa


def get_feature_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'feature'."""
    return pa.schema(
        [
            pa.field("name", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("version", pa.string(), nullable=True),
        ]
    )


FEATURE_SCHEMA = get_feature_schema()
