"""Auto-generated Arrow schema for OCSF object 'compliance'.

OCSF version 1.0.0.
"""

import pyarrow as pa


def get_compliance_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'compliance'."""
    return pa.schema(
        [
            pa.field("requirements", pa.list_(pa.string()), nullable=True),
            pa.field("status", pa.string(), nullable=True),
            pa.field("status_detail", pa.string(), nullable=True),
        ]
    )


COMPLIANCE_SCHEMA = get_compliance_schema()
