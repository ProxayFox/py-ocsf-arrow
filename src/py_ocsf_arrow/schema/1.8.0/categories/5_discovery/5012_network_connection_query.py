"""Auto-generated Arrow schema for OCSF class 'network_connection_query'.

OCSF version 1.8.0.
"""

import importlib.util
from pathlib import Path

import pyarrow as pa

_OBJECTS_DIR = Path(__file__).resolve().parents[2] / "objects"


def _load_dep(name: str):
    spec = importlib.util.spec_from_file_location(name, _OBJECTS_DIR / f"{name}.py")
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


ACTOR_SCHEMA = _load_dep("actor").ACTOR_SCHEMA
API_SCHEMA = _load_dep("api").API_SCHEMA
ATTACK_SCHEMA = _load_dep("attack").ATTACK_SCHEMA
AUTHORIZATION_SCHEMA = _load_dep("authorization").AUTHORIZATION_SCHEMA
CLOUD_SCHEMA = _load_dep("cloud").CLOUD_SCHEMA
DEVICE_SCHEMA = _load_dep("device").DEVICE_SCHEMA
ENRICHMENT_SCHEMA = _load_dep("enrichment").ENRICHMENT_SCHEMA
FINGERPRINT_SCHEMA = _load_dep("fingerprint").FINGERPRINT_SCHEMA
FIREWALL_RULE_SCHEMA = _load_dep("firewall_rule").FIREWALL_RULE_SCHEMA
MALWARE_SCHEMA = _load_dep("malware").MALWARE_SCHEMA
MALWARE_SCAN_INFO_SCHEMA = _load_dep("malware_scan_info").MALWARE_SCAN_INFO_SCHEMA
METADATA_SCHEMA = _load_dep("metadata").METADATA_SCHEMA
NETWORK_CONNECTION_INFO_SCHEMA = _load_dep(
    "network_connection_info"
).NETWORK_CONNECTION_INFO_SCHEMA
OBJECT_SCHEMA = _load_dep("object").OBJECT_SCHEMA
OBSERVABLE_SCHEMA = _load_dep("observable").OBSERVABLE_SCHEMA
OSINT_SCHEMA = _load_dep("osint").OSINT_SCHEMA
POLICY_SCHEMA = _load_dep("policy").POLICY_SCHEMA
PROCESS_SCHEMA = _load_dep("process").PROCESS_SCHEMA
QUERY_INFO_SCHEMA = _load_dep("query_info").QUERY_INFO_SCHEMA


def get_network_connection_query_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF class 'network_connection_query'."""
    return pa.schema(
        [
            pa.field("action", pa.string(), nullable=True),
            pa.field("action_id", pa.int32(), nullable=True),
            pa.field("activity_id", pa.int32(), nullable=False),
            pa.field("activity_name", pa.string(), nullable=True),
            pa.field("actor", pa.struct(list(ACTOR_SCHEMA)), nullable=True),
            pa.field("api", pa.struct(list(API_SCHEMA)), nullable=True),
            pa.field(
                "attacks",
                pa.list_(pa.struct(list(ATTACK_SCHEMA))),
                nullable=True,
            ),
            pa.field(
                "authorizations",
                pa.list_(pa.struct(list(AUTHORIZATION_SCHEMA))),
                nullable=True,
            ),
            pa.field("category_name", pa.string(), nullable=True),
            pa.field("category_uid", pa.int32(), nullable=False),
            pa.field("class_name", pa.string(), nullable=True),
            pa.field("class_uid", pa.int32(), nullable=False),
            pa.field("cloud", pa.struct(list(CLOUD_SCHEMA)), nullable=False),
            pa.field("confidence", pa.string(), nullable=True),
            pa.field("confidence_id", pa.int32(), nullable=True),
            pa.field("confidence_score", pa.int32(), nullable=True),
            pa.field(
                "connection_info",
                pa.struct(list(NETWORK_CONNECTION_INFO_SCHEMA)),
                nullable=False,
            ),
            pa.field("count", pa.int32(), nullable=True),
            pa.field("device", pa.struct(list(DEVICE_SCHEMA)), nullable=True),
            pa.field("disposition", pa.string(), nullable=True),
            pa.field("disposition_id", pa.int32(), nullable=True),
            pa.field("duration", pa.int64(), nullable=True),
            pa.field("end_time", pa.int64(), nullable=True),
            pa.field("end_time_dt", pa.string(), nullable=True),
            pa.field(
                "enrichments",
                pa.list_(pa.struct(list(ENRICHMENT_SCHEMA))),
                nullable=True,
            ),
            pa.field(
                "firewall_rule",
                pa.struct(list(FIREWALL_RULE_SCHEMA)),
                nullable=True,
            ),
            pa.field("is_alert", pa.bool8(), nullable=True),
            pa.field(
                "malware",
                pa.list_(pa.struct(list(MALWARE_SCHEMA))),
                nullable=True,
            ),
            pa.field(
                "malware_scan_info",
                pa.struct(list(MALWARE_SCAN_INFO_SCHEMA)),
                nullable=True,
            ),
            pa.field("message", pa.string(), nullable=True),
            pa.field("metadata", pa.struct(list(METADATA_SCHEMA)), nullable=False),
            pa.field(
                "observables",
                pa.list_(pa.struct(list(OBSERVABLE_SCHEMA))),
                nullable=True,
            ),
            pa.field("osint", pa.list_(pa.struct(list(OSINT_SCHEMA))), nullable=False),
            pa.field("policy", pa.struct(list(POLICY_SCHEMA)), nullable=True),
            pa.field("process", pa.struct(list(PROCESS_SCHEMA)), nullable=False),
            pa.field("query_info", pa.struct(list(QUERY_INFO_SCHEMA)), nullable=True),
            pa.field("query_result", pa.string(), nullable=True),
            pa.field("query_result_id", pa.int32(), nullable=False),
            pa.field("raw_data", pa.string(), nullable=True),
            pa.field(
                "raw_data_hash",
                pa.struct(list(FINGERPRINT_SCHEMA)),
                nullable=True,
            ),
            pa.field("raw_data_size", pa.int64(), nullable=True),
            pa.field("risk_details", pa.string(), nullable=True),
            pa.field("risk_level", pa.string(), nullable=True),
            pa.field("risk_level_id", pa.int32(), nullable=True),
            pa.field("risk_score", pa.int32(), nullable=True),
            pa.field("severity", pa.string(), nullable=True),
            pa.field("severity_id", pa.int32(), nullable=False),
            pa.field("start_time", pa.int64(), nullable=True),
            pa.field("start_time_dt", pa.string(), nullable=True),
            pa.field("state", pa.string(), nullable=True),
            pa.field("state_id", pa.int32(), nullable=False),
            pa.field("status", pa.string(), nullable=True),
            pa.field("status_code", pa.string(), nullable=True),
            pa.field("status_detail", pa.string(), nullable=True),
            pa.field("status_id", pa.int32(), nullable=True),
            pa.field("time", pa.int64(), nullable=False),
            pa.field("time_dt", pa.string(), nullable=True),
            pa.field("timezone_offset", pa.int32(), nullable=True),
            pa.field("type_name", pa.string(), nullable=True),
            pa.field("type_uid", pa.int64(), nullable=False),
            pa.field("unmapped", pa.struct(list(OBJECT_SCHEMA)), nullable=True),
        ]
    )


NETWORK_CONNECTION_QUERY_SCHEMA = get_network_connection_query_schema()
