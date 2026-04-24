"""Auto-generated Arrow schema for OCSF object 'gpu_info'.

Generated from version 1.8.0 at 2026-04-24T03:47:42+00:00.
"""

import pyarrow as pa


def get_gpu_info_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'gpu_info'."""
    return pa.schema(
        [
            pa.field("bus_type", pa.string(), nullable=True),
            pa.field("bus_type_id", pa.int32(), nullable=True),
            pa.field("cores", pa.int32(), nullable=True),
            pa.field("model", pa.string(), nullable=True),
            pa.field("vendor_name", pa.string(), nullable=True),
            pa.field("vram_mode", pa.string(), nullable=True),
            pa.field("vram_mode_id", pa.int32(), nullable=True),
            pa.field("vram_size", pa.int32(), nullable=True),
        ]
    )


GPU_INFO_SCHEMA = get_gpu_info_schema()
