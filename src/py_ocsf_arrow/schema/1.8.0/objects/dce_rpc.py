"""Auto-generated Arrow schema for OCSF object 'dce_rpc'.

OCSF version 1.8.0.
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


RPC_INTERFACE_SCHEMA = _load_dep("rpc_interface").RPC_INTERFACE_SCHEMA


def get_dce_rpc_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'dce_rpc'."""
    return pa.schema(
        [
            pa.field("command", pa.string(), nullable=True),
            pa.field("command_response", pa.string(), nullable=True),
            pa.field("flags", pa.list_(pa.string()), nullable=False),
            pa.field("opnum", pa.int32(), nullable=True),
            pa.field(
                "rpc_interface",
                pa.struct(list(RPC_INTERFACE_SCHEMA)),
                nullable=False,
            ),
        ]
    )


DCE_RPC_SCHEMA = get_dce_rpc_schema()
