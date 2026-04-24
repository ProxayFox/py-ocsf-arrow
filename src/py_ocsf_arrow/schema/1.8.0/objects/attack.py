"""Auto-generated Arrow schema for OCSF object 'attack'.

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


MITIGATION_SCHEMA = _load_dep("mitigation").MITIGATION_SCHEMA
SUB_TECHNIQUE_SCHEMA = _load_dep("sub_technique").SUB_TECHNIQUE_SCHEMA
TACTIC_SCHEMA = _load_dep("tactic").TACTIC_SCHEMA
TECHNIQUE_SCHEMA = _load_dep("technique").TECHNIQUE_SCHEMA


def get_attack_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'attack'."""
    return pa.schema(
        [
            pa.field("mitigation", pa.struct(list(MITIGATION_SCHEMA)), nullable=True),
            pa.field(
                "sub_technique",
                pa.struct(list(SUB_TECHNIQUE_SCHEMA)),
                nullable=True,
            ),
            pa.field("tactic", pa.struct(list(TACTIC_SCHEMA)), nullable=True),
            pa.field(
                "tactics",
                pa.list_(pa.struct(list(TACTIC_SCHEMA))),
                nullable=True,
            ),
            pa.field("technique", pa.struct(list(TECHNIQUE_SCHEMA)), nullable=True),
            pa.field("version", pa.string(), nullable=True),
        ]
    )


ATTACK_SCHEMA = get_attack_schema()
