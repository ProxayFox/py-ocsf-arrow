"""Auto-generated Arrow schema for OCSF object 'attack'.

OCSF version 1.0.0.
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


TACTIC_SCHEMA = _load_dep("tactic").TACTIC_SCHEMA
TECHNIQUE_SCHEMA = _load_dep("technique").TECHNIQUE_SCHEMA


def get_attack_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'attack'."""
    return pa.schema(
        [
            pa.field(
                "tactics",
                pa.list_(pa.struct(list(TACTIC_SCHEMA))),
                nullable=False,
            ),
            pa.field("technique", pa.struct(list(TECHNIQUE_SCHEMA)), nullable=False),
            pa.field("version", pa.string(), nullable=False),
        ]
    )


ATTACK_SCHEMA = get_attack_schema()
