"""Auto-generated Arrow schema for OCSF object 'dns_answer'.

Generated from version 1.2.0 at 2026-04-24T03:47:40+00:00.
"""

import pyarrow as pa


def get_dns_answer_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'dns_answer'."""
    return pa.schema(
        [
            pa.field("class", pa.string(), nullable=True),
            pa.field("flag_ids", pa.list_(pa.int32()), nullable=True),
            pa.field("flags", pa.list_(pa.string()), nullable=True),
            pa.field("packet_uid", pa.int32(), nullable=True),
            pa.field("rdata", pa.string(), nullable=False),
            pa.field("ttl", pa.int32(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
        ]
    )


DNS_ANSWER_SCHEMA = get_dns_answer_schema()
