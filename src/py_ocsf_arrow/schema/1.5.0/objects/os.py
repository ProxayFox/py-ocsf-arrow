"""Auto-generated Arrow schema for OCSF object 'os'.

Generated from version 1.5.0 at 2026-04-24T03:47:41+00:00.
"""

import pyarrow as pa


def get_os_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'os'."""
    return pa.schema(
        [
            pa.field("build", pa.string(), nullable=True),
            pa.field("country", pa.string(), nullable=True),
            pa.field("cpe_name", pa.string(), nullable=True),
            pa.field("cpu_bits", pa.int32(), nullable=True),
            pa.field("edition", pa.string(), nullable=True),
            pa.field("kernel_release", pa.string(), nullable=True),
            pa.field("lang", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=False),
            pa.field("sp_name", pa.string(), nullable=True),
            pa.field("sp_ver", pa.int32(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("type_id", pa.int32(), nullable=False),
            pa.field("version", pa.string(), nullable=True),
        ]
    )


OS_SCHEMA = get_os_schema()
