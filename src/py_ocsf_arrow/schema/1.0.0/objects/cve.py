"""Auto-generated Arrow schema for OCSF object 'cve'.

OCSF version 1.0.0.
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


CVSS_SCHEMA = _load_dep("cvss").CVSS_SCHEMA
PRODUCT_SCHEMA = _load_dep("product").PRODUCT_SCHEMA


def get_cve_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'cve'."""
    return pa.schema(
        [
            pa.field("created_time", pa.int64(), nullable=True),
            pa.field("created_time_dt", pa.string(), nullable=True),
            pa.field("cvss", pa.struct(list(CVSS_SCHEMA)), nullable=True),
            pa.field("cwe_uid", pa.string(), nullable=True),
            pa.field("cwe_url", pa.string(), nullable=True),
            pa.field("modified_time", pa.int64(), nullable=True),
            pa.field("modified_time_dt", pa.string(), nullable=True),
            pa.field("product", pa.struct(list(PRODUCT_SCHEMA)), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=False),
        ]
    )


CVE_SCHEMA = get_cve_schema()
