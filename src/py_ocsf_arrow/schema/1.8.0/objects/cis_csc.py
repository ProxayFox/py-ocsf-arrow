"""Auto-generated Arrow schema for OCSF object 'cis_csc'.

Generated from version 1.8.0 at 2026-04-24T03:47:42+00:00.
"""

import pyarrow as pa


def get_cis_csc_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'cis_csc'."""
    return pa.schema(
        [
            pa.field("control", pa.string(), nullable=False),
            pa.field("version", pa.string(), nullable=True),
        ]
    )


CIS_CSC_SCHEMA = get_cis_csc_schema()
