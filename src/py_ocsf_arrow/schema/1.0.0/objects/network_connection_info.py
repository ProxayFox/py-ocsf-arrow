"""Auto-generated Arrow schema for OCSF object 'network_connection_info'.

OCSF version 1.0.0.
"""

import pyarrow as pa


def get_network_connection_info_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'network_connection_info'."""
    return pa.schema(
        [
            pa.field("boundary", pa.string(), nullable=True),
            pa.field("boundary_id", pa.int32(), nullable=True),
            pa.field("direction", pa.string(), nullable=True),
            pa.field("direction_id", pa.int32(), nullable=False),
            pa.field("protocol_name", pa.string(), nullable=True),
            pa.field("protocol_num", pa.int32(), nullable=True),
            pa.field("protocol_ver", pa.string(), nullable=True),
            pa.field("protocol_ver_id", pa.int32(), nullable=True),
            pa.field("tcp_flags", pa.int32(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
        ]
    )


NETWORK_CONNECTION_INFO_SCHEMA = get_network_connection_info_schema()
