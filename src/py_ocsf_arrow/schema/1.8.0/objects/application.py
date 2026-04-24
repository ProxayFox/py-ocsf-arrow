"""Auto-generated Arrow schema for OCSF object 'application'.

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


GRAPH_SCHEMA = _load_dep("graph").GRAPH_SCHEMA
GROUP_SCHEMA = _load_dep("group").GROUP_SCHEMA
KEY_VALUE_OBJECT_SCHEMA = _load_dep("key_value_object").KEY_VALUE_OBJECT_SCHEMA
SBOM_SCHEMA = _load_dep("sbom").SBOM_SCHEMA
URL_SCHEMA = _load_dep("url").URL_SCHEMA
USER_SCHEMA = _load_dep("user").USER_SCHEMA


def get_application_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'application'."""
    return pa.schema(
        [
            pa.field("criticality", pa.string(), nullable=True),
            pa.field("data", pa.string(), nullable=True),
            pa.field("desc", pa.string(), nullable=True),
            pa.field("group", pa.struct(list(GROUP_SCHEMA)), nullable=True),
            pa.field("hostname", pa.string(), nullable=True),
            pa.field("labels", pa.list_(pa.string()), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("owner", pa.struct(list(USER_SCHEMA)), nullable=True),
            pa.field("region", pa.string(), nullable=True),
            pa.field(
                "resource_relationship",
                pa.struct(list(GRAPH_SCHEMA)),
                nullable=True,
            ),
            pa.field("risk_level", pa.string(), nullable=True),
            pa.field("risk_level_id", pa.int32(), nullable=True),
            pa.field("risk_score", pa.int32(), nullable=True),
            pa.field("sbom", pa.struct(list(SBOM_SCHEMA)), nullable=True),
            pa.field(
                "tags",
                pa.list_(pa.struct(list(KEY_VALUE_OBJECT_SCHEMA))),
                nullable=True,
            ),
            pa.field("type", pa.string(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("uid_alt", pa.string(), nullable=True),
            pa.field("url", pa.struct(list(URL_SCHEMA)), nullable=True),
            pa.field("version", pa.string(), nullable=True),
        ]
    )


APPLICATION_SCHEMA = get_application_schema()
