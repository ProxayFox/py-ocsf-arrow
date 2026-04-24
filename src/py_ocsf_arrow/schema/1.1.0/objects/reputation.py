"""Auto-generated Arrow schema for OCSF object 'reputation'.

OCSF version 1.1.0.
"""

import pyarrow as pa


def get_reputation_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'reputation'."""
    return pa.schema(
        [
            pa.field("base_score", pa.float32(), nullable=False),
            pa.field("provider", pa.string(), nullable=True),
            pa.field("score", pa.string(), nullable=True),
            pa.field("score_id", pa.int32(), nullable=False),
        ]
    )


REPUTATION_SCHEMA = get_reputation_schema()
