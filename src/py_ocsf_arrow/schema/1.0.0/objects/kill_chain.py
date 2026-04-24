"""Auto-generated Arrow schema for OCSF object 'kill_chain'.

Generated from version 1.0.0 at 2026-04-24T03:47:40+00:00.
"""

import pyarrow as pa


def get_kill_chain_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'kill_chain'."""
    return pa.schema(
        [
            pa.field("phase", pa.string(), nullable=True),
            pa.field("phase_id", pa.int32(), nullable=False),
        ]
    )


KILL_CHAIN_SCHEMA = get_kill_chain_schema()
