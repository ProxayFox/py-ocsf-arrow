"""Auto-generated Arrow schema for OCSF object 'package'.

OCSF version 1.8.0.
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


def get_package_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'package'."""
    return pa.schema(
        [
            pa.field("architecture", pa.string(), nullable=True),
            pa.field("cpe_name", pa.string(), nullable=True),
            pa.field("epoch", pa.int32(), nullable=True),
            pa.field("hash", pa.struct(list(FINGERPRINT_SCHEMA)), nullable=True),
            pa.field("license", pa.string(), nullable=True),
            pa.field("license_url", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=False),
            pa.field("package_manager", pa.string(), nullable=True),
            pa.field("package_manager_url", pa.string(), nullable=True),
            pa.field("purl", pa.string(), nullable=True),
            pa.field("release", pa.string(), nullable=True),
            pa.field("src_url", pa.string(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("type_id", pa.int32(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("vendor_name", pa.string(), nullable=True),
            pa.field("version", pa.string(), nullable=False),
        ]
    )


PACKAGE_SCHEMA = get_package_schema()
