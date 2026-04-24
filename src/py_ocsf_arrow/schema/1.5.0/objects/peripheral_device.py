"""Auto-generated Arrow schema for OCSF object 'peripheral_device'.

OCSF version 1.5.0.
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
