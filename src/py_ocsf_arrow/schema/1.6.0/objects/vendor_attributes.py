"""Auto-generated Arrow schema for OCSF object 'vendor_attributes'.

OCSF version 1.6.0.
"""

import pyarrow as pa


def get_vendor_attributes_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'vendor_attributes'."""
    return pa.schema(
        [
            pa.field("severity", pa.string(), nullable=True),
            pa.field("severity_id", pa.int32(), nullable=True),
        ]
    )


VENDOR_ATTRIBUTES_SCHEMA = get_vendor_attributes_schema()
