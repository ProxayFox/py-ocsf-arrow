"""Auto-generated Arrow schema for OCSF object 'technique'.

OCSF version 1.0.0.
"""

import pyarrow as pa


def get_technique_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'technique'."""
    return pa.schema(
        [
            pa.field("name", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
        ]
    )


TECHNIQUE_SCHEMA = get_technique_schema()
