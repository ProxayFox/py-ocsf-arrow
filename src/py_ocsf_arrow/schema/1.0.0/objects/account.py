"""Auto-generated Arrow schema for OCSF object 'account'.

OCSF version 1.0.0.
"""

import pyarrow as pa


def get_account_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'account'."""
    return pa.schema(
        [
            pa.field("name", pa.string(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("type_id", pa.int32(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
        ]
    )


ACCOUNT_SCHEMA = get_account_schema()
