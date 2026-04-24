"""Auto-generated Arrow schema for OCSF object 'remediation'.

Generated from version 1.3.0 at 2026-04-24T03:47:40+00:00.
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


def get_remediation_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'remediation'."""
    return pa.schema(
        [
            pa.field("desc", pa.string(), nullable=False),
            pa.field(
                "kb_article_list",
                pa.list_(pa.struct(list(KB_ARTICLE_SCHEMA))),
                nullable=True,
            ),
            pa.field("kb_articles", pa.list_(pa.string()), nullable=True),
            pa.field("references", pa.list_(pa.string()), nullable=True),
        ]
    )


REMEDIATION_SCHEMA = get_remediation_schema()
