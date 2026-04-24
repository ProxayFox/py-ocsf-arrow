"""Auto-generated Arrow schema for OCSF object 'user'.

OCSF version 1.7.0.
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


ACCOUNT_SCHEMA = _load_dep("account").ACCOUNT_SCHEMA
GROUP_SCHEMA = _load_dep("group").GROUP_SCHEMA
LDAP_PERSON_SCHEMA = _load_dep("ldap_person").LDAP_PERSON_SCHEMA
ORGANIZATION_SCHEMA = _load_dep("organization").ORGANIZATION_SCHEMA
PROGRAMMATIC_CREDENTIAL_SCHEMA = _load_dep(
    "programmatic_credential"
).PROGRAMMATIC_CREDENTIAL_SCHEMA


def get_user_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'user'."""
    return pa.schema(
        [
            pa.field("account", pa.struct(list(ACCOUNT_SCHEMA)), nullable=True),
            pa.field("credential_uid", pa.string(), nullable=True),
            pa.field("display_name", pa.string(), nullable=True),
            pa.field("domain", pa.string(), nullable=True),
            pa.field("email_addr", pa.string(), nullable=True),
            pa.field("forward_addr", pa.string(), nullable=True),
            pa.field("full_name", pa.string(), nullable=True),
            pa.field("groups", pa.list_(pa.struct(list(GROUP_SCHEMA))), nullable=True),
            pa.field("has_mfa", pa.bool8(), nullable=True),
            pa.field("ldap_person", pa.struct(list(LDAP_PERSON_SCHEMA)), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("org", pa.struct(list(ORGANIZATION_SCHEMA)), nullable=True),
            pa.field("phone_number", pa.string(), nullable=True),
            pa.field(
                "programmatic_credentials",
                pa.list_(pa.struct(list(PROGRAMMATIC_CREDENTIAL_SCHEMA))),
                nullable=True,
            ),
            pa.field("risk_level", pa.string(), nullable=True),
            pa.field("risk_level_id", pa.int32(), nullable=True),
            pa.field("risk_score", pa.int32(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("type_id", pa.int32(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("uid_alt", pa.string(), nullable=True),
        ]
    )


USER_SCHEMA = get_user_schema()
