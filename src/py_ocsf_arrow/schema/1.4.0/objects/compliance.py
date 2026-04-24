"""Auto-generated Arrow schema for OCSF object 'compliance'.

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


KB_ARTICLE_SCHEMA = _load_dep("kb_article").KB_ARTICLE_SCHEMA
KEY_VALUE_OBJECT_SCHEMA = _load_dep("key_value_object").KEY_VALUE_OBJECT_SCHEMA


def get_compliance_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'compliance'."""
    return pa.schema(
        [
            pa.field(
                "compliance_references",
                pa.list_(pa.struct(list(KB_ARTICLE_SCHEMA))),
                nullable=True,
            ),
            pa.field(
                "compliance_standards",
                pa.list_(pa.struct(list(KB_ARTICLE_SCHEMA))),
                nullable=True,
            ),
            pa.field("control", pa.string(), nullable=True),
            pa.field(
                "control_parameters",
                pa.list_(pa.struct(list(KEY_VALUE_OBJECT_SCHEMA))),
                nullable=True,
            ),
            pa.field("requirements", pa.list_(pa.string()), nullable=True),
            pa.field("standards", pa.list_(pa.string()), nullable=False),
            pa.field("status", pa.string(), nullable=True),
            pa.field("status_code", pa.string(), nullable=True),
            pa.field("status_detail", pa.string(), nullable=True),
            pa.field("status_details", pa.list_(pa.string()), nullable=True),
            pa.field("status_id", pa.int32(), nullable=True),
        ]
    )


COMPLIANCE_SCHEMA = get_compliance_schema()
