"""Auto-generated Arrow schema for OCSF object 'module'.

Generated from version 1.7.0 at 2026-04-24T03:47:42+00:00.
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
FUNCTION_INVOCATION_SCHEMA = _load_dep("function_invocation").FUNCTION_INVOCATION_SCHEMA


def get_module_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'module'."""
    return pa.schema(
        [
            pa.field("base_address", pa.string(), nullable=True),
            pa.field("file", pa.struct(list(FILE_SCHEMA)), nullable=True),
            pa.field(
                "function_invocation",
                pa.struct(list(FUNCTION_INVOCATION_SCHEMA)),
                nullable=True,
            ),
            pa.field("function_name", pa.string(), nullable=True),
            pa.field("load_type", pa.string(), nullable=True),
            pa.field("load_type_id", pa.int32(), nullable=True),
            pa.field("start_address", pa.string(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
        ]
    )


MODULE_SCHEMA = get_module_schema()
