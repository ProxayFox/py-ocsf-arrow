"""Auto-generated Arrow schema for OCSF object 'token'.

OCSF version 1.8.0.
"""

import pyarrow as pa


def get_token_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'token'."""
    return pa.schema(
        [
            pa.field("created_time", pa.int64(), nullable=True),
            pa.field("created_time_dt", pa.string(), nullable=True),
            pa.field("expiration_time", pa.int64(), nullable=True),
            pa.field("expiration_time_dt", pa.string(), nullable=True),
            pa.field("is_renewable", pa.bool8(), nullable=True),
            pa.field("modified_time", pa.int64(), nullable=True),
            pa.field("modified_time_dt", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("tenant_uid", pa.string(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("type_id", pa.int32(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("zone", pa.string(), nullable=True),
        ]
    )


TOKEN_SCHEMA = get_token_schema()
