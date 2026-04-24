"""Auto-generated Arrow schema for OCSF object 'anomaly_analysis'.

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


ANALYSIS_TARGET_SCHEMA = _load_dep("analysis_target").ANALYSIS_TARGET_SCHEMA
ANOMALY_SCHEMA = _load_dep("anomaly").ANOMALY_SCHEMA
BASELINE_SCHEMA = _load_dep("baseline").BASELINE_SCHEMA


def get_anomaly_analysis_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'anomaly_analysis'."""
    return pa.schema(
        [
            pa.field(
                "analysis_targets",
                pa.list_(pa.struct(list(ANALYSIS_TARGET_SCHEMA))),
                nullable=False,
            ),
            pa.field(
                "anomalies", pa.list_(pa.struct(list(ANOMALY_SCHEMA))), nullable=False
            ),
            pa.field(
                "baselines", pa.list_(pa.struct(list(BASELINE_SCHEMA))), nullable=True
            ),
        ]
    )


ANOMALY_ANALYSIS_SCHEMA = get_anomaly_analysis_schema()
