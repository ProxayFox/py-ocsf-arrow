"""Auto-generated Arrow schema for OCSF object 'process_entity'.

Generated from version 1.8.0 at 2026-04-24T03:47:42+00:00.
"""

import pyarrow as pa


def get_process_entity_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'process_entity'."""
    return pa.schema(
        [
            pa.field("cmd_line", pa.string(), nullable=True),
            pa.field("cpid", pa.string(), nullable=True),
            pa.field("created_time", pa.int64(), nullable=True),
            pa.field("created_time_dt", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("path", pa.string(), nullable=True),
            pa.field("pid", pa.int32(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
        ]
    )


PROCESS_ENTITY_SCHEMA = get_process_entity_schema()
