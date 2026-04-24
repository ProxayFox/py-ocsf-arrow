"""Auto-generated Arrow schema for OCSF object 'request'.

OCSF version 1.4.0.
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


CONTAINER_SCHEMA = _load_dep("container").CONTAINER_SCHEMA


def get_request_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'request'."""
    return pa.schema(
        [
            pa.field(
                "containers",
                pa.list_(pa.struct(list(CONTAINER_SCHEMA))),
                nullable=True,
            ),
            pa.field("data", pa.string(), nullable=True),
            pa.field("flags", pa.list_(pa.string()), nullable=True),
            pa.field("uid", pa.string(), nullable=False),
        ]
    )


REQUEST_SCHEMA = get_request_schema()
