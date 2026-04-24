"""Auto-generated Arrow schema for OCSF object 'fingerprint'.

OCSF version 1.0.0.
"""

import pyarrow as pa


def get_fingerprint_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'fingerprint'."""
    return pa.schema(
        [
            pa.field("algorithm", pa.string(), nullable=True),
            pa.field("algorithm_id", pa.int32(), nullable=False),
            pa.field("value", pa.string(), nullable=False),
        ]
    )


FINGERPRINT_SCHEMA = get_fingerprint_schema()
