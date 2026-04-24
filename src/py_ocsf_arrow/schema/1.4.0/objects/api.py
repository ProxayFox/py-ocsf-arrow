"""Auto-generated Arrow schema for OCSF object 'api'.

Generated from version 1.4.0 at 2026-04-24T03:47:41+00:00.
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


REQUEST_SCHEMA = _load_dep("request").REQUEST_SCHEMA
RESPONSE_SCHEMA = _load_dep("response").RESPONSE_SCHEMA
SERVICE_SCHEMA = _load_dep("service").SERVICE_SCHEMA


def get_api_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'api'."""
    return pa.schema(
        [
            pa.field("operation", pa.string(), nullable=False),
            pa.field("request", pa.struct(list(REQUEST_SCHEMA)), nullable=True),
            pa.field("response", pa.struct(list(RESPONSE_SCHEMA)), nullable=True),
            pa.field("service", pa.struct(list(SERVICE_SCHEMA)), nullable=True),
            pa.field("version", pa.string(), nullable=True),
        ]
    )


API_SCHEMA = get_api_schema()
