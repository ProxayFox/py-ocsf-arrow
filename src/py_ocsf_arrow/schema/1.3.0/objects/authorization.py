"""Auto-generated Arrow schema for OCSF object 'authorization'.

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


POLICY_SCHEMA = _load_dep("policy").POLICY_SCHEMA


def get_authorization_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'authorization'."""
    return pa.schema(
        [
            pa.field("decision", pa.string(), nullable=True),
            pa.field("policy", pa.struct(list(POLICY_SCHEMA)), nullable=True),
        ]
    )


AUTHORIZATION_SCHEMA = get_authorization_schema()
