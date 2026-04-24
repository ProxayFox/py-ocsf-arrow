"""Auto-generated Arrow schema for OCSF object 'web_resource'.

OCSF version 1.2.0.
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


def get_web_resource_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'web_resource'."""
    return pa.schema(
        [
            pa.field("data", pa.string(), nullable=True),
            pa.field(
                "data_classification",
                pa.struct(list(DATA_CLASSIFICATION_SCHEMA)),
                nullable=True,
            ),
            pa.field("desc", pa.string(), nullable=True),
            pa.field("labels", pa.list_(pa.string()), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("url_string", pa.string(), nullable=True),
        ]
    )


WEB_RESOURCE_SCHEMA = get_web_resource_schema()
