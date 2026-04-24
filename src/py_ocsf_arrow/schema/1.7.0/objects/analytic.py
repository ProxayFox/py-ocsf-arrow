"""Auto-generated Arrow schema for OCSF object 'analytic'.

OCSF version 1.7.0.
"""

import pyarrow as pa


def get_analytic_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'analytic'."""
    return pa.schema(
        [
            pa.field("algorithm", pa.string(), nullable=True),
            pa.field("category", pa.string(), nullable=True),
            pa.field("desc", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("related_analytics", pa.list_(pa.string()), nullable=True),
            pa.field("state", pa.string(), nullable=True),
            pa.field("state_id", pa.int32(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("type_id", pa.int32(), nullable=False),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("version", pa.string(), nullable=True),
        ]
    )


ANALYTIC_SCHEMA = get_analytic_schema()
