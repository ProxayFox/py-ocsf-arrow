"""Auto-generated Arrow schema for OCSF object 'ja4_fingerprint'.

Generated from version 1.5.0 at 2026-04-24T03:47:41+00:00.
"""

import pyarrow as pa


def get_ja4_fingerprint_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'ja4_fingerprint'."""
    return pa.schema(
        [
            pa.field("section_a", pa.string(), nullable=True),
            pa.field("section_b", pa.string(), nullable=True),
            pa.field("section_c", pa.string(), nullable=True),
            pa.field("section_d", pa.string(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("type_id", pa.int32(), nullable=False),
            pa.field("value", pa.string(), nullable=False),
        ]
    )


JA4_FINGERPRINT_SCHEMA = get_ja4_fingerprint_schema()
