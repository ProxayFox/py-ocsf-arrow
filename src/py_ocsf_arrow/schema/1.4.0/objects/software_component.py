"""Auto-generated Arrow schema for OCSF object 'software_component'.

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


FINGERPRINT_SCHEMA = _load_dep("fingerprint").FINGERPRINT_SCHEMA


def get_software_component_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'software_component'."""
    return pa.schema(
        [
            pa.field("author", pa.string(), nullable=True),
            pa.field("hash", pa.struct(list(FINGERPRINT_SCHEMA)), nullable=True),
            pa.field("license", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=False),
            pa.field("purl", pa.string(), nullable=True),
            pa.field("related_component", pa.string(), nullable=True),
            pa.field("relationship", pa.string(), nullable=True),
            pa.field("relationship_id", pa.int32(), nullable=True),
            pa.field("type", pa.string(), nullable=True),
            pa.field("type_id", pa.int32(), nullable=True),
            pa.field("version", pa.string(), nullable=False),
        ]
    )


SOFTWARE_COMPONENT_SCHEMA = get_software_component_schema()
