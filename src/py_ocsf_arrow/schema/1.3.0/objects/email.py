"""Auto-generated Arrow schema for OCSF object 'email'.

OCSF version 1.3.0.
"""

import importlib.util
from pathlib import Path

import pyarrow as pa

_OBJECTS_DIR = Path(__file__).parent


def _load_dep(name: str):
    spec = importlib.util.spec_from_file_location(name, _OBJECTS_DIR / f"{name}.py")
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


DATA_CLASSIFICATION_SCHEMA = _load_dep("data_classification").DATA_CLASSIFICATION_SCHEMA


def get_email_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'email'."""
    return pa.schema(
        [
            pa.field("cc", pa.list_(pa.string()), nullable=True),
            pa.field(
                "data_classification",
                pa.struct(list(DATA_CLASSIFICATION_SCHEMA)),
                nullable=True,
            ),
            pa.field("delivered_to", pa.string(), nullable=True),
            pa.field("from", pa.string(), nullable=False),
            pa.field("message_uid", pa.string(), nullable=True),
            pa.field("raw_header", pa.string(), nullable=True),
            pa.field("reply_to", pa.string(), nullable=True),
            pa.field("size", pa.int64(), nullable=True),
            pa.field("smtp_from", pa.string(), nullable=True),
            pa.field("smtp_to", pa.list_(pa.string()), nullable=True),
            pa.field("subject", pa.string(), nullable=True),
            pa.field("to", pa.list_(pa.string()), nullable=False),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("x_originating_ip", pa.list_(pa.string()), nullable=True),
        ]
    )


EMAIL_SCHEMA = get_email_schema()
