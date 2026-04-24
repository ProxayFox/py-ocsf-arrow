"""Auto-generated Arrow schema for OCSF object 'security_state'.

Generated from version 1.8.0 at 2026-04-24T03:47:42+00:00.
"""

import pyarrow as pa


def get_security_state_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'security_state'."""
    return pa.schema(
        [
            pa.field("state", pa.string(), nullable=True),
            pa.field("state_id", pa.int32(), nullable=True),
        ]
    )


SECURITY_STATE_SCHEMA = get_security_state_schema()
