"""Auto-generated Arrow schema for OCSF object 'organization'.

OCSF version 1.6.0.
"""

import pyarrow as pa


def get_organization_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'organization'."""
    return pa.schema(
        [
            pa.field("name", pa.string(), nullable=True),
            pa.field("ou_name", pa.string(), nullable=True),
            pa.field("ou_uid", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
        ]
    )


ORGANIZATION_SCHEMA = get_organization_schema()
