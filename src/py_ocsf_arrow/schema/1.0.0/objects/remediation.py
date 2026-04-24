"""Auto-generated Arrow schema for OCSF object 'remediation'.

OCSF version 1.0.0.
"""

import pyarrow as pa


def get_remediation_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'remediation'."""
    return pa.schema(
        [
            pa.field("desc", pa.string(), nullable=True),
            pa.field("kb_articles", pa.list_(pa.string()), nullable=True),
        ]
    )


REMEDIATION_SCHEMA = get_remediation_schema()
