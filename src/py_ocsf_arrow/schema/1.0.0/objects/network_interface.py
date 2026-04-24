"""Auto-generated Arrow schema for OCSF object 'network_interface'.

OCSF version 1.0.0.
"""

import pyarrow as pa


def get_network_interface_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'network_interface'."""
    return pa.schema(
        [
            pa.field("hostname", pa.string(), nullable=True),
            pa.field("ip", pa.string(), nullable=True),
            pa.field("mac", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("namespace", pa.string(), nullable=True),
            pa.field("subnet_prefix", pa.int32(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("type_id", pa.int32(), nullable=False),
            pa.field("uid", pa.string(), nullable=True),
        ]
    )


NETWORK_INTERFACE_SCHEMA = get_network_interface_schema()
