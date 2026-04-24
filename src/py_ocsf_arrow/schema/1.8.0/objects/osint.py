"""Auto-generated Arrow schema for OCSF object 'osint'.

Generated from version 1.8.0 at 2026-04-24T03:47:42+00:00.
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


ANALYTIC_SCHEMA = _load_dep("analytic").ANALYTIC_SCHEMA
AUTONOMOUS_SYSTEM_SCHEMA = _load_dep("autonomous_system").AUTONOMOUS_SYSTEM_SCHEMA
CAMPAIGN_SCHEMA = _load_dep("campaign").CAMPAIGN_SCHEMA
DIGITAL_SIGNATURE_SCHEMA = _load_dep("digital_signature").DIGITAL_SIGNATURE_SCHEMA
DNS_ANSWER_SCHEMA = _load_dep("dns_answer").DNS_ANSWER_SCHEMA
EMAIL_SCHEMA = _load_dep("email").EMAIL_SCHEMA
EMAIL_AUTH_SCHEMA = _load_dep("email_auth").EMAIL_AUTH_SCHEMA
FILE_SCHEMA = _load_dep("file").FILE_SCHEMA
KILL_CHAIN_PHASE_SCHEMA = _load_dep("kill_chain_phase").KILL_CHAIN_PHASE_SCHEMA
LOCATION_SCHEMA = _load_dep("location").LOCATION_SCHEMA
REPUTATION_SCHEMA = _load_dep("reputation").REPUTATION_SCHEMA
SCRIPT_SCHEMA = _load_dep("script").SCRIPT_SCHEMA
THREAT_ACTOR_SCHEMA = _load_dep("threat_actor").THREAT_ACTOR_SCHEMA
USER_SCHEMA = _load_dep("user").USER_SCHEMA
VULNERABILITY_SCHEMA = _load_dep("vulnerability").VULNERABILITY_SCHEMA
WHOIS_SCHEMA = _load_dep("whois").WHOIS_SCHEMA


def get_osint_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'osint'."""
    return pa.schema(
        [
            pa.field(
                "answers", pa.list_(pa.struct(list(DNS_ANSWER_SCHEMA))), nullable=True
            ),
            pa.field(
                "autonomous_system",
                pa.struct(list(AUTONOMOUS_SYSTEM_SCHEMA)),
                nullable=True,
            ),
            pa.field("campaign", pa.struct(list(CAMPAIGN_SCHEMA)), nullable=True),
            pa.field("category", pa.string(), nullable=True),
            pa.field("comment", pa.string(), nullable=True),
            pa.field("created_time", pa.int64(), nullable=True),
            pa.field("created_time_dt", pa.string(), nullable=True),
            pa.field("creator", pa.struct(list(USER_SCHEMA)), nullable=True),
            pa.field("desc", pa.string(), nullable=True),
            pa.field("detection_pattern", pa.string(), nullable=True),
            pa.field("detection_pattern_type", pa.string(), nullable=True),
            pa.field("detection_pattern_type_id", pa.int32(), nullable=True),
            pa.field("email", pa.struct(list(EMAIL_SCHEMA)), nullable=True),
            pa.field("email_auth", pa.struct(list(EMAIL_AUTH_SCHEMA)), nullable=True),
            pa.field("expiration_time", pa.int64(), nullable=True),
            pa.field("expiration_time_dt", pa.string(), nullable=True),
            pa.field("external_uid", pa.string(), nullable=True),
            pa.field("file", pa.struct(list(FILE_SCHEMA)), nullable=True),
            pa.field("intrusion_sets", pa.list_(pa.string()), nullable=True),
            pa.field(
                "kill_chain",
                pa.list_(pa.struct(list(KILL_CHAIN_PHASE_SCHEMA))),
                nullable=True,
            ),
            pa.field("labels", pa.list_(pa.string()), nullable=True),
            pa.field("location", pa.struct(list(LOCATION_SCHEMA)), nullable=True),
            pa.field("modified_time", pa.int64(), nullable=True),
            pa.field("modified_time_dt", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("references", pa.list_(pa.string()), nullable=True),
            pa.field(
                "related_analytics",
                pa.list_(pa.struct(list(ANALYTIC_SCHEMA))),
                nullable=True,
            ),
            pa.field("reputation", pa.struct(list(REPUTATION_SCHEMA)), nullable=True),
            pa.field("script", pa.struct(list(SCRIPT_SCHEMA)), nullable=True),
            pa.field("severity", pa.string(), nullable=True),
            pa.field("severity_id", pa.int32(), nullable=True),
            pa.field(
                "signatures",
                pa.list_(pa.struct(list(DIGITAL_SIGNATURE_SCHEMA))),
                nullable=True,
            ),
            pa.field("subdomains", pa.list_(pa.string()), nullable=True),
            pa.field("subnet", pa.string(), nullable=True),
            pa.field(
                "threat_actor", pa.struct(list(THREAT_ACTOR_SCHEMA)), nullable=True
            ),
            pa.field("tlp", pa.string(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("type_id", pa.int32(), nullable=False),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("uploaded_time", pa.int64(), nullable=True),
            pa.field("uploaded_time_dt", pa.string(), nullable=True),
            pa.field("value", pa.string(), nullable=False),
            pa.field("vendor_name", pa.string(), nullable=True),
            pa.field(
                "vulnerabilities",
                pa.list_(pa.struct(list(VULNERABILITY_SCHEMA))),
                nullable=True,
            ),
            pa.field("whois", pa.struct(list(WHOIS_SCHEMA)), nullable=True),
        ]
    )


OSINT_SCHEMA = get_osint_schema()
