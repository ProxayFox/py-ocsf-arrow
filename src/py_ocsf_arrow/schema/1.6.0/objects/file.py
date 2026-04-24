"""Auto-generated Arrow schema for OCSF object 'file'.

OCSF version 1.6.0.
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


DATA_CLASSIFICATION_SCHEMA = _load_dep("data_classification").DATA_CLASSIFICATION_SCHEMA
DIGITAL_SIGNATURE_SCHEMA = _load_dep("digital_signature").DIGITAL_SIGNATURE_SCHEMA
ENCRYPTION_DETAILS_SCHEMA = _load_dep("encryption_details").ENCRYPTION_DETAILS_SCHEMA
FINGERPRINT_SCHEMA = _load_dep("fingerprint").FINGERPRINT_SCHEMA
KEY_VALUE_OBJECT_SCHEMA = _load_dep("key_value_object").KEY_VALUE_OBJECT_SCHEMA
OBJECT_SCHEMA = _load_dep("object").OBJECT_SCHEMA
PRODUCT_SCHEMA = _load_dep("product").PRODUCT_SCHEMA
URL_SCHEMA = _load_dep("url").URL_SCHEMA
USER_SCHEMA = _load_dep("user").USER_SCHEMA


def get_file_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'file'."""
    return pa.schema(
        [
            pa.field("accessed_time", pa.int64(), nullable=True),
            pa.field("accessed_time_dt", pa.string(), nullable=True),
            pa.field("accessor", pa.struct(list(USER_SCHEMA)), nullable=True),
            pa.field("attributes", pa.int32(), nullable=True),
            pa.field("company_name", pa.string(), nullable=True),
            pa.field("confidentiality", pa.string(), nullable=True),
            pa.field("confidentiality_id", pa.int32(), nullable=True),
            pa.field("created_time", pa.int64(), nullable=True),
            pa.field("created_time_dt", pa.string(), nullable=True),
            pa.field("creator", pa.struct(list(USER_SCHEMA)), nullable=True),
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
            pa.field("drive_type", pa.string(), nullable=True),
            pa.field("drive_type_id", pa.int32(), nullable=True),
            pa.field(
                "encryption_details",
                pa.struct(list(ENCRYPTION_DETAILS_SCHEMA)),
                nullable=True,
            ),
            pa.field("ext", pa.string(), nullable=True),
            pa.field(
                "hashes",
                pa.list_(pa.struct(list(FINGERPRINT_SCHEMA))),
                nullable=True,
            ),
            pa.field("internal_name", pa.string(), nullable=True),
            pa.field("is_deleted", pa.bool8(), nullable=True),
            pa.field("is_encrypted", pa.bool8(), nullable=True),
            pa.field("is_public", pa.bool8(), nullable=True),
            pa.field("is_readonly", pa.bool8(), nullable=True),
            pa.field("is_system", pa.bool8(), nullable=True),
            pa.field("mime_type", pa.string(), nullable=True),
            pa.field("modified_time", pa.int64(), nullable=True),
            pa.field("modified_time_dt", pa.string(), nullable=True),
            pa.field("modifier", pa.struct(list(USER_SCHEMA)), nullable=True),
            pa.field("name", pa.string(), nullable=False),
            pa.field("owner", pa.struct(list(USER_SCHEMA)), nullable=True),
            pa.field("parent_folder", pa.string(), nullable=True),
            pa.field("path", pa.string(), nullable=True),
            pa.field("product", pa.struct(list(PRODUCT_SCHEMA)), nullable=True),
            pa.field("security_descriptor", pa.string(), nullable=True),
            pa.field(
                "signature",
                pa.struct(list(DIGITAL_SIGNATURE_SCHEMA)),
                nullable=True,
            ),
            pa.field("size", pa.int64(), nullable=True),
            pa.field("storage_class", pa.string(), nullable=True),
            pa.field(
                "tags",
                pa.list_(pa.struct(list(KEY_VALUE_OBJECT_SCHEMA))),
                nullable=True,
            ),
            pa.field("type", pa.string(), nullable=True),
            pa.field("type_id", pa.int32(), nullable=False),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("uri", pa.string(), nullable=True),
            pa.field("url", pa.struct(list(URL_SCHEMA)), nullable=True),
            pa.field("version", pa.string(), nullable=True),
            pa.field("volume", pa.string(), nullable=True),
            pa.field("xattributes", pa.struct(list(OBJECT_SCHEMA)), nullable=True),
        ]
    )


FILE_SCHEMA = get_file_schema()
