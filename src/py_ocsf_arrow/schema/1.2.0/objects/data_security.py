"""Auto-generated Arrow schema for OCSF object 'data_security'.

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


POLICY_SCHEMA = _load_dep("policy").POLICY_SCHEMA


def get_data_security_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'data_security'."""
    return pa.schema(
        [
            pa.field("category", pa.string(), nullable=True),
            pa.field("category_id", pa.int32(), nullable=True),
            pa.field("confidentiality", pa.string(), nullable=True),
            pa.field("confidentiality_id", pa.int32(), nullable=True),
            pa.field("data_lifecycle_state", pa.string(), nullable=True),
            pa.field("data_lifecycle_state_id", pa.int32(), nullable=True),
            pa.field("detection_pattern", pa.string(), nullable=True),
            pa.field("detection_system", pa.string(), nullable=True),
            pa.field("detection_system_id", pa.int32(), nullable=True),
            pa.field("pattern_match", pa.string(), nullable=True),
            pa.field("policy", pa.struct(list(POLICY_SCHEMA)), nullable=True),
        ]
    )


DATA_SECURITY_SCHEMA = get_data_security_schema()
