"""Auto-generated Arrow schema for OCSF object 'privilege_info'.

OCSF version 1.8.0.
"""

import pyarrow as pa


def get_privilege_info_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'privilege_info'."""
    return pa.schema(
        [
            pa.field("is_unused", pa.bool8(), nullable=True),
            pa.field("last_used_time", pa.int64(), nullable=True),
            pa.field("last_used_time_dt", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=False),
            pa.field("type", pa.string(), nullable=True),
            pa.field("type_id", pa.int32(), nullable=True),
        ]
    )


PRIVILEGE_INFO_SCHEMA = get_privilege_info_schema()
