"""Auto-generated Arrow schema for OCSF object 'rpc_interface'.

Generated from version 1.7.0 at 2026-04-24T03:47:42+00:00.
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
