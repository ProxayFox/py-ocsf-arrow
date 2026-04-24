"""Auto-generated Arrow schema for OCSF object 'identity_activity_metrics'.

Generated from version 1.6.0 at 2026-04-24T03:47:41+00:00.
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


PROGRAMMATIC_CREDENTIAL_SCHEMA = _load_dep(
    "programmatic_credential"
).PROGRAMMATIC_CREDENTIAL_SCHEMA


def get_identity_activity_metrics_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'identity_activity_metrics'."""
    return pa.schema(
        [
            pa.field("first_seen_time", pa.int64(), nullable=True),
            pa.field("first_seen_time_dt", pa.string(), nullable=True),
            pa.field("last_authentication_time", pa.int64(), nullable=True),
            pa.field("last_authentication_time_dt", pa.string(), nullable=True),
            pa.field("last_seen_time", pa.int64(), nullable=True),
            pa.field("last_seen_time_dt", pa.string(), nullable=True),
            pa.field("password_last_used_time", pa.int64(), nullable=True),
            pa.field("password_last_used_time_dt", pa.string(), nullable=True),
            pa.field(
                "programmatic_credentials",
                pa.list_(pa.struct(list(PROGRAMMATIC_CREDENTIAL_SCHEMA))),
                nullable=True,
            ),
        ]
    )


IDENTITY_ACTIVITY_METRICS_SCHEMA = get_identity_activity_metrics_schema()
