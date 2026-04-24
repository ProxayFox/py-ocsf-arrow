"""Auto-generated Arrow schema for OCSF object 'authorization'.

Generated from version 1.6.0 at 2026-04-24T03:47:41+00:00.
"""

import pyarrow as pa


def get_authorization_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'authorization'."""
    return pa.schema(
        [
            pa.field("decision", pa.string(), nullable=True),
        ]
    )


AUTHORIZATION_SCHEMA = get_authorization_schema()
