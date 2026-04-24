"""Auto-generated Arrow schema for OCSF object 'script'.

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


FILE_SCHEMA = _load_dep("file").FILE_SCHEMA
FINGERPRINT_SCHEMA = _load_dep("fingerprint").FINGERPRINT_SCHEMA
LONG_STRING_SCHEMA = _load_dep("long_string").LONG_STRING_SCHEMA


def get_script_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'script'."""
    return pa.schema(
        [
            pa.field("file", pa.struct(list(FILE_SCHEMA)), nullable=True),
            pa.field(
                "hashes", pa.list_(pa.struct(list(FINGERPRINT_SCHEMA))), nullable=True
            ),
            pa.field("name", pa.string(), nullable=True),
            pa.field("parent_uid", pa.string(), nullable=True),
            pa.field(
                "script_content", pa.struct(list(LONG_STRING_SCHEMA)), nullable=False
            ),
            pa.field("type", pa.string(), nullable=True),
            pa.field("type_id", pa.int32(), nullable=False),
            pa.field("uid", pa.string(), nullable=True),
        ]
    )


SCRIPT_SCHEMA = get_script_schema()
