"""Auto-generated Arrow schema for OCSF object 'cwe'.

Generated from version 1.2.0 at 2026-04-24T03:47:40+00:00.
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
