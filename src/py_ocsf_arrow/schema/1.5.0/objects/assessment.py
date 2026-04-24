"""Auto-generated Arrow schema for OCSF object 'assessment'.

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


POLICY_SCHEMA = _load_dep("policy").POLICY_SCHEMA


def get_assessment_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'assessment'."""
    return pa.schema(
        [
            pa.field("category", pa.string(), nullable=True),
            pa.field("desc", pa.string(), nullable=True),
            pa.field("meets_criteria", pa.bool8(), nullable=False),
            pa.field("name", pa.string(), nullable=True),
            pa.field("policy", pa.struct(list(POLICY_SCHEMA)), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
        ]
    )


ASSESSMENT_SCHEMA = get_assessment_schema()
