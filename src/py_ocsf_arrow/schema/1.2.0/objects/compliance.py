"""Auto-generated Arrow schema for OCSF object 'compliance'.

Generated from version 1.2.0 at 2026-04-24T03:47:40+00:00.
"""

import pyarrow as pa


def get_compliance_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'compliance'."""
    return pa.schema(
        [
            pa.field("control", pa.string(), nullable=True),
            pa.field("requirements", pa.list_(pa.string()), nullable=True),
            pa.field("standards", pa.list_(pa.string()), nullable=False),
            pa.field("status", pa.string(), nullable=True),
            pa.field("status_code", pa.string(), nullable=True),
            pa.field("status_detail", pa.string(), nullable=True),
            pa.field("status_id", pa.int32(), nullable=True),
        ]
    )


COMPLIANCE_SCHEMA = get_compliance_schema()
