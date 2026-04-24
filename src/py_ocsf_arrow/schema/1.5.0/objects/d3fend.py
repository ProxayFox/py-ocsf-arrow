"""Auto-generated Arrow schema for OCSF object 'd3fend'.

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


D3F_TACTIC_SCHEMA = _load_dep("d3f_tactic").D3F_TACTIC_SCHEMA
D3F_TECHNIQUE_SCHEMA = _load_dep("d3f_technique").D3F_TECHNIQUE_SCHEMA


def get_d3fend_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'd3fend'."""
    return pa.schema(
        [
            pa.field("d3f_tactic", pa.struct(list(D3F_TACTIC_SCHEMA)), nullable=True),
            pa.field(
                "d3f_technique",
                pa.struct(list(D3F_TECHNIQUE_SCHEMA)),
                nullable=True,
            ),
            pa.field("version", pa.string(), nullable=True),
        ]
    )


D3FEND_SCHEMA = get_d3fend_schema()
