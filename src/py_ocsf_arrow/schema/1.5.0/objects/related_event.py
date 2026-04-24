"""Auto-generated Arrow schema for OCSF object 'related_event'.

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


KEY_VALUE_OBJECT_SCHEMA = _load_dep("key_value_object").KEY_VALUE_OBJECT_SCHEMA
KILL_CHAIN_PHASE_SCHEMA = _load_dep("kill_chain_phase").KILL_CHAIN_PHASE_SCHEMA
OBSERVABLE_SCHEMA = _load_dep("observable").OBSERVABLE_SCHEMA
PRODUCT_SCHEMA = _load_dep("product").PRODUCT_SCHEMA
TRAIT_SCHEMA = _load_dep("trait").TRAIT_SCHEMA


def get_related_event_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'related_event'."""
    return pa.schema(
        [
            pa.field("count", pa.int32(), nullable=True),
            pa.field("created_time", pa.int64(), nullable=True),
            pa.field("created_time_dt", pa.string(), nullable=True),
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
            pa.field(
                "observables",
                pa.list_(pa.struct(list(OBSERVABLE_SCHEMA))),
                nullable=True,
            ),
            pa.field("product", pa.struct(list(PRODUCT_SCHEMA)), nullable=True),
            pa.field("product_uid", pa.string(), nullable=True),
            pa.field("severity", pa.string(), nullable=True),
            pa.field("severity_id", pa.int32(), nullable=True),
            pa.field(
                "tags",
                pa.list_(pa.struct(list(KEY_VALUE_OBJECT_SCHEMA))),
                nullable=True,
            ),
            pa.field("title", pa.string(), nullable=True),
            pa.field("traits", pa.list_(pa.struct(list(TRAIT_SCHEMA))), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("type_name", pa.string(), nullable=True),
            pa.field("type_uid", pa.int64(), nullable=True),
            pa.field("uid", pa.string(), nullable=False),
        ]
    )


RELATED_EVENT_SCHEMA = get_related_event_schema()
