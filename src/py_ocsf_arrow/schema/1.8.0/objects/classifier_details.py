"""Auto-generated Arrow schema for OCSF object 'classifier_details'.

Generated from version 1.8.0 at 2026-04-24T03:47:42+00:00.
"""

import pyarrow as pa


def get_classifier_details_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'classifier_details'."""
    return pa.schema(
        [
            pa.field("name", pa.string(), nullable=True),
            pa.field("type", pa.string(), nullable=False),
            pa.field("uid", pa.string(), nullable=True),
        ]
    )


CLASSIFIER_DETAILS_SCHEMA = get_classifier_details_schema()
