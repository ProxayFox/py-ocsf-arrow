"""Auto-generated Arrow schema for OCSF object 'long_string'.

OCSF version 1.4.0.
"""

import pyarrow as pa


def get_long_string_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'long_string'."""
    return pa.schema(
        [
            pa.field("is_truncated", pa.bool8(), nullable=True),
            pa.field("untruncated_size", pa.int32(), nullable=True),
            pa.field("value", pa.string(), nullable=False),
        ]
    )


LONG_STRING_SCHEMA = get_long_string_schema()
