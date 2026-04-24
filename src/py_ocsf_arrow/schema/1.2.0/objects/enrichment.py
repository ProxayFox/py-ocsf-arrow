"""Auto-generated Arrow schema for OCSF object 'enrichment'.

Generated from version 1.2.0 at 2026-04-24T03:47:40+00:00.
"""

import pyarrow as pa


def get_enrichment_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'enrichment'."""
    return pa.schema(
        [
            pa.field("data", pa.string(), nullable=False),
            pa.field("name", pa.string(), nullable=False),
            pa.field("provider", pa.string(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("value", pa.string(), nullable=False),
        ]
    )


ENRICHMENT_SCHEMA = get_enrichment_schema()
