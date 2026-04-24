"""Auto-generated Arrow schema for OCSF object 'threat_actor'.

OCSF version 1.8.0.
"""

import pyarrow as pa


def get_threat_actor_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'threat_actor'."""
    return pa.schema(
        [
            pa.field("name", pa.string(), nullable=False),
            pa.field("type", pa.string(), nullable=True),
            pa.field("type_id", pa.int32(), nullable=True),
        ]
    )


THREAT_ACTOR_SCHEMA = get_threat_actor_schema()
