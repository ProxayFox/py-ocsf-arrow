"""Auto-generated Arrow schema for OCSF object 'sso'.

Generated from version 1.6.0 at 2026-04-24T03:47:41+00:00.
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


CERTIFICATE_SCHEMA = _load_dep("certificate").CERTIFICATE_SCHEMA


def get_sso_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'sso'."""
    return pa.schema(
        [
            pa.field("auth_protocol", pa.string(), nullable=True),
            pa.field("auth_protocol_id", pa.int32(), nullable=True),
            pa.field("certificate", pa.struct(list(CERTIFICATE_SCHEMA)), nullable=True),
            pa.field("created_time", pa.int64(), nullable=True),
            pa.field("created_time_dt", pa.string(), nullable=True),
            pa.field("duration_mins", pa.int32(), nullable=True),
            pa.field("idle_timeout", pa.int32(), nullable=True),
            pa.field("login_endpoint", pa.string(), nullable=True),
            pa.field("logout_endpoint", pa.string(), nullable=True),
            pa.field("metadata_endpoint", pa.string(), nullable=True),
            pa.field("modified_time", pa.int64(), nullable=True),
            pa.field("modified_time_dt", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("protocol_name", pa.string(), nullable=True),
            pa.field("scopes", pa.list_(pa.string()), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("vendor_name", pa.string(), nullable=True),
        ]
    )


SSO_SCHEMA = get_sso_schema()
