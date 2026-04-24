"""Auto-generated Arrow schema for OCSF object 'cis_benchmark_result'.

OCSF version 1.4.0.
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


REMEDIATION_SCHEMA = _load_dep("remediation").REMEDIATION_SCHEMA
RULE_SCHEMA = _load_dep("rule").RULE_SCHEMA


def get_cis_benchmark_result_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'cis_benchmark_result'."""
    return pa.schema(
        [
            pa.field("desc", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=False),
            pa.field("remediation", pa.struct(list(REMEDIATION_SCHEMA)), nullable=True),
            pa.field("rule", pa.struct(list(RULE_SCHEMA)), nullable=True),
        ]
    )


CIS_BENCHMARK_RESULT_SCHEMA = get_cis_benchmark_result_schema()
