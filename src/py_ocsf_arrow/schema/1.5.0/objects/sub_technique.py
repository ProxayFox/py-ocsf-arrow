"""Auto-generated Arrow schema for OCSF object 'sub_technique'.

OCSF version 1.5.0.
"""

import pyarrow as pa


def get_sub_technique_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'sub_technique'."""
    return pa.schema(
        [
            pa.field("name", pa.string(), nullable=True),
            pa.field("src_url", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
        ]
    )


SUB_TECHNIQUE_SCHEMA = get_sub_technique_schema()
