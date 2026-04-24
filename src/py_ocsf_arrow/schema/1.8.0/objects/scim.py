"""Auto-generated Arrow schema for OCSF object 'scim'.

Generated from version 1.8.0 at 2026-04-24T03:47:42+00:00.
"""

import pyarrow as pa


def get_scim_schema() -> pa.Schema:
    """Return the Arrow schema for OCSF object 'scim'."""
    return pa.schema(
        [
            pa.field("auth_protocol", pa.string(), nullable=True),
            pa.field("auth_protocol_id", pa.int32(), nullable=True),
            pa.field("created_time", pa.int64(), nullable=True),
            pa.field("created_time_dt", pa.string(), nullable=True),
            pa.field("error_message", pa.string(), nullable=True),
            pa.field("is_group_provisioning_enabled", pa.bool8(), nullable=True),
            pa.field("is_user_provisioning_enabled", pa.bool8(), nullable=True),
            pa.field("last_run_time", pa.int64(), nullable=True),
            pa.field("last_run_time_dt", pa.string(), nullable=True),
            pa.field("modified_time", pa.int64(), nullable=True),
            pa.field("modified_time_dt", pa.string(), nullable=True),
            pa.field("name", pa.string(), nullable=True),
            pa.field("protocol_name", pa.string(), nullable=True),
            pa.field("rate_limit", pa.int32(), nullable=True),
            pa.field("scim_group_schema", pa.string(), nullable=True),
            pa.field("scim_user_schema", pa.string(), nullable=True),
            pa.field("state", pa.string(), nullable=True),
            pa.field("state_id", pa.int32(), nullable=True),
            pa.field("uid", pa.string(), nullable=True),
            pa.field("uid_alt", pa.string(), nullable=True),
            pa.field("url_string", pa.string(), nullable=True),
            pa.field("vendor_name", pa.string(), nullable=True),
            pa.field("version", pa.string(), nullable=True),
        ]
    )


SCIM_SCHEMA = get_scim_schema()
