"""Auto-generated Arrow schema for OCSF object 'kill_chain_phase'.

OCSF version 1.5.0.
"""

import pyarrow as pa


def get_kill_chain_phase_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'kill_chain_phase'."""
    return pa.schema(
        [
            pa.field("phase", pa.string(), nullable=True),
            pa.field("phase_id", pa.int32(), nullable=False),
        ]
    )


KILL_CHAIN_PHASE_SCHEMA = get_kill_chain_phase_schema()
