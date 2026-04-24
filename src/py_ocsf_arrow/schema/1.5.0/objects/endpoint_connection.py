"""Auto-generated Arrow schema for OCSF object 'endpoint_connection'.

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


NETWORK_ENDPOINT_SCHEMA = _load_dep("network_endpoint").NETWORK_ENDPOINT_SCHEMA


def get_endpoint_connection_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'endpoint_connection'."""
    return pa.schema(
        [
            pa.field("code", pa.int32(), nullable=True),
            pa.field(
                "network_endpoint",
                pa.struct(list(NETWORK_ENDPOINT_SCHEMA)),
                nullable=True,
            ),
        ]
    )


ENDPOINT_CONNECTION_SCHEMA = get_endpoint_connection_schema()
