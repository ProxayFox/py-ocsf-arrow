"""Auto-generated Arrow schema for OCSF object 'peripheral_device'.

Generated from version 1.7.0 at 2026-04-24T03:47:42+00:00.
"""

import pyarrow as pa


def get_peripheral_device_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'peripheral_device'."""
    return pa.schema(
        [
            pa.field("class", pa.string(), nullable=True),
            pa.field("model", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=False),
            pa.field("serial_number", pa.string(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("type_id", pa.int32(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("vendor_id_list", pa.list_(pa.string()), nullable=True),
            pa.field("vendor_name", pa.string(), nullable=True),
        ]
    )


PERIPHERAL_DEVICE_SCHEMA = get_peripheral_device_schema()
