"""Auto-generated Arrow schema for OCSF object 'product'.

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


DATA_CLASSIFICATION_SCHEMA = _load_dep("data_classification").DATA_CLASSIFICATION_SCHEMA
FEATURE_SCHEMA = _load_dep("feature").FEATURE_SCHEMA


def get_product_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'product'."""
    return pa.schema(
        [
            pa.field("cpe_name", pa.string(), nullable=True),
            pa.field(
                "data_classification",
                pa.struct(list(DATA_CLASSIFICATION_SCHEMA)),
                nullable=True,
            ),
            pa.field("feature", pa.struct(list(FEATURE_SCHEMA)), nullable=True),
            pa.field("lang", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("path", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("url_string", pa.string(), nullable=True),
            pa.field("vendor_name", pa.string(), nullable=False),
            pa.field("version", pa.string(), nullable=True),
        ]
    )


PRODUCT_SCHEMA = get_product_schema()
