"""Auto-generated Arrow schema for OCSF object 'assessment'.

Generated from version 1.7.0 at 2026-04-24T03:47:42+00:00.
"""

import pyarrow as pa


def get_assessment_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'assessment'."""
    return pa.schema(
        [
            pa.field("category", pa.string(), nullable=True),
            pa.field("desc", pa.string(), nullable=True),
            pa.field("meets_criteria", pa.bool8(), nullable=False),
            pa.field("name", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
        ]
    )


ASSESSMENT_SCHEMA = get_assessment_schema()
