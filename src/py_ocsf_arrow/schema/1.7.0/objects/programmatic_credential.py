"""Auto-generated Arrow schema for OCSF object 'programmatic_credential'.

OCSF version 1.7.0.
"""

import pyarrow as pa


def get_programmatic_credential_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'programmatic_credential'."""
    return pa.schema(
        [
            pa.field("last_used_time", pa.int64(), nullable=True),
            pa.field("last_used_time_dt", pa.string(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=False),
        ]
    )


PROGRAMMATIC_CREDENTIAL_SCHEMA = get_programmatic_credential_schema()
