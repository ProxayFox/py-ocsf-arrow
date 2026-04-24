"""Auto-generated Arrow schema for OCSF object 'parameter'.

Generated from version 1.7.0 at 2026-04-24T03:47:42+00:00.
"""

import pyarrow as pa


def get_parameter_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'parameter'."""
    return pa.schema(
        [
            pa.field("name", pa.string(), nullable=True),
            pa.field("post_value", pa.string(), nullable=True),
            pa.field("pre_value", pa.string(), nullable=True),
        ]
    )


PARAMETER_SCHEMA = get_parameter_schema()
