"""Auto-generated Arrow schema for OCSF object 'cloud'.

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


ACCOUNT_SCHEMA = _load_dep("account").ACCOUNT_SCHEMA
ORGANIZATION_SCHEMA = _load_dep("organization").ORGANIZATION_SCHEMA


def get_cloud_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'cloud'."""
    return pa.schema(
        [
            pa.field("account", pa.struct(list(ACCOUNT_SCHEMA)), nullable=True),
            pa.field("org", pa.struct(list(ORGANIZATION_SCHEMA)), nullable=True),
            pa.field("project_uid", pa.string(), nullable=True),
            pa.field("provider", pa.string(), nullable=False),
            pa.field("region", pa.string(), nullable=True),
            pa.field("zone", pa.string(), nullable=True),
        ]
    )


CLOUD_SCHEMA = get_cloud_schema()
