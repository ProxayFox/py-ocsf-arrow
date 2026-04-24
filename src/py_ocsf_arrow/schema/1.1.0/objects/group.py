"""Auto-generated Arrow schema for OCSF object 'group'.

Generated from version 1.1.0 at 2026-04-24T03:47:40+00:00.
"""

import pyarrow as pa


def get_group_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'group'."""
    return pa.schema(
        [
            pa.field("desc", pa.string(), nullable=True),
            pa.field("domain", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("privileges", pa.list_(pa.string()), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
        ]
    )


GROUP_SCHEMA = get_group_schema()
