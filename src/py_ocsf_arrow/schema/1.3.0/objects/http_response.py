"""Auto-generated Arrow schema for OCSF object 'http_response'.

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


def get_http_response_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'http_response'."""
    return pa.schema(
        [
            pa.field("code", pa.int32(), nullable=False),
            pa.field("content_type", pa.string(), nullable=True),
            pa.field(
                "http_headers",
                pa.list_(pa.struct(list(HTTP_HEADER_SCHEMA))),
                nullable=True,
            ),
            pa.field("latency", pa.int32(), nullable=True),
            pa.field("length", pa.int32(), nullable=True),
            pa.field("message", pa.string(), nullable=True),
            pa.field("status", pa.string(), nullable=True),
        ]
    )


HTTP_RESPONSE_SCHEMA = get_http_response_schema()
