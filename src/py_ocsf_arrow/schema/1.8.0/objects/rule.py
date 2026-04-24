"""Auto-generated Arrow schema for OCSF object 'rule'.

OCSF version 1.8.0.
"""

import pyarrow as pa


def get_rule_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'rule'."""
    return pa.schema(
        [
            pa.field("category", pa.string(), nullable=True),
            pa.field("desc", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("version", pa.string(), nullable=True),
        ]
    )


RULE_SCHEMA = get_rule_schema()
