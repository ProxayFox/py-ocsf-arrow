"""Auto-generated Arrow schema for OCSF object 'additional_restriction'.

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


POLICY_SCHEMA = _load_dep("policy").POLICY_SCHEMA


def get_additional_restriction_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'additional_restriction'."""
    return pa.schema(
        [
            pa.field("policy", pa.struct(list(POLICY_SCHEMA)), nullable=False),
            pa.field("status", pa.string(), nullable=True),
            pa.field("status_id", pa.int32(), nullable=True),
        ]
    )


ADDITIONAL_RESTRICTION_SCHEMA = get_additional_restriction_schema()
