"""Auto-generated Arrow schema for OCSF object 'ldap_person'.

OCSF version 1.3.0.
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


LOCATION_SCHEMA = _load_dep("location").LOCATION_SCHEMA


def get_ldap_person_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'ldap_person'."""
    return pa.schema(
        [
            pa.field("cost_center", pa.string(), nullable=True),
            pa.field("created_time", pa.int64(), nullable=True),
            pa.field("created_time_dt", pa.string(), nullable=True),
            pa.field("deleted_time", pa.int64(), nullable=True),
            pa.field("deleted_time_dt", pa.string(), nullable=True),
            pa.field("email_addrs", pa.list_(pa.string()), nullable=True),
            pa.field("employee_uid", pa.string(), nullable=True),
            pa.field("given_name", pa.string(), nullable=True),
            pa.field("hire_time", pa.int64(), nullable=True),
            pa.field("hire_time_dt", pa.string(), nullable=True),
            pa.field("job_title", pa.string(), nullable=True),
            pa.field("labels", pa.list_(pa.string()), nullable=True),
            pa.field("last_login_time", pa.int64(), nullable=True),
            pa.field("last_login_time_dt", pa.string(), nullable=True),
            pa.field("ldap_cn", pa.string(), nullable=True),
            pa.field("ldap_dn", pa.string(), nullable=True),
            pa.field("leave_time", pa.int64(), nullable=True),
            pa.field("leave_time_dt", pa.string(), nullable=True),
            pa.field("location", pa.struct(list(LOCATION_SCHEMA)), nullable=True),
            pa.field("manager", pa.string(), nullable=True),
            pa.field("modified_time", pa.int64(), nullable=True),
            pa.field("modified_time_dt", pa.string(), nullable=True),
            pa.field("office_location", pa.string(), nullable=True),
            pa.field("surname", pa.string(), nullable=True),
        ]
    )


LDAP_PERSON_SCHEMA = get_ldap_person_schema()
