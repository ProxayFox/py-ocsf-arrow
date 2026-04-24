"""Auto-generated Arrow schema for OCSF object 'check'.

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


RESOURCE_DETAILS_SCHEMA = _load_dep("resource_details").RESOURCE_DETAILS_SCHEMA


def get_check_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'check'."""
    return pa.schema(
        [
            pa.field("desc", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field(
                "resource",
                pa.struct(list(RESOURCE_DETAILS_SCHEMA)),
                nullable=True,
            ),
            pa.field("severity", pa.string(), nullable=True),
            pa.field("severity_id", pa.int32(), nullable=True),
            pa.field("standards", pa.list_(pa.string()), nullable=True),
            pa.field("status", pa.string(), nullable=True),
            pa.field("status_id", pa.int32(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("version", pa.string(), nullable=True),
        ]
    )


CHECK_SCHEMA = get_check_schema()
