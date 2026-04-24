"""Auto-generated Arrow schema for OCSF object 'actor'.

OCSF version 1.8.0.
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


AUTHORIZATION_SCHEMA = _load_dep("authorization").AUTHORIZATION_SCHEMA
IDP_SCHEMA = _load_dep("idp").IDP_SCHEMA
PROCESS_SCHEMA = _load_dep("process").PROCESS_SCHEMA
SESSION_SCHEMA = _load_dep("session").SESSION_SCHEMA
USER_SCHEMA = _load_dep("user").USER_SCHEMA


def get_actor_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'actor'."""
    return pa.schema(
        [
            pa.field("app_name", pa.string(), nullable=True),
            pa.field("app_uid", pa.string(), nullable=True),
            pa.field(
                "authorizations",
                pa.list_(pa.struct(list(AUTHORIZATION_SCHEMA))),
                nullable=True,
            ),
            pa.field("idp", pa.struct(list(IDP_SCHEMA)), nullable=True),
            pa.field("invoked_by", pa.string(), nullable=True),
            pa.field("process", pa.struct(list(PROCESS_SCHEMA)), nullable=True),
            pa.field("session", pa.struct(list(SESSION_SCHEMA)), nullable=True),
            pa.field("user", pa.struct(list(USER_SCHEMA)), nullable=True),
        ]
    )


ACTOR_SCHEMA = get_actor_schema()
