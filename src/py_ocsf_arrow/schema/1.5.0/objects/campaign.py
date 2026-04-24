"""Auto-generated Arrow schema for OCSF object 'campaign'.

OCSF version 1.5.0.
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
