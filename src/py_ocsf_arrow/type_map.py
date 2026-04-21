import pyarrow as pa

# OCSF type_name → PyArrow type
# This is the only hand-written part — everything else is generated
OCSF_TO_ARROW: dict[str, pa.DataType] = {
    "string_t": pa.string(),
    "integer_t": pa.int32(),
    "long_t": pa.int64(),
    "boolean_t": pa.bool_(),
    "float_t": pa.float64(),
    "timestamp_t": pa.timestamp("ms"),
    "json_t": pa.string(),  # JSON stored as string in Arrow
}
