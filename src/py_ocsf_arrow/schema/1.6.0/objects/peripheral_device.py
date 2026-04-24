"""Auto-generated Arrow schema for OCSF object 'peripheral_device'.

Generated from version 1.6.0 at 2026-04-24T03:47:41+00:00.
"""

import pyarrow as pa


def get_peripheral_device_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'peripheral_device'."""
    return pa.schema(
        [
            pa.field("class", pa.string(), nullable=False),
            pa.field("model", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=False),
            pa.field("serial_number", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("vendor_name", pa.string(), nullable=True),
        ]
    )


PERIPHERAL_DEVICE_SCHEMA = get_peripheral_device_schema()
