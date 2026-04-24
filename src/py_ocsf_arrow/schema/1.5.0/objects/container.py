"""Auto-generated Arrow schema for OCSF object 'container'.

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


FINGERPRINT_SCHEMA = _load_dep("fingerprint").FINGERPRINT_SCHEMA
IMAGE_SCHEMA = _load_dep("image").IMAGE_SCHEMA
KEY_VALUE_OBJECT_SCHEMA = _load_dep("key_value_object").KEY_VALUE_OBJECT_SCHEMA


def get_container_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'container'."""
    return pa.schema(
        [
            pa.field("hash", pa.struct(list(FINGERPRINT_SCHEMA)), nullable=True),
            pa.field("image", pa.struct(list(IMAGE_SCHEMA)), nullable=True),
            pa.field("labels", pa.list_(pa.string()), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("network_driver", pa.string(), nullable=True),
            pa.field("orchestrator", pa.string(), nullable=True),
            pa.field("pod_uuid", pa.string(), nullable=True),
            pa.field("runtime", pa.string(), nullable=True),
            pa.field("size", pa.int64(), nullable=True),
            pa.field("tag", pa.string(), nullable=True),
            pa.field(
                "tags",
                pa.list_(pa.struct(list(KEY_VALUE_OBJECT_SCHEMA))),
                nullable=True,
            ),
            pa.field("uid", pa.string(), nullable=True),
        ]
    )


CONTAINER_SCHEMA = get_container_schema()
