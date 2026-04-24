"""Auto-generated Arrow schema for OCSF object 'http_request'.

Generated from version 1.3.0 at 2026-04-24T03:47:40+00:00.
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


HTTP_HEADER_SCHEMA = _load_dep("http_header").HTTP_HEADER_SCHEMA
URL_SCHEMA = _load_dep("url").URL_SCHEMA


def get_http_request_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'http_request'."""
    return pa.schema(
        [
            pa.field("args", pa.string(), nullable=True),
            pa.field(
                "http_headers",
                pa.list_(pa.struct(list(HTTP_HEADER_SCHEMA))),
                nullable=True,
            ),
            pa.field("http_method", pa.string(), nullable=True),
            pa.field("length", pa.int32(), nullable=True),
            pa.field("referrer", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("url", pa.struct(list(URL_SCHEMA)), nullable=True),
            pa.field("user_agent", pa.string(), nullable=True),
            pa.field("version", pa.string(), nullable=True),
            pa.field("x_forwarded_for", pa.list_(pa.string()), nullable=True),
        ]
    )


HTTP_REQUEST_SCHEMA = get_http_request_schema()
