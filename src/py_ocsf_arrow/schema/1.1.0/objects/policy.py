"""Auto-generated Arrow schema for OCSF object 'policy'.

OCSF version 1.1.0.
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


GROUP_SCHEMA = _load_dep("group").GROUP_SCHEMA


def get_policy_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'policy'."""
    return pa.schema(
        [
            pa.field("desc", pa.string(), nullable=True),
            pa.field("group", pa.struct(list(GROUP_SCHEMA)), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("version", pa.string(), nullable=True),
        ]
    )


POLICY_SCHEMA = get_policy_schema()
