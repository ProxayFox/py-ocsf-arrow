"""Auto-generated Arrow schema for OCSF object 'mitigation'.

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


D3FEND_SCHEMA = _load_dep("d3fend").D3FEND_SCHEMA


def get_mitigation_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'mitigation'."""
    return pa.schema(
        [
            pa.field(
                "countermeasures",
                pa.list_(pa.struct(list(D3FEND_SCHEMA))),
                nullable=True,
            ),
            pa.field("name", pa.string(), nullable=True),
            pa.field("src_url", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
        ]
    )


MITIGATION_SCHEMA = get_mitigation_schema()
