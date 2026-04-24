"""Auto-generated Arrow schema for OCSF object 'resource_details'.

Generated from version 1.1.0 at 2026-04-24T03:47:40+00:00.
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


USER_SCHEMA = _load_dep("user").USER_SCHEMA


def get_resource_details_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'resource_details'."""
    return pa.schema(
        [
            pa.field("cloud_partition", pa.string(), nullable=True),
            pa.field("criticality", pa.string(), nullable=True),
            pa.field("data", pa.string(), nullable=True),
            pa.field("labels", pa.list_(pa.string()), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("namespace", pa.string(), nullable=True),
            pa.field("owner", pa.struct(list(USER_SCHEMA)), nullable=True),
            pa.field("region", pa.string(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("version", pa.string(), nullable=True),
        ]
    )


RESOURCE_DETAILS_SCHEMA = get_resource_details_schema()
