"""Auto-generated Arrow schema for OCSF object 'database'.

OCSF version 1.7.0.
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


DATA_CLASSIFICATION_SCHEMA = _load_dep("data_classification").DATA_CLASSIFICATION_SCHEMA
GROUP_SCHEMA = _load_dep("group").GROUP_SCHEMA


def get_database_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'database'."""
    return pa.schema(
        [
            pa.field("created_time", pa.int64(), nullable=True),
            pa.field("created_time_dt", pa.string(), nullable=True),
            pa.field(
                "data_classification",
                pa.struct(list(DATA_CLASSIFICATION_SCHEMA)),
                nullable=True,
            ),
            pa.field(
                "data_classifications",
                pa.list_(pa.struct(list(DATA_CLASSIFICATION_SCHEMA))),
                nullable=True,
            ),
            pa.field("desc", pa.string(), nullable=True),
            pa.field("groups", pa.list_(pa.struct(list(GROUP_SCHEMA))), nullable=True),
            pa.field("modified_time", pa.int64(), nullable=True),
            pa.field("modified_time_dt", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("size", pa.int64(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("type_id", pa.int32(), nullable=False),
            pa.field("uid", pa.string(), nullable=True),
        ]
    )


DATABASE_SCHEMA = get_database_schema()
