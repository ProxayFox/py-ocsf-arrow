# `TypeMapper`

`TypeMapper` maps OCSF scalar and derived types to `pyarrow` types.

## Create a mapper

```python
from py_ocsf_arrow import TypeMapper

mapper = TypeMapper.init(version="default")
```

The computed mapping is available through the cached `OCSF_TO_ARROW` property.

```python
mapping = mapper.OCSF_TO_ARROW
```

## Base mappings

The current built-in base mappings are:

| OCSF type | Arrow type |
| --- | --- |
| `boolean_t` | `pa.bool8()` |
| `float_t` | `pa.float32()` |
| `integer_t` | `pa.int32()` |
| `json_t` | `pa.string()` |
| `long_t` | `pa.int64()` |
| `string_t` | `pa.string()` |

## Derived type handling

The OCSF schema defines many derived types in terms of those base types. `TypeMapper` loads the current schema version and copies the matching Arrow type for each derived type.

If the upstream schema introduces a derived type with an unknown base type, `TypeMapper` raises `TypeMappingError` rather than silently guessing.

## Notes

- Mapping is version-aware.
- Results are cached per instance.
- Object types are **not** handled here; object expansion belongs to `SchemaGenerator`.

## Example

```python
from py_ocsf_arrow import TypeMapper

mapper = TypeMapper.init(version="1.8.0")
assert mapper.OCSF_TO_ARROW["severity_id"]
```
