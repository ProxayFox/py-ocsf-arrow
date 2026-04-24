"""Auto-generated Arrow schema for OCSF object 'enrichment'.

OCSF version 1.5.0.
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


REPUTATION_SCHEMA = _load_dep("reputation").REPUTATION_SCHEMA


def get_enrichment_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'enrichment'."""
    return pa.schema(
        [
            pa.field("created_time", pa.int64(), nullable=True),
            pa.field("created_time_dt", pa.string(), nullable=True),
            pa.field("data", pa.string(), nullable=False),
            pa.field("desc", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=False),
            pa.field("provider", pa.string(), nullable=True),
            pa.field("reputation", pa.struct(list(REPUTATION_SCHEMA)), nullable=True),
            pa.field("short_desc", pa.string(), nullable=True),
            pa.field("src_url", pa.string(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("value", pa.string(), nullable=False),
        ]
    )


ENRICHMENT_SCHEMA = get_enrichment_schema()
