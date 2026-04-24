"""Auto-generated Arrow schema for OCSF object 'fingerprint'.

Generated from version 1.2.0 at 2026-04-24T03:47:40+00:00.
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
