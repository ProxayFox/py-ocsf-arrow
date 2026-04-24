"""Auto-generated Arrow schema for OCSF object 'authentication_token'.

OCSF version 1.7.0.
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


ENCRYPTION_DETAILS_SCHEMA = _load_dep("encryption_details").ENCRYPTION_DETAILS_SCHEMA


def get_authentication_token_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'authentication_token'."""
    return pa.schema(
        [
            pa.field("created_time", pa.int64(), nullable=True),
            pa.field("created_time_dt", pa.string(), nullable=True),
            pa.field(
                "encryption_details",
                pa.struct(list(ENCRYPTION_DETAILS_SCHEMA)),
                nullable=True,
            ),
            pa.field("expiration_time", pa.int64(), nullable=True),
            pa.field("expiration_time_dt", pa.string(), nullable=True),
            pa.field("is_renewable", pa.bool8(), nullable=True),
            pa.field("kerberos_flags", pa.string(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("type_id", pa.int32(), nullable=True),
        ]
    )


AUTHENTICATION_TOKEN_SCHEMA = get_authentication_token_schema()
