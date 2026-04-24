"""Auto-generated Arrow schema for OCSF object 'dns_query'.

Generated from version 1.5.0 at 2026-04-24T03:47:41+00:00.
"""

import pyarrow as pa


def get_dns_query_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'dns_query'."""
    return pa.schema(
        [
            pa.field("class", pa.string(), nullable=True),
            pa.field("hostname", pa.string(), nullable=False),
            pa.field("opcode", pa.string(), nullable=True),
            pa.field("opcode_id", pa.int32(), nullable=True),
            pa.field("packet_uid", pa.int32(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
        ]
    )


DNS_QUERY_SCHEMA = get_dns_query_schema()
