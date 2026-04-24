"""Auto-generated Arrow schema for OCSF object 'related_event'.

Generated from version 1.0.0 at 2026-04-24T03:47:40+00:00.
"""

import pyarrow as pa


def get_related_event_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'related_event'."""
    return pa.schema(
        [
            pa.field("product_uid", pa.string(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("type_uid", pa.int32(), nullable=True),
            pa.field("uid", pa.string(), nullable=False),
        ]
    )


RELATED_EVENT_SCHEMA = get_related_event_schema()
