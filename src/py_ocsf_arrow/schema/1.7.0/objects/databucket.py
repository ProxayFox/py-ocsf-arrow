"""Auto-generated Arrow schema for OCSF object 'databucket'.

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


AGENT_SCHEMA = _load_dep("agent").AGENT_SCHEMA
DATA_CLASSIFICATION_SCHEMA = _load_dep("data_classification").DATA_CLASSIFICATION_SCHEMA
ENCRYPTION_DETAILS_SCHEMA = _load_dep("encryption_details").ENCRYPTION_DETAILS_SCHEMA
FILE_SCHEMA = _load_dep("file").FILE_SCHEMA
GRAPH_SCHEMA = _load_dep("graph").GRAPH_SCHEMA
GROUP_SCHEMA = _load_dep("group").GROUP_SCHEMA
KEY_VALUE_OBJECT_SCHEMA = _load_dep("key_value_object").KEY_VALUE_OBJECT_SCHEMA
USER_SCHEMA = _load_dep("user").USER_SCHEMA


def get_databucket_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'databucket'."""
    return pa.schema(
        [
            pa.field(
                "agent_list",
                pa.list_(pa.struct(list(AGENT_SCHEMA))),
                nullable=True,
            ),
            pa.field("cloud_partition", pa.string(), nullable=True),
            pa.field("created_time", pa.int64(), nullable=True),
            pa.field("created_time_dt", pa.string(), nullable=True),
            pa.field("criticality", pa.string(), nullable=True),
            pa.field("data", pa.string(), nullable=True),
            pa.field(
                "data_classification",
                pa.struct(list(DATA_CLASSIFICATION_SCHEMA)),
                nullable=True,
            ),
            pa.field(
                "data_classifications",
                pa.list_(pa.struct(list(DATA_CLASSIFICATION_SCHEMA))),
                nullable=True,
            ),
            pa.field("desc", pa.string(), nullable=True),
            pa.field(
                "encryption_details",
                pa.struct(list(ENCRYPTION_DETAILS_SCHEMA)),
                nullable=True,
            ),
            pa.field("file", pa.struct(list(FILE_SCHEMA)), nullable=True),
            pa.field("group", pa.struct(list(GROUP_SCHEMA)), nullable=True),
            pa.field("groups", pa.list_(pa.struct(list(GROUP_SCHEMA))), nullable=True),
            pa.field("hostname", pa.string(), nullable=True),
            pa.field("ip", pa.string(), nullable=True),
            pa.field("is_backed_up", pa.bool8(), nullable=True),
            pa.field("is_encrypted", pa.bool8(), nullable=True),
            pa.field("is_public", pa.bool8(), nullable=True),
            pa.field("labels", pa.list_(pa.string()), nullable=True),
            pa.field("modified_time", pa.int64(), nullable=True),
            pa.field("modified_time_dt", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("namespace", pa.string(), nullable=True),
            pa.field("owner", pa.struct(list(USER_SCHEMA)), nullable=True),
            pa.field("region", pa.string(), nullable=True),
            pa.field(
                "resource_relationship",
                pa.struct(list(GRAPH_SCHEMA)),
                nullable=True,
            ),
            pa.field("size", pa.int64(), nullable=True),
            pa.field(
                "tags",
                pa.list_(pa.struct(list(KEY_VALUE_OBJECT_SCHEMA))),
                nullable=True,
            ),
            pa.field("type", pa.string(), nullable=True),
            pa.field("type_id", pa.int32(), nullable=False),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("uid_alt", pa.string(), nullable=True),
            pa.field("version", pa.string(), nullable=True),
            pa.field("zone", pa.string(), nullable=True),
        ]
    )


DATABUCKET_SCHEMA = get_databucket_schema()
