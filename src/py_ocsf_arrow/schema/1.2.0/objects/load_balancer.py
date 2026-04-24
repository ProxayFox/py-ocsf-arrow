"""Auto-generated Arrow schema for OCSF object 'load_balancer'.

OCSF version 1.2.0.
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


ENDPOINT_CONNECTION_SCHEMA = _load_dep("endpoint_connection").ENDPOINT_CONNECTION_SCHEMA
METRIC_SCHEMA = _load_dep("metric").METRIC_SCHEMA
NETWORK_ENDPOINT_SCHEMA = _load_dep("network_endpoint").NETWORK_ENDPOINT_SCHEMA


def get_load_balancer_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'load_balancer'."""
    return pa.schema(
        [
            pa.field("classification", pa.string(), nullable=True),
            pa.field("code", pa.int32(), nullable=True),
            pa.field(
                "dst_endpoint",
                pa.struct(list(NETWORK_ENDPOINT_SCHEMA)),
                nullable=True,
            ),
            pa.field(
                "endpoint_connections",
                pa.list_(pa.struct(list(ENDPOINT_CONNECTION_SCHEMA))),
                nullable=True,
            ),
            pa.field("error_message", pa.string(), nullable=True),
            pa.field("message", pa.string(), nullable=True),
            pa.field(
                "metrics",
                pa.list_(pa.struct(list(METRIC_SCHEMA))),
                nullable=True,
            ),
            pa.field("name", pa.string(), nullable=True),
            pa.field("status_detail", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
        ]
    )


LOAD_BALANCER_SCHEMA = get_load_balancer_schema()
