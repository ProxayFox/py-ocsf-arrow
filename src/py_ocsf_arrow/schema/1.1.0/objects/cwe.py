"""Auto-generated Arrow schema for OCSF object 'cwe'.

OCSF version 1.1.0.
"""

import pyarrow as pa


def get_cwe_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'cwe'."""
    return pa.schema(
        [
            pa.field("caption", pa.string(), nullable=True),
            pa.field("src_url", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=False),
        ]
    )


CWE_SCHEMA = get_cwe_schema()
