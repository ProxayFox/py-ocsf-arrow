"""Auto-generated Arrow schema for OCSF object 'occurrence_details'.

Generated from version 1.7.0 at 2026-04-24T03:47:42+00:00.
"""

import pyarrow as pa


def get_occurrence_details_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'occurrence_details'."""
    return pa.schema(
        [
            pa.field("cell_name", pa.string(), nullable=True),
            pa.field("column_name", pa.string(), nullable=True),
            pa.field("column_number", pa.int32(), nullable=True),
            pa.field("end_line", pa.int32(), nullable=True),
            pa.field("json_path", pa.string(), nullable=True),
            pa.field("page_number", pa.int32(), nullable=True),
            pa.field("record_index_in_array", pa.int32(), nullable=True),
            pa.field("row_number", pa.int32(), nullable=True),
            pa.field("start_line", pa.int32(), nullable=True),
        ]
    )


OCCURRENCE_DETAILS_SCHEMA = get_occurrence_details_schema()
