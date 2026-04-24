"""Auto-generated Arrow schema for OCSF object 'd3f_technique'.

Generated from version 1.6.0 at 2026-04-24T03:47:41+00:00.
"""

import pyarrow as pa


def get_d3f_technique_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'd3f_technique'."""
    return pa.schema(
        [
            pa.field("name", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
        ]
    )


D3F_TECHNIQUE_SCHEMA = get_d3f_technique_schema()
