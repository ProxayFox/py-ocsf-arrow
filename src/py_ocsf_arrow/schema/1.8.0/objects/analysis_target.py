"""Auto-generated Arrow schema for OCSF object 'analysis_target'.

OCSF version 1.8.0.
"""

import pyarrow as pa


def get_analysis_target_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'analysis_target'."""
    return pa.schema(
        [
            pa.field("name", pa.string(), nullable=False),
            pa.field("type", pa.string(), nullable=True),
        ]
    )


ANALYSIS_TARGET_SCHEMA = get_analysis_target_schema()
