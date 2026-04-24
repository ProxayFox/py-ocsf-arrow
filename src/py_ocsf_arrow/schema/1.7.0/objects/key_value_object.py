"""Auto-generated Arrow schema for OCSF object 'key_value_object'.

OCSF version 1.7.0.
"""

import pyarrow as pa


def get_key_value_object_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'key_value_object'."""
    return pa.schema(
        [
            pa.field("name", pa.string(), nullable=False),
            pa.field("value", pa.string(), nullable=True),
            pa.field("values", pa.list_(pa.string()), nullable=True),
        ]
    )


KEY_VALUE_OBJECT_SCHEMA = get_key_value_object_schema()
