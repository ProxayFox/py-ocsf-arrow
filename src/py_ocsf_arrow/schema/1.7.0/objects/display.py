"""Auto-generated Arrow schema for OCSF object 'display'.

OCSF version 1.7.0.
"""

import pyarrow as pa


def get_display_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'display'."""
    return pa.schema(
        [
            pa.field("color_depth", pa.int32(), nullable=True),
            pa.field("physical_height", pa.int32(), nullable=True),
            pa.field("physical_orientation", pa.int32(), nullable=True),
            pa.field("physical_width", pa.int32(), nullable=True),
            pa.field("scale_factor", pa.int32(), nullable=True),
        ]
    )


DISPLAY_SCHEMA = get_display_schema()
