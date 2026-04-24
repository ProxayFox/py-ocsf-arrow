"""Auto-generated Arrow schema for OCSF object 'parameter'.

OCSF version 1.7.0.
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
