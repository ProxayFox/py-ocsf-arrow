"""Auto-generated Arrow schema for OCSF object 'response'.

Generated from version 1.8.0 at 2026-04-24T03:47:42+00:00.
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


CONTAINER_SCHEMA = _load_dep("container").CONTAINER_SCHEMA


def get_response_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'response'."""
    return pa.schema(
        [
            pa.field("code", pa.int32(), nullable=True),
            pa.field(
                "containers", pa.list_(pa.struct(list(CONTAINER_SCHEMA))), nullable=True
            ),
            pa.field("data", pa.string(), nullable=True),
            pa.field("error", pa.string(), nullable=True),
            pa.field("error_message", pa.string(), nullable=True),
            pa.field("flags", pa.list_(pa.string()), nullable=True),
            pa.field("message", pa.string(), nullable=True),
        ]
    )


RESPONSE_SCHEMA = get_response_schema()
