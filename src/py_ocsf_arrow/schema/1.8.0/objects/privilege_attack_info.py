"""Auto-generated Arrow schema for OCSF object 'privilege_attack_info'.

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


ATTACK_SCHEMA = _load_dep("attack").ATTACK_SCHEMA
PRIVILEGE_INFO_SCHEMA = _load_dep("privilege_info").PRIVILEGE_INFO_SCHEMA


def get_privilege_attack_info_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'privilege_attack_info'."""
    return pa.schema(
        [
            pa.field("attack", pa.struct(list(ATTACK_SCHEMA)), nullable=False),
            pa.field(
                "privilege_info_list",
                pa.list_(pa.struct(list(PRIVILEGE_INFO_SCHEMA))),
                nullable=False,
            ),
        ]
    )


PRIVILEGE_ATTACK_INFO_SCHEMA = get_privilege_attack_info_schema()
