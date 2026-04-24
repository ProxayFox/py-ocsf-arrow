"""Auto-generated Arrow schema for OCSF object 'keyboard_info'.

OCSF version 1.8.0.
"""

import pyarrow as pa


def get_keyboard_info_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'keyboard_info'."""
    return pa.schema(
        [
            pa.field("function_keys", pa.int32(), nullable=True),
            pa.field("ime", pa.string(), nullable=True),
            pa.field("keyboard_layout", pa.string(), nullable=True),
            pa.field("keyboard_subtype", pa.int32(), nullable=True),
            pa.field("keyboard_type", pa.string(), nullable=True),
        ]
    )


KEYBOARD_INFO_SCHEMA = get_keyboard_info_schema()
