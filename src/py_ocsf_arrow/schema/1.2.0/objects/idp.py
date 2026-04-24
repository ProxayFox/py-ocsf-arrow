"""Auto-generated Arrow schema for OCSF object 'idp'.

Generated from version 1.2.0 at 2026-04-24T03:47:40+00:00.
"""

import pyarrow as pa


def get_idp_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'idp'."""
    return pa.schema(
        [
            pa.field("name", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
        ]
    )


IDP_SCHEMA = get_idp_schema()
