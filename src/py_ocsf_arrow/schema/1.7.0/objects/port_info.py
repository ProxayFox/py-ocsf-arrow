"""Auto-generated Arrow schema for OCSF object 'port_info'.

OCSF version 1.7.0.
"""

import pyarrow as pa


def get_port_info_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'port_info'."""
    return pa.schema(
        [
            pa.field("port", pa.int32(), nullable=False),
            pa.field("protocol_name", pa.string(), nullable=True),
            pa.field("protocol_num", pa.int32(), nullable=True),
        ]
    )


PORT_INFO_SCHEMA = get_port_info_schema()
