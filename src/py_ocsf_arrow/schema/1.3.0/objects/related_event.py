"""Auto-generated Arrow schema for OCSF object 'related_event'.

OCSF version 1.3.0.
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


ATTACK_SCHEMA = _load_dep("attack").ATTACK_SCHEMA
KILL_CHAIN_PHASE_SCHEMA = _load_dep("kill_chain_phase").KILL_CHAIN_PHASE_SCHEMA
OBSERVABLE_SCHEMA = _load_dep("observable").OBSERVABLE_SCHEMA


def get_related_event_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'related_event'."""
    return pa.schema(
        [
            pa.field(
                "attacks",
                pa.list_(pa.struct(list(ATTACK_SCHEMA))),
                nullable=True,
            ),
            pa.field(
                "kill_chain",
                pa.list_(pa.struct(list(KILL_CHAIN_PHASE_SCHEMA))),
                nullable=True,
            ),
            pa.field(
                "observables",
                pa.list_(pa.struct(list(OBSERVABLE_SCHEMA))),
                nullable=True,
            ),
            pa.field("product_uid", pa.string(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("type_name", pa.string(), nullable=True),
            pa.field("type_uid", pa.int64(), nullable=True),
            pa.field("uid", pa.string(), nullable=False),
        ]
    )


RELATED_EVENT_SCHEMA = get_related_event_schema()
