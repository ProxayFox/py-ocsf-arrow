"""Auto-generated Arrow schema for OCSF object 'session'.

OCSF version 1.2.0.
"""

import pyarrow as pa


def get_session_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'session'."""
    return pa.schema(
        [
            pa.field("count", pa.int32(), nullable=True),
            pa.field("created_time", pa.int64(), nullable=True),
            pa.field("created_time_dt", pa.string(), nullable=True),
            pa.field("credential_uid", pa.string(), nullable=True),
            pa.field("expiration_reason", pa.string(), nullable=True),
            pa.field("expiration_time", pa.int64(), nullable=True),
            pa.field("expiration_time_dt", pa.string(), nullable=True),
            pa.field("is_mfa", pa.bool8(), nullable=True),
            pa.field("is_remote", pa.bool8(), nullable=True),
            pa.field("is_vpn", pa.bool8(), nullable=True),
            pa.field("issuer", pa.string(), nullable=True),
            pa.field("terminal", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("uid_alt", pa.string(), nullable=True),
            pa.field("uuid", pa.string(), nullable=True),
        ]
    )


SESSION_SCHEMA = get_session_schema()
