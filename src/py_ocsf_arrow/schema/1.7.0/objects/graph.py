"""Auto-generated Arrow schema for OCSF object 'graph'.

Generated from version 1.7.0 at 2026-04-24T03:47:42+00:00.
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


EDGE_SCHEMA = _load_dep("edge").EDGE_SCHEMA
NODE_SCHEMA = _load_dep("node").NODE_SCHEMA


def get_graph_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'graph'."""
    return pa.schema(
        [
            pa.field("desc", pa.string(), nullable=True),
            pa.field("edges", pa.list_(pa.struct(list(EDGE_SCHEMA))), nullable=True),
            pa.field("is_directed", pa.bool8(), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("nodes", pa.list_(pa.struct(list(NODE_SCHEMA))), nullable=False),
            pa.field("query_language", pa.string(), nullable=True),
            pa.field("query_language_id", pa.int32(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
        ]
    )


GRAPH_SCHEMA = get_graph_schema()
