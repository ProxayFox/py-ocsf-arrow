"""Auto-generated Arrow schema for OCSF object 'certificate'.

OCSF version 1.6.0.
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
SAN_SCHEMA = _load_dep("san").SAN_SCHEMA


def get_certificate_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'certificate'."""
    return pa.schema(
        [
            pa.field("created_time", pa.int64(), nullable=True),
            pa.field("created_time_dt", pa.string(), nullable=True),
            pa.field("expiration_time", pa.int64(), nullable=True),
            pa.field("expiration_time_dt", pa.string(), nullable=True),
            pa.field(
                "fingerprints",
                pa.list_(pa.struct(list(FINGERPRINT_SCHEMA))),
                nullable=True,
            ),
            pa.field("is_self_signed", pa.bool8(), nullable=True),
            pa.field("issuer", pa.string(), nullable=False),
            pa.field("sans", pa.list_(pa.struct(list(SAN_SCHEMA))), nullable=True),
            pa.field("serial_number", pa.string(), nullable=False),
            pa.field("subject", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("version", pa.string(), nullable=True),
        ]
    )


CERTIFICATE_SCHEMA = get_certificate_schema()
