"""Auto-generated Arrow schema for OCSF object 'network_traffic'.

OCSF version 1.5.0.
"""

import pyarrow as pa


def get_network_traffic_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'network_traffic'."""
    return pa.schema(
        [
            pa.field("bytes", pa.int64(), nullable=True),
            pa.field("bytes_in", pa.int64(), nullable=True),
            pa.field("bytes_missed", pa.int64(), nullable=True),
            pa.field("bytes_out", pa.int64(), nullable=True),
            pa.field("chunks", pa.int64(), nullable=True),
            pa.field("chunks_in", pa.int64(), nullable=True),
            pa.field("chunks_out", pa.int64(), nullable=True),
            pa.field("packets", pa.int64(), nullable=True),
            pa.field("packets_in", pa.int64(), nullable=True),
            pa.field("packets_out", pa.int64(), nullable=True),
        ]
    )


NETWORK_TRAFFIC_SCHEMA = get_network_traffic_schema()
