"""Auto-generated Arrow schema for OCSF object 'network_traffic'.

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


TIMESPAN_SCHEMA = _load_dep("timespan").TIMESPAN_SCHEMA


def get_network_traffic_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'network_traffic'."""
    return pa.schema(
        [
            pa.field("bytes", pa.int64(), nullable=True),
            pa.field("bytes_in", pa.int64(), nullable=True),
            pa.field("bytes_missed", pa.int64(), nullable=True),
            pa.field("bytes_out", pa.int64(), nullable=True),
            pa.field("chunks", pa.int64(), nullable=True),
            pa.field("chunks_in", pa.int64(), nullable=True),
            pa.field("chunks_out", pa.int64(), nullable=True),
            pa.field("end_time", pa.int64(), nullable=True),
            pa.field("end_time_dt", pa.string(), nullable=True),
            pa.field("packets", pa.int64(), nullable=True),
            pa.field("packets_in", pa.int64(), nullable=True),
            pa.field("packets_out", pa.int64(), nullable=True),
            pa.field("start_time", pa.int64(), nullable=True),
            pa.field("start_time_dt", pa.string(), nullable=True),
            pa.field("timespan", pa.struct(list(TIMESPAN_SCHEMA)), nullable=True),
        ]
    )


NETWORK_TRAFFIC_SCHEMA = get_network_traffic_schema()
