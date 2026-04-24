"""Auto-generated Arrow schema for OCSF object 'campaign'.

Generated from version 1.6.0 at 2026-04-24T03:47:41+00:00.
"""

import pyarrow as pa


def get_campaign_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'campaign'."""
    return pa.schema(
        [
            pa.field("name", pa.string(), nullable=False),
        ]
    )


CAMPAIGN_SCHEMA = get_campaign_schema()
