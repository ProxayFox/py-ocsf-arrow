"""Auto-generated Arrow schema for OCSF object 'package'.

OCSF version 1.0.0.
"""

import pyarrow as pa


def get_package_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'package'."""
    return pa.schema(
        [
            pa.field("architecture", pa.string(), nullable=True),
            pa.field("epoch", pa.int32(), nullable=True),
            pa.field("license", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=False),
            pa.field("release", pa.string(), nullable=True),
            pa.field("version", pa.string(), nullable=False),
        ]
    )


PACKAGE_SCHEMA = get_package_schema()
