"""Auto-generated Arrow schema for OCSF object 'd3f_technique'.

OCSF version 1.3.0.
"""

import pyarrow as pa


def get_d3f_technique_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'd3f_technique'."""
    return pa.schema(
        [
            pa.field("name", pa.string(), nullable=True),
            pa.field("src_url", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
        ]
    )


D3F_TECHNIQUE_SCHEMA = get_d3f_technique_schema()
