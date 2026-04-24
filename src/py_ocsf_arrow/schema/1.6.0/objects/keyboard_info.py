"""Auto-generated Arrow schema for OCSF object 'keyboard_info'.

Generated from version 1.6.0 at 2026-04-24T03:47:41+00:00.
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
