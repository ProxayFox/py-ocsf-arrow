"""Auto-generated Arrow schema for OCSF object 'managed_entity'.

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


EMAIL_SCHEMA = _load_dep("email").EMAIL_SCHEMA
ORGANIZATION_SCHEMA = _load_dep("organization").ORGANIZATION_SCHEMA
POLICY_SCHEMA = _load_dep("policy").POLICY_SCHEMA
USER_SCHEMA = _load_dep("user").USER_SCHEMA


def get_managed_entity_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'managed_entity'."""
    return pa.schema(
        [
            pa.field("data", pa.string(), nullable=True),
            pa.field("email", pa.struct(list(EMAIL_SCHEMA)), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("org", pa.struct(list(ORGANIZATION_SCHEMA)), nullable=True),
            pa.field("policy", pa.struct(list(POLICY_SCHEMA)), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("type_id", pa.int32(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("user", pa.struct(list(USER_SCHEMA)), nullable=True),
            pa.field("version", pa.string(), nullable=True),
        ]
    )


MANAGED_ENTITY_SCHEMA = get_managed_entity_schema()
