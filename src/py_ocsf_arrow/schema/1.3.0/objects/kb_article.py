"""Auto-generated Arrow schema for OCSF object 'kb_article'.

Generated from version 1.3.0 at 2026-04-24T03:47:40+00:00.
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


OS_SCHEMA = _load_dep("os").OS_SCHEMA
PRODUCT_SCHEMA = _load_dep("product").PRODUCT_SCHEMA
TIMESPAN_SCHEMA = _load_dep("timespan").TIMESPAN_SCHEMA


def get_kb_article_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'kb_article'."""
    return pa.schema(
        [
            pa.field("avg_timespan", pa.struct(list(TIMESPAN_SCHEMA)), nullable=True),
            pa.field("bulletin", pa.string(), nullable=True),
            pa.field("classification", pa.string(), nullable=True),
            pa.field("created_time", pa.int64(), nullable=True),
            pa.field("created_time_dt", pa.string(), nullable=True),
            pa.field("install_state", pa.string(), nullable=True),
            pa.field("install_state_id", pa.int32(), nullable=True),
            pa.field("is_superseded", pa.bool8(), nullable=True),
            pa.field("os", pa.struct(list(OS_SCHEMA)), nullable=True),
            pa.field("product", pa.struct(list(PRODUCT_SCHEMA)), nullable=True),
            pa.field("severity", pa.string(), nullable=True),
            pa.field("size", pa.int64(), nullable=True),
            pa.field("src_url", pa.string(), nullable=True),
            pa.field("title", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=False),
        ]
    )


KB_ARTICLE_SCHEMA = get_kb_article_schema()
