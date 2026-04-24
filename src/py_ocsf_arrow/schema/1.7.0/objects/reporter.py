"""Auto-generated Arrow schema for OCSF object 'reporter'.

Generated from version 1.7.0 at 2026-04-24T03:47:42+00:00.
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


ORGANIZATION_SCHEMA = _load_dep("organization").ORGANIZATION_SCHEMA


def get_reporter_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'reporter'."""
    return pa.schema(
        [
            pa.field("hostname", pa.string(), nullable=True),
            pa.field("ip", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("org", pa.struct(list(ORGANIZATION_SCHEMA)), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
        ]
    )


REPORTER_SCHEMA = get_reporter_schema()
