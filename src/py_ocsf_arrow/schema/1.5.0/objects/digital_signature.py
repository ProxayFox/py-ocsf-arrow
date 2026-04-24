"""Auto-generated Arrow schema for OCSF object 'digital_signature'.

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


CERTIFICATE_SCHEMA = _load_dep("certificate").CERTIFICATE_SCHEMA
FINGERPRINT_SCHEMA = _load_dep("fingerprint").FINGERPRINT_SCHEMA


def get_digital_signature_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'digital_signature'."""
    return pa.schema(
        [
            pa.field("algorithm", pa.string(), nullable=True),
            pa.field("algorithm_id", pa.int32(), nullable=False),
            pa.field("certificate", pa.struct(list(CERTIFICATE_SCHEMA)), nullable=True),
            pa.field("created_time", pa.int64(), nullable=True),
            pa.field("created_time_dt", pa.string(), nullable=True),
            pa.field("developer_uid", pa.string(), nullable=True),
            pa.field("digest", pa.struct(list(FINGERPRINT_SCHEMA)), nullable=True),
            pa.field("state", pa.string(), nullable=True),
            pa.field("state_id", pa.int32(), nullable=True),
        ]
    )


DIGITAL_SIGNATURE_SCHEMA = get_digital_signature_schema()
