"""Auto-generated Arrow schema for OCSF object 'idp'.

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


AUTH_FACTOR_SCHEMA = _load_dep("auth_factor").AUTH_FACTOR_SCHEMA
FINGERPRINT_SCHEMA = _load_dep("fingerprint").FINGERPRINT_SCHEMA
SCIM_SCHEMA = _load_dep("scim").SCIM_SCHEMA
SSO_SCHEMA = _load_dep("sso").SSO_SCHEMA


def get_idp_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'idp'."""
    return pa.schema(
        [
            pa.field(
                "auth_factors",
                pa.list_(pa.struct(list(AUTH_FACTOR_SCHEMA))),
                nullable=True,
            ),
            pa.field("domain", pa.string(), nullable=True),
            pa.field("fingerprint", pa.struct(list(FINGERPRINT_SCHEMA)), nullable=True),
            pa.field("has_mfa", pa.bool8(), nullable=True),
            pa.field("issuer", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("protocol_name", pa.string(), nullable=True),
            pa.field("scim", pa.struct(list(SCIM_SCHEMA)), nullable=True),
            pa.field("sso", pa.struct(list(SSO_SCHEMA)), nullable=True),
            pa.field("state", pa.string(), nullable=True),
            pa.field("state_id", pa.int32(), nullable=True),
            pa.field("tenant_uid", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("url_string", pa.string(), nullable=True),
        ]
    )


IDP_SCHEMA = get_idp_schema()
