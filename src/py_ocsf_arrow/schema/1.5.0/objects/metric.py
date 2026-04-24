"""Auto-generated Arrow schema for OCSF object 'metric'.

Generated from version 1.5.0 at 2026-04-24T03:47:41+00:00.
"""

import pyarrow as pa


def get_metric_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'metric'."""
    return pa.schema(
        [
            pa.field("name", pa.string(), nullable=False),
            pa.field("value", pa.string(), nullable=False),
        ]
    )


METRIC_SCHEMA = get_metric_schema()
