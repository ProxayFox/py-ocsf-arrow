"""Auto-generated Arrow schema for OCSF object 'cis_control'.

OCSF version 1.7.0.
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
