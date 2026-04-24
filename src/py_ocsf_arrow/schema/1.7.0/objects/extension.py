"""Auto-generated Arrow schema for OCSF object 'extension'.

OCSF version 1.7.0.
"""

import pyarrow as pa


def get_extension_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'extension'."""
    return pa.schema(
        [
            pa.field("name", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("version", pa.string(), nullable=False),
        ]
    )


EXTENSION_SCHEMA = get_extension_schema()
