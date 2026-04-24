"""Auto-generated Arrow schema for OCSF object 'email_auth'.

Generated from version 1.5.0 at 2026-04-24T03:47:41+00:00.
"""

import pyarrow as pa


def get_email_auth_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'email_auth'."""
    return pa.schema(
        [
            pa.field("dkim", pa.string(), nullable=True),
            pa.field("dkim_domain", pa.string(), nullable=True),
            pa.field("dkim_signature", pa.string(), nullable=True),
            pa.field("dmarc", pa.string(), nullable=True),
            pa.field("dmarc_override", pa.string(), nullable=True),
            pa.field("dmarc_policy", pa.string(), nullable=True),
            pa.field("spf", pa.string(), nullable=True),
        ]
    )


EMAIL_AUTH_SCHEMA = get_email_auth_schema()
