"""Auto-generated Arrow schema for OCSF object 'email'.

OCSF version 1.0.0.
"""

import pyarrow as pa


def get_email_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'email'."""
    return pa.schema(
        [
            pa.field("cc", pa.list_(pa.string()), nullable=True),
            pa.field("delivered_to", pa.string(), nullable=True),
            pa.field("from", pa.string(), nullable=False),
            pa.field("message_uid", pa.string(), nullable=True),
            pa.field("raw_header", pa.string(), nullable=True),
            pa.field("reply_to", pa.string(), nullable=True),
            pa.field("size", pa.int64(), nullable=True),
            pa.field("smtp_from", pa.string(), nullable=True),
            pa.field("smtp_to", pa.list_(pa.string()), nullable=True),
            pa.field("subject", pa.string(), nullable=True),
            pa.field("to", pa.list_(pa.string()), nullable=False),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("x_originating_ip", pa.list_(pa.string()), nullable=True),
        ]
    )


EMAIL_SCHEMA = get_email_schema()
