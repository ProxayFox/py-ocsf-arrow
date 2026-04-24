"""Auto-generated Arrow schema for OCSF object 'cis_control'.

Generated from version 1.6.0 at 2026-04-24T03:47:41+00:00.
"""

import pyarrow as pa


def get_cis_control_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'cis_control'."""
    return pa.schema(
        [
            pa.field("desc", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=False),
            pa.field("version", pa.string(), nullable=True),
        ]
    )


CIS_CONTROL_SCHEMA = get_cis_control_schema()
