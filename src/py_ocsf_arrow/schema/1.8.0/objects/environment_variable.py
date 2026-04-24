"""Auto-generated Arrow schema for OCSF object 'environment_variable'.

Generated from version 1.8.0 at 2026-04-24T03:47:42+00:00.
"""

import pyarrow as pa


def get_environment_variable_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'environment_variable'."""
    return pa.schema(
        [
            pa.field("name", pa.string(), nullable=False),
            pa.field("value", pa.string(), nullable=False),
        ]
    )


ENVIRONMENT_VARIABLE_SCHEMA = get_environment_variable_schema()
