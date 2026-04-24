"""Auto-generated Arrow schema for OCSF class 'security_finding'.

Generated from version 1.2.0 at 2026-04-24T03:47:40+00:00.
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


ANALYTIC_SCHEMA = _load_dep("analytic").ANALYTIC_SCHEMA
CIS_CSC_SCHEMA = _load_dep("cis_csc").CIS_CSC_SCHEMA
COMPLIANCE_SCHEMA = _load_dep("compliance").COMPLIANCE_SCHEMA
ENRICHMENT_SCHEMA = _load_dep("enrichment").ENRICHMENT_SCHEMA
FINDING_SCHEMA = _load_dep("finding").FINDING_SCHEMA
KILL_CHAIN_PHASE_SCHEMA = _load_dep("kill_chain_phase").KILL_CHAIN_PHASE_SCHEMA
METADATA_SCHEMA = _load_dep("metadata").METADATA_SCHEMA
OBJECT_SCHEMA = _load_dep("object").OBJECT_SCHEMA
OBSERVABLE_SCHEMA = _load_dep("observable").OBSERVABLE_SCHEMA
PROCESS_SCHEMA = _load_dep("process").PROCESS_SCHEMA
RESOURCE_DETAILS_SCHEMA = _load_dep("resource_details").RESOURCE_DETAILS_SCHEMA
VULNERABILITY_SCHEMA = _load_dep("vulnerability").VULNERABILITY_SCHEMA


def get_security_finding_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF class 'security_finding'."""
    return pa.schema(
        [
            pa.field("activity_id", pa.int32(), nullable=False),
            pa.field("activity_name", pa.string(), nullable=True),
            pa.field("analytic", pa.struct(list(ANALYTIC_SCHEMA)), nullable=True),
            pa.field("category_name", pa.string(), nullable=True),
            pa.field("category_uid", pa.int32(), nullable=False),
            pa.field(
                "cis_csc", pa.list_(pa.struct(list(CIS_CSC_SCHEMA))), nullable=True
            ),
            pa.field("class_name", pa.string(), nullable=True),
            pa.field("class_uid", pa.int32(), nullable=False),
            pa.field("compliance", pa.struct(list(COMPLIANCE_SCHEMA)), nullable=True),
            pa.field("confidence", pa.string(), nullable=True),
            pa.field("confidence_id", pa.int32(), nullable=True),
            pa.field("confidence_score", pa.int32(), nullable=True),
            pa.field("count", pa.int32(), nullable=True),
            pa.field("data_sources", pa.list_(pa.string()), nullable=True),
            pa.field("duration", pa.int32(), nullable=True),
            pa.field("end_time", pa.int64(), nullable=True),
            pa.field("end_time_dt", pa.string(), nullable=True),
            pa.field(
                "enrichments",
                pa.list_(pa.struct(list(ENRICHMENT_SCHEMA))),
                nullable=True,
            ),
            pa.field("evidence", pa.string(), nullable=True),
            pa.field("finding", pa.struct(list(FINDING_SCHEMA)), nullable=False),
            pa.field("impact", pa.string(), nullable=True),
            pa.field("impact_id", pa.int32(), nullable=True),
            pa.field("impact_score", pa.int32(), nullable=True),
            pa.field(
                "kill_chain",
                pa.list_(pa.struct(list(KILL_CHAIN_PHASE_SCHEMA))),
                nullable=True,
            ),
            pa.field("message", pa.string(), nullable=True),
            pa.field("metadata", pa.struct(list(METADATA_SCHEMA)), nullable=False),
            pa.field("nist", pa.list_(pa.string()), nullable=True),
            pa.field(
                "observables",
                pa.list_(pa.struct(list(OBSERVABLE_SCHEMA))),
                nullable=True,
            ),
            pa.field("process", pa.struct(list(PROCESS_SCHEMA)), nullable=True),
            pa.field("raw_data", pa.string(), nullable=True),
            pa.field(
                "resources",
                pa.list_(pa.struct(list(RESOURCE_DETAILS_SCHEMA))),
                nullable=True,
            ),
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
            pa.field(
                "vulnerabilities",
                pa.list_(pa.struct(list(VULNERABILITY_SCHEMA))),
                nullable=True,
            ),
        ]
    )


SECURITY_FINDING_SCHEMA = get_security_finding_schema()
