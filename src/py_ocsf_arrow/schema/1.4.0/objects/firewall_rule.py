"""Auto-generated Arrow schema for OCSF object 'firewall_rule'.

Generated from version 1.4.0 at 2026-04-24T03:47:41+00:00.
"""

import pyarrow as pa


def get_firewall_rule_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'firewall_rule'."""
    return pa.schema(
        [
            pa.field("category", pa.string(), nullable=True),
            pa.field("condition", pa.string(), nullable=True),
            pa.field("desc", pa.string(), nullable=True),
            pa.field("duration", pa.int64(), nullable=True),
            pa.field("match_details", pa.list_(pa.string()), nullable=True),
            pa.field("match_location", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("rate_limit", pa.int32(), nullable=True),
            pa.field("sensitivity", pa.string(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("version", pa.string(), nullable=True),
        ]
    )


FIREWALL_RULE_SCHEMA = get_firewall_rule_schema()
