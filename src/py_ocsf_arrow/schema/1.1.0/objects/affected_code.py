"""Auto-generated Arrow schema for OCSF object 'affected_code'.

OCSF version 1.1.0.
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


FILE_SCHEMA = _load_dep("file").FILE_SCHEMA
REMEDIATION_SCHEMA = _load_dep("remediation").REMEDIATION_SCHEMA
USER_SCHEMA = _load_dep("user").USER_SCHEMA


def get_affected_code_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'affected_code'."""
    return pa.schema(
        [
            pa.field("end_line", pa.int32(), nullable=True),
            pa.field("file", pa.struct(list(FILE_SCHEMA)), nullable=False),
            pa.field("owner", pa.struct(list(USER_SCHEMA)), nullable=True),
            pa.field("remediation", pa.struct(list(REMEDIATION_SCHEMA)), nullable=True),
            pa.field("start_line", pa.int32(), nullable=True),
        ]
    )


AFFECTED_CODE_SCHEMA = get_affected_code_schema()
