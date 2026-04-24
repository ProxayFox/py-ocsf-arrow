"""Auto-generated Arrow schema for OCSF object 'idp'.

OCSF version 1.1.0.
"""

import pyarrow as pa


def get_idp_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'idp'."""
    return pa.schema(
        [
            pa.field("name", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
        ]
    )


IDP_SCHEMA = get_idp_schema()
