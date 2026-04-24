"""Auto-generated Arrow schema for OCSF object 'message_context'.

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


APPLICATION_SCHEMA = _load_dep("application").APPLICATION_SCHEMA
SERVICE_SCHEMA = _load_dep("service").SERVICE_SCHEMA


def get_message_context_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'message_context'."""
    return pa.schema(
        [
            pa.field("ai_role", pa.string(), nullable=True),
            pa.field("ai_role_id", pa.int32(), nullable=True),
            pa.field("application", pa.struct(list(APPLICATION_SCHEMA)), nullable=True),
            pa.field("completion_tokens", pa.int32(), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("prompt_tokens", pa.int32(), nullable=True),
            pa.field("service", pa.struct(list(SERVICE_SCHEMA)), nullable=True),
            pa.field("total_tokens", pa.int32(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
        ]
    )


MESSAGE_CONTEXT_SCHEMA = get_message_context_schema()
