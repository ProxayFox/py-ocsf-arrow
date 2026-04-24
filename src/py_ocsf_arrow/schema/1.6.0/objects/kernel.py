"""Auto-generated Arrow schema for OCSF object 'kernel'.

OCSF version 1.6.0.
"""

import pyarrow as pa


def get_kernel_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'kernel'."""
    return pa.schema(
        [
            pa.field("is_system", pa.bool8(), nullable=True),
            pa.field("name", pa.string(), nullable=False),
            pa.field("path", pa.string(), nullable=True),
            pa.field("system_call", pa.string(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("type_id", pa.int32(), nullable=False),
        ]
    )


KERNEL_SCHEMA = get_kernel_schema()
