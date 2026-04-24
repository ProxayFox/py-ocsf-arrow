"""Auto-generated Arrow schema for OCSF object 'hassh'.

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


FINGERPRINT_SCHEMA = _load_dep("fingerprint").FINGERPRINT_SCHEMA


def get_hassh_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'hassh'."""
    return pa.schema(
        [
            pa.field("algorithm", pa.string(), nullable=True),
            pa.field(
                "fingerprint",
                pa.struct(list(FINGERPRINT_SCHEMA)),
                nullable=False,
            ),
        ]
    )


HASSH_SCHEMA = get_hassh_schema()
