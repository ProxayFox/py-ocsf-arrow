"""Auto-generated Arrow schema for OCSF object 'policy'.

Generated from version 1.4.0 at 2026-04-24T03:47:41+00:00.
"""

import pyarrow as pa


def get_policy_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'policy'."""
    return pa.schema(
        [
            pa.field("desc", pa.string(), nullable=True),
            pa.field("is_applied", pa.bool8(), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("version", pa.string(), nullable=True),
        ]
    )


POLICY_SCHEMA = get_policy_schema()
