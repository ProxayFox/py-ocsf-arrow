"""Auto-generated Arrow schema for OCSF object 'packet'.

OCSF version 1.8.0.
"""

import pyarrow as pa


def get_packet_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'packet'."""
    return pa.schema(
        [
            pa.field("encoding", pa.string(), nullable=True),
            pa.field("encoding_id", pa.int32(), nullable=True),
            pa.field("end_offset", pa.int64(), nullable=True),
            pa.field("format", pa.string(), nullable=True),
            pa.field("format_id", pa.int32(), nullable=True),
            pa.field("sequence_number", pa.int64(), nullable=True),
            pa.field("source", pa.string(), nullable=True),
            pa.field("source_id", pa.int32(), nullable=True),
            pa.field("start_offset", pa.int64(), nullable=True),
            pa.field("value", pa.string(), nullable=False),
        ]
    )


PACKET_SCHEMA = get_packet_schema()
