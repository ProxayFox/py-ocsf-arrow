"""Auto-generated Arrow schema for OCSF object 'finding_info'.

Generated from version 1.1.0 at 2026-04-24T03:47:40+00:00.
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
KILL_CHAIN_PHASE_SCHEMA = _load_dep("kill_chain_phase").KILL_CHAIN_PHASE_SCHEMA
RELATED_EVENT_SCHEMA = _load_dep("related_event").RELATED_EVENT_SCHEMA


def get_finding_info_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'finding_info'."""
    return pa.schema(
        [
            pa.field("analytic", pa.struct(list(ANALYTIC_SCHEMA)), nullable=True),
            pa.field("created_time", pa.int64(), nullable=True),
            pa.field("created_time_dt", pa.string(), nullable=True),
            pa.field("data_sources", pa.list_(pa.string()), nullable=True),
            pa.field("desc", pa.string(), nullable=True),
            pa.field("first_seen_time", pa.int64(), nullable=True),
            pa.field("first_seen_time_dt", pa.string(), nullable=True),
            pa.field(
                "kill_chain",
                pa.list_(pa.struct(list(KILL_CHAIN_PHASE_SCHEMA))),
                nullable=True,
            ),
            pa.field("last_seen_time", pa.int64(), nullable=True),
            pa.field("last_seen_time_dt", pa.string(), nullable=True),
            pa.field("modified_time", pa.int64(), nullable=True),
            pa.field("modified_time_dt", pa.string(), nullable=True),
            pa.field("product_uid", pa.string(), nullable=True),
            pa.field(
                "related_analytics",
                pa.list_(pa.struct(list(ANALYTIC_SCHEMA))),
                nullable=True,
            ),
            pa.field(
                "related_events",
                pa.list_(pa.struct(list(RELATED_EVENT_SCHEMA))),
                nullable=True,
            ),
            pa.field("src_url", pa.string(), nullable=True),
            pa.field("title", pa.string(), nullable=False),
            pa.field("types", pa.list_(pa.string()), nullable=True),
            pa.field("uid", pa.string(), nullable=False),
        ]
    )


FINDING_INFO_SCHEMA = get_finding_info_schema()
