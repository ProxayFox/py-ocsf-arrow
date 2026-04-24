"""Auto-generated Arrow schema for OCSF object 'email'.

OCSF version 1.7.0.
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
FILE_SCHEMA = _load_dep("file").FILE_SCHEMA
HTTP_HEADER_SCHEMA = _load_dep("http_header").HTTP_HEADER_SCHEMA
URL_SCHEMA = _load_dep("url").URL_SCHEMA


def get_email_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'email'."""
    return pa.schema(
        [
            pa.field("cc", pa.list_(pa.string()), nullable=True),
            pa.field("cc_mailboxes", pa.list_(pa.string()), nullable=True),
            pa.field(
                "data_classification",
                pa.struct(list(DATA_CLASSIFICATION_SCHEMA)),
                nullable=True,
            ),
            pa.field(
                "data_classifications",
                pa.list_(pa.struct(list(DATA_CLASSIFICATION_SCHEMA))),
                nullable=True,
            ),
            pa.field("delivered_to", pa.string(), nullable=True),
            pa.field("delivered_to_list", pa.list_(pa.string()), nullable=True),
            pa.field("files", pa.list_(pa.struct(list(FILE_SCHEMA))), nullable=True),
            pa.field("from", pa.string(), nullable=True),
            pa.field("from_list", pa.list_(pa.string()), nullable=True),
            pa.field("from_mailbox", pa.string(), nullable=True),
            pa.field("from_mailboxes", pa.list_(pa.string()), nullable=True),
            pa.field(
                "http_headers",
                pa.list_(pa.struct(list(HTTP_HEADER_SCHEMA))),
                nullable=True,
            ),
            pa.field("is_read", pa.bool8(), nullable=True),
            pa.field("message_uid", pa.string(), nullable=True),
            pa.field("raw_header", pa.string(), nullable=True),
            pa.field("reply_to", pa.string(), nullable=True),
            pa.field("reply_to_list", pa.list_(pa.string()), nullable=True),
            pa.field("reply_to_mailboxes", pa.list_(pa.string()), nullable=True),
            pa.field("return_path", pa.string(), nullable=True),
            pa.field("sender", pa.string(), nullable=True),
            pa.field("sender_mailbox", pa.string(), nullable=True),
            pa.field("size", pa.int64(), nullable=True),
            pa.field("smtp_from", pa.string(), nullable=True),
            pa.field("smtp_to", pa.list_(pa.string()), nullable=True),
            pa.field("subject", pa.string(), nullable=True),
            pa.field("to", pa.list_(pa.string()), nullable=True),
            pa.field("to_mailboxes", pa.list_(pa.string()), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("urls", pa.list_(pa.struct(list(URL_SCHEMA))), nullable=True),
            pa.field("x_originating_ip", pa.list_(pa.string()), nullable=True),
        ]
    )


EMAIL_SCHEMA = get_email_schema()
