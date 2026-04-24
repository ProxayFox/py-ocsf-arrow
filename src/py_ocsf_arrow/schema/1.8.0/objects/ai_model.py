"""Auto-generated Arrow schema for OCSF object 'ai_model'.

OCSF version 1.8.0.
"""

import pyarrow as pa


def get_ai_model_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'ai_model'."""
    return pa.schema(
        [
            pa.field("ai_provider", pa.string(), nullable=False),
            pa.field("name", pa.string(), nullable=False),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("version", pa.string(), nullable=True),
        ]
    )


AI_MODEL_SCHEMA = get_ai_model_schema()
