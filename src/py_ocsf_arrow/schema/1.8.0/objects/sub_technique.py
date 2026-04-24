"""Auto-generated Arrow schema for OCSF object 'sub_technique'.

Generated from version 1.8.0 at 2026-04-24T03:47:42+00:00.
"""

import pyarrow as pa


def get_sub_technique_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'sub_technique'."""
    return pa.schema(
        [
            pa.field("name", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
        ]
    )


SUB_TECHNIQUE_SCHEMA = get_sub_technique_schema()
