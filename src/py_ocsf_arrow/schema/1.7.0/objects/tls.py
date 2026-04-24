"""Auto-generated Arrow schema for OCSF object 'tls'.

Generated from version 1.7.0 at 2026-04-24T03:47:42+00:00.
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
SAN_SCHEMA = _load_dep("san").SAN_SCHEMA
TLS_EXTENSION_SCHEMA = _load_dep("tls_extension").TLS_EXTENSION_SCHEMA


def get_tls_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'tls'."""
    return pa.schema(
        [
            pa.field("alert", pa.int32(), nullable=True),
            pa.field("certificate", pa.struct(list(CERTIFICATE_SCHEMA)), nullable=True),
            pa.field("certificate_chain", pa.list_(pa.string()), nullable=True),
            pa.field("cipher", pa.string(), nullable=True),
            pa.field("client_ciphers", pa.list_(pa.string()), nullable=True),
            pa.field(
                "extension_list",
                pa.list_(pa.struct(list(TLS_EXTENSION_SCHEMA))),
                nullable=True,
            ),
            pa.field("handshake_dur", pa.int32(), nullable=True),
            pa.field("ja3_hash", pa.struct(list(FINGERPRINT_SCHEMA)), nullable=True),
            pa.field("ja3s_hash", pa.struct(list(FINGERPRINT_SCHEMA)), nullable=True),
            pa.field("key_length", pa.int32(), nullable=True),
            pa.field("sans", pa.list_(pa.struct(list(SAN_SCHEMA))), nullable=True),
            pa.field("server_ciphers", pa.list_(pa.string()), nullable=True),
            pa.field("sni", pa.string(), nullable=True),
            pa.field(
                "tls_extension_list",
                pa.list_(pa.struct(list(TLS_EXTENSION_SCHEMA))),
                nullable=True,
            ),
            pa.field("version", pa.string(), nullable=False),
        ]
    )


TLS_SCHEMA = get_tls_schema()
