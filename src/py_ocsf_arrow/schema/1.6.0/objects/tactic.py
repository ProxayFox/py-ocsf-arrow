"""Auto-generated Arrow schema for OCSF object 'tactic'.

OCSF version 1.6.0.
"""

import pyarrow as pa


def get_tactic_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'tactic'."""
    return pa.schema(
        [
            pa.field("name", pa.string(), nullable=True),
            pa.field("src_url", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
        ]
    )


TACTIC_SCHEMA = get_tactic_schema()
