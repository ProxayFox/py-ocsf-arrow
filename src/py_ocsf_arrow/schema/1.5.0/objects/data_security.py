"""Auto-generated Arrow schema for OCSF object 'data_security'.

Generated from version 1.5.0 at 2026-04-24T03:47:41+00:00.
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


CLASSIFIER_DETAILS_SCHEMA = _load_dep("classifier_details").CLASSIFIER_DETAILS_SCHEMA
DISCOVERY_DETAILS_SCHEMA = _load_dep("discovery_details").DISCOVERY_DETAILS_SCHEMA


def get_data_security_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'data_security'."""
    return pa.schema(
        [
            pa.field("category", pa.string(), nullable=True),
            pa.field("category_id", pa.int32(), nullable=True),
            pa.field(
                "classifier_details",
                pa.struct(list(CLASSIFIER_DETAILS_SCHEMA)),
                nullable=True,
            ),
            pa.field("confidentiality", pa.string(), nullable=True),
            pa.field("confidentiality_id", pa.int32(), nullable=True),
            pa.field("data_lifecycle_state", pa.string(), nullable=True),
            pa.field("data_lifecycle_state_id", pa.int32(), nullable=True),
            pa.field("detection_pattern", pa.string(), nullable=True),
            pa.field("detection_system", pa.string(), nullable=True),
            pa.field("detection_system_id", pa.int32(), nullable=True),
            pa.field(
                "discovery_details",
                pa.list_(pa.struct(list(DISCOVERY_DETAILS_SCHEMA))),
                nullable=True,
            ),
            pa.field("pattern_match", pa.string(), nullable=True),
            pa.field("size", pa.int64(), nullable=True),
            pa.field("status", pa.string(), nullable=True),
            pa.field("status_details", pa.list_(pa.string()), nullable=True),
            pa.field("status_id", pa.int32(), nullable=True),
            pa.field("total", pa.int32(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
        ]
    )


DATA_SECURITY_SCHEMA = get_data_security_schema()
