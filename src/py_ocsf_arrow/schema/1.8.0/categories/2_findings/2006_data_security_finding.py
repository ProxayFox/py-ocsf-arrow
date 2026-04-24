"""Auto-generated Arrow schema for OCSF class 'data_security_finding'.

Generated from version 1.8.0 at 2026-04-24T03:47:42+00:00.
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


DATA_SECURITY_SCHEMA = _load_dep("data_security").DATA_SECURITY_SCHEMA
DATABASE_SCHEMA = _load_dep("database").DATABASE_SCHEMA
DATABUCKET_SCHEMA = _load_dep("databucket").DATABUCKET_SCHEMA
ENRICHMENT_SCHEMA = _load_dep("enrichment").ENRICHMENT_SCHEMA
FILE_SCHEMA = _load_dep("file").FILE_SCHEMA
FINDING_INFO_SCHEMA = _load_dep("finding_info").FINDING_INFO_SCHEMA
FINGERPRINT_SCHEMA = _load_dep("fingerprint").FINGERPRINT_SCHEMA
METADATA_SCHEMA = _load_dep("metadata").METADATA_SCHEMA
NETWORK_ENDPOINT_SCHEMA = _load_dep("network_endpoint").NETWORK_ENDPOINT_SCHEMA
OBJECT_SCHEMA = _load_dep("object").OBJECT_SCHEMA
OBSERVABLE_SCHEMA = _load_dep("observable").OBSERVABLE_SCHEMA
RESOURCE_DETAILS_SCHEMA = _load_dep("resource_details").RESOURCE_DETAILS_SCHEMA
TABLE_SCHEMA = _load_dep("table").TABLE_SCHEMA
VENDOR_ATTRIBUTES_SCHEMA = _load_dep("vendor_attributes").VENDOR_ATTRIBUTES_SCHEMA


def get_data_security_finding_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF class 'data_security_finding'."""
    return pa.schema(
        [
            pa.field("activity_id", pa.int32(), nullable=False),
            pa.field("activity_name", pa.string(), nullable=True),
            pa.field("category_name", pa.string(), nullable=True),
            pa.field("category_uid", pa.int32(), nullable=False),
            pa.field("class_name", pa.string(), nullable=True),
            pa.field("class_uid", pa.int32(), nullable=False),
            pa.field("comment", pa.string(), nullable=True),
            pa.field("count", pa.int32(), nullable=True),
            pa.field(
                "data_security", pa.struct(list(DATA_SECURITY_SCHEMA)), nullable=True
            ),
            pa.field("database", pa.struct(list(DATABASE_SCHEMA)), nullable=True),
            pa.field("databucket", pa.struct(list(DATABUCKET_SCHEMA)), nullable=True),
            pa.field(
                "dst_endpoint", pa.struct(list(NETWORK_ENDPOINT_SCHEMA)), nullable=True
            ),
            pa.field("duration", pa.int64(), nullable=True),
            pa.field("end_time", pa.int64(), nullable=True),
            pa.field("end_time_dt", pa.string(), nullable=True),
            pa.field(
                "enrichments",
                pa.list_(pa.struct(list(ENRICHMENT_SCHEMA))),
                nullable=True,
            ),
            pa.field("file", pa.struct(list(FILE_SCHEMA)), nullable=True),
            pa.field(
                "finding_info", pa.struct(list(FINDING_INFO_SCHEMA)), nullable=False
            ),
            pa.field("message", pa.string(), nullable=True),
            pa.field("metadata", pa.struct(list(METADATA_SCHEMA)), nullable=False),
            pa.field(
                "observables",
                pa.list_(pa.struct(list(OBSERVABLE_SCHEMA))),
                nullable=True,
            ),
            pa.field("raw_data", pa.string(), nullable=True),
            pa.field(
                "raw_data_hash", pa.struct(list(FINGERPRINT_SCHEMA)), nullable=True
            ),
            pa.field("raw_data_size", pa.int64(), nullable=True),
            pa.field(
                "resources",
                pa.list_(pa.struct(list(RESOURCE_DETAILS_SCHEMA))),
                nullable=True,
            ),
            pa.field("severity", pa.string(), nullable=True),
            pa.field("severity_id", pa.int32(), nullable=False),
            pa.field(
                "src_endpoint", pa.struct(list(NETWORK_ENDPOINT_SCHEMA)), nullable=True
            ),
            pa.field("start_time", pa.int64(), nullable=True),
            pa.field("start_time_dt", pa.string(), nullable=True),
            pa.field("status", pa.string(), nullable=True),
            pa.field("status_code", pa.string(), nullable=True),
            pa.field("status_detail", pa.string(), nullable=True),
            pa.field("status_id", pa.int32(), nullable=True),
            pa.field("table", pa.struct(list(TABLE_SCHEMA)), nullable=True),
            pa.field("time", pa.int64(), nullable=False),
            pa.field("time_dt", pa.string(), nullable=True),
            pa.field("timezone_offset", pa.int32(), nullable=True),
            pa.field("type_name", pa.string(), nullable=True),
            pa.field("type_uid", pa.int64(), nullable=False),
            pa.field("unmapped", pa.struct(list(OBJECT_SCHEMA)), nullable=True),
            pa.field(
                "vendor_attributes",
                pa.struct(list(VENDOR_ATTRIBUTES_SCHEMA)),
                nullable=True,
            ),
        ]
    )


DATA_SECURITY_FINDING_SCHEMA = get_data_security_finding_schema()
