"""Auto-generated Arrow schema for OCSF object 'finding'.

Generated from version 1.5.0 at 2026-04-24T03:47:41+00:00.
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


PRODUCT_SCHEMA = _load_dep("product").PRODUCT_SCHEMA
RELATED_EVENT_SCHEMA = _load_dep("related_event").RELATED_EVENT_SCHEMA
REMEDIATION_SCHEMA = _load_dep("remediation").REMEDIATION_SCHEMA


def get_finding_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'finding'."""
    return pa.schema(
        [
            pa.field("created_time", pa.int64(), nullable=True),
            pa.field("created_time_dt", pa.string(), nullable=True),
            pa.field("desc", pa.string(), nullable=True),
            pa.field("first_seen_time", pa.int64(), nullable=True),
            pa.field("first_seen_time_dt", pa.string(), nullable=True),
            pa.field("last_seen_time", pa.int64(), nullable=True),
            pa.field("last_seen_time_dt", pa.string(), nullable=True),
            pa.field("modified_time", pa.int64(), nullable=True),
            pa.field("modified_time_dt", pa.string(), nullable=True),
            pa.field("product", pa.struct(list(PRODUCT_SCHEMA)), nullable=True),
            pa.field("product_uid", pa.string(), nullable=True),
            pa.field(
                "related_events",
                pa.list_(pa.struct(list(RELATED_EVENT_SCHEMA))),
                nullable=True,
            ),
            pa.field("remediation", pa.struct(list(REMEDIATION_SCHEMA)), nullable=True),
            pa.field("supporting_data", pa.string(), nullable=True),
            pa.field("title", pa.string(), nullable=False),
            pa.field("types", pa.list_(pa.string()), nullable=True),
            pa.field("uid", pa.string(), nullable=False),
        ]
    )


FINDING_SCHEMA = get_finding_schema()
