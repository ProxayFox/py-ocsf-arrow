"""Auto-generated Arrow schema for OCSF object 'image'.

Generated from version 1.4.0 at 2026-04-24T03:47:41+00:00.
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


KEY_VALUE_OBJECT_SCHEMA = _load_dep("key_value_object").KEY_VALUE_OBJECT_SCHEMA


def get_image_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'image'."""
    return pa.schema(
        [
            pa.field("labels", pa.list_(pa.string()), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("path", pa.string(), nullable=True),
            pa.field("tag", pa.string(), nullable=True),
            pa.field(
                "tags",
                pa.list_(pa.struct(list(KEY_VALUE_OBJECT_SCHEMA))),
                nullable=True,
            ),
            pa.field("uid", pa.string(), nullable=False),
        ]
    )


IMAGE_SCHEMA = get_image_schema()
