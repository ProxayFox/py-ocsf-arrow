"""Auto-generated Arrow schema for OCSF object 'network_interface'.

OCSF version 1.7.0.
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


PORT_INFO_SCHEMA = _load_dep("port_info").PORT_INFO_SCHEMA


def get_network_interface_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'network_interface'."""
    return pa.schema(
        [
            pa.field("hostname", pa.string(), nullable=True),
            pa.field("ip", pa.string(), nullable=True),
            pa.field("mac", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("namespace", pa.string(), nullable=True),
            pa.field(
                "open_ports",
                pa.list_(pa.struct(list(PORT_INFO_SCHEMA))),
                nullable=True,
            ),
            pa.field("subnet_prefix", pa.int32(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("type_id", pa.int32(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
        ]
    )


NETWORK_INTERFACE_SCHEMA = get_network_interface_schema()
