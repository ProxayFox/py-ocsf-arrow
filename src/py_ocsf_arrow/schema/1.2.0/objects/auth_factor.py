"""Auto-generated Arrow schema for OCSF object 'auth_factor'.

OCSF version 1.2.0.
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


DEVICE_SCHEMA = _load_dep("device").DEVICE_SCHEMA


def get_auth_factor_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'auth_factor'."""
    return pa.schema(
        [
            pa.field("device", pa.struct(list(DEVICE_SCHEMA)), nullable=True),
            pa.field("email_addr", pa.string(), nullable=True),
            pa.field("factor_type", pa.string(), nullable=True),
            pa.field("factor_type_id", pa.int32(), nullable=False),
            pa.field("is_hotp", pa.bool8(), nullable=True),
            pa.field("is_totp", pa.bool8(), nullable=True),
            pa.field("phone_number", pa.string(), nullable=True),
            pa.field("provider", pa.string(), nullable=True),
            pa.field("security_questions", pa.list_(pa.string()), nullable=True),
        ]
    )


AUTH_FACTOR_SCHEMA = get_auth_factor_schema()
