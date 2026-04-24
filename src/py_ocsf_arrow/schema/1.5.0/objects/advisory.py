"""Auto-generated Arrow schema for OCSF object 'advisory'.

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


CVE_SCHEMA = _load_dep("cve").CVE_SCHEMA
CWE_SCHEMA = _load_dep("cwe").CWE_SCHEMA
OS_SCHEMA = _load_dep("os").OS_SCHEMA
PRODUCT_SCHEMA = _load_dep("product").PRODUCT_SCHEMA
TIMESPAN_SCHEMA = _load_dep("timespan").TIMESPAN_SCHEMA


def get_advisory_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'advisory'."""
    return pa.schema(
        [
            pa.field("avg_timespan", pa.struct(list(TIMESPAN_SCHEMA)), nullable=True),
            pa.field("bulletin", pa.string(), nullable=True),
            pa.field("classification", pa.string(), nullable=True),
            pa.field("created_time", pa.int64(), nullable=True),
            pa.field("created_time_dt", pa.string(), nullable=True),
            pa.field("desc", pa.string(), nullable=True),
            pa.field("install_state", pa.string(), nullable=True),
            pa.field("install_state_id", pa.int32(), nullable=True),
            pa.field("is_superseded", pa.bool8(), nullable=True),
            pa.field("modified_time", pa.int64(), nullable=True),
            pa.field("modified_time_dt", pa.string(), nullable=True),
            pa.field("os", pa.struct(list(OS_SCHEMA)), nullable=True),
            pa.field("product", pa.struct(list(PRODUCT_SCHEMA)), nullable=True),
            pa.field("references", pa.list_(pa.string()), nullable=True),
            pa.field(
                "related_cves",
                pa.list_(pa.struct(list(CVE_SCHEMA))),
                nullable=True,
            ),
            pa.field(
                "related_cwes",
                pa.list_(pa.struct(list(CWE_SCHEMA))),
                nullable=True,
            ),
            pa.field("size", pa.int64(), nullable=True),
            pa.field("src_url", pa.string(), nullable=True),
            pa.field("title", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=False),
        ]
    )


ADVISORY_SCHEMA = get_advisory_schema()
