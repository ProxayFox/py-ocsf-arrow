"""Auto-generated Arrow schema for OCSF object 'cvss'.

Generated from version 1.5.0 at 2026-04-24T03:47:41+00:00.
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


METRIC_SCHEMA = _load_dep("metric").METRIC_SCHEMA


def get_cvss_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'cvss'."""
    return pa.schema(
        [
            pa.field("base_score", pa.float32(), nullable=False),
            pa.field("depth", pa.string(), nullable=True),
            pa.field(
                "metrics", pa.list_(pa.struct(list(METRIC_SCHEMA))), nullable=True
            ),
            pa.field("overall_score", pa.float32(), nullable=True),
            pa.field("severity", pa.string(), nullable=True),
            pa.field("vector_string", pa.string(), nullable=True),
            pa.field("vendor_name", pa.string(), nullable=True),
            pa.field("version", pa.string(), nullable=False),
        ]
    )


CVSS_SCHEMA = get_cvss_schema()
