"""Auto-generated Arrow schema for OCSF object 'rpc_interface'.

OCSF version 1.7.0.
"""

import pyarrow as pa


def get_rpc_interface_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'rpc_interface'."""
    return pa.schema(
        [
            pa.field("ack_reason", pa.int32(), nullable=True),
            pa.field("ack_result", pa.int32(), nullable=True),
            pa.field("uuid", pa.string(), nullable=False),
            pa.field("version", pa.string(), nullable=False),
        ]
    )


RPC_INTERFACE_SCHEMA = get_rpc_interface_schema()
