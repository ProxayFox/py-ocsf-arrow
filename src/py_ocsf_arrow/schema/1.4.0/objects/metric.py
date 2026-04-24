"""Auto-generated Arrow schema for OCSF object 'metric'.

OCSF version 1.4.0.
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
