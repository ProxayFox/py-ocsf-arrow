"""Auto-generated Arrow schema for OCSF object 'auth_factor'.

Generated from version 1.4.0 at 2026-04-24T03:47:41+00:00.
"""

import pyarrow as pa


def get_auth_factor_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'auth_factor'."""
    return pa.schema(
        [
            pa.field("email_addr", pa.string(), nullable=True),
            pa.field("factor_type", pa.string(), nullable=True),
            pa.field("factor_type_id", pa.int32(), nullable=False),
            pa.field("is_hotp", pa.bool8(), nullable=True),
            pa.field("is_totp", pa.bool8(), nullable=True),
            pa.field("phone_number", pa.string(), nullable=True),
            pa.field("provider", pa.string(), nullable=True),
            pa.field("security_questions", pa.list_(pa.string()), nullable=True),
        ]
    )


AUTH_FACTOR_SCHEMA = get_auth_factor_schema()
