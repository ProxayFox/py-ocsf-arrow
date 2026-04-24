"""Auto-generated Arrow schema for OCSF object 'ticket'.

Generated from version 1.5.0 at 2026-04-24T03:47:41+00:00.
"""

import pyarrow as pa


def get_ticket_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'ticket'."""
    return pa.schema(
        [
            pa.field("status", pa.string(), nullable=True),
            pa.field("status_details", pa.list_(pa.string()), nullable=True),
            pa.field("status_id", pa.int32(), nullable=True),
            pa.field("title", pa.string(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("type_id", pa.int32(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
        ]
    )


TICKET_SCHEMA = get_ticket_schema()
