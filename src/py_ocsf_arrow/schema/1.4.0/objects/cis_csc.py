"""Auto-generated Arrow schema for OCSF object 'cis_csc'.

OCSF version 1.4.0.
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
