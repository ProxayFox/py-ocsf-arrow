"""Auto-generated Arrow schema for OCSF object 'autonomous_system'.

OCSF version 1.2.0.
"""

import pyarrow as pa


def get_autonomous_system_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'autonomous_system'."""
    return pa.schema(
        [
            pa.field("name", pa.string(), nullable=True),
            pa.field("number", pa.int32(), nullable=True),
        ]
    )


AUTONOMOUS_SYSTEM_SCHEMA = get_autonomous_system_schema()
