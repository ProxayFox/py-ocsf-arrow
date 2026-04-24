"""Auto-generated Arrow schema for OCSF object 'd3f_tactic'.

OCSF version 1.4.0.
"""

import pyarrow as pa


def get_d3f_tactic_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'd3f_tactic'."""
    return pa.schema(
        [
            pa.field("name", pa.string(), nullable=True),
            pa.field("src_url", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
        ]
    )


D3F_TACTIC_SCHEMA = get_d3f_tactic_schema()
