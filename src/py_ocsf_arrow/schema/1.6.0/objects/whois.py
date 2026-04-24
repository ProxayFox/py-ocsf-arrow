"""Auto-generated Arrow schema for OCSF object 'whois'.

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


AUTONOMOUS_SYSTEM_SCHEMA = _load_dep("autonomous_system").AUTONOMOUS_SYSTEM_SCHEMA
DOMAIN_CONTACT_SCHEMA = _load_dep("domain_contact").DOMAIN_CONTACT_SCHEMA


def get_whois_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'whois'."""
    return pa.schema(
        [
            pa.field(
                "autonomous_system",
                pa.struct(list(AUTONOMOUS_SYSTEM_SCHEMA)),
                nullable=True,
            ),
            pa.field("created_time", pa.int64(), nullable=True),
            pa.field("created_time_dt", pa.string(), nullable=True),
            pa.field("dnssec_status", pa.string(), nullable=True),
            pa.field("dnssec_status_id", pa.int32(), nullable=True),
            pa.field("domain", pa.string(), nullable=True),
            pa.field(
                "domain_contacts",
                pa.list_(pa.struct(list(DOMAIN_CONTACT_SCHEMA))),
                nullable=True,
            ),
            pa.field("email_addr", pa.string(), nullable=True),
            pa.field("isp", pa.string(), nullable=True),
            pa.field("isp_org", pa.string(), nullable=True),
            pa.field("last_seen_time", pa.int64(), nullable=True),
            pa.field("last_seen_time_dt", pa.string(), nullable=True),
            pa.field("name_servers", pa.list_(pa.string()), nullable=True),
            pa.field("phone_number", pa.string(), nullable=True),
            pa.field("registrar", pa.string(), nullable=True),
            pa.field("status", pa.string(), nullable=True),
            pa.field("subdomains", pa.list_(pa.string()), nullable=True),
            pa.field("subnet", pa.string(), nullable=True),
        ]
    )


WHOIS_SCHEMA = get_whois_schema()
