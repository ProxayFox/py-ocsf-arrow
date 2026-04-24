# `SchemaGenerator`

`SchemaGenerator` builds `pyarrow.Schema` objects directly from OCSF metadata.

## Create a generator

```python
from py_ocsf_arrow import SchemaGenerator

generator = SchemaGenerator.init(version="default")
```

`SchemaGenerator` inherits from `OCSFArrow`, so it shares the same version, cache, extension, and profile handling.

## Build a class schema

```python
schema = generator.build_class_schema("vulnerability_finding")
```

This returns a `pyarrow.Schema` for the requested OCSF class.

## Build an object schema

```python
schema = generator.build_object_schema("cve")
```

This returns a `pyarrow.Schema` for an OCSF object definition.

## Nested object resolution

A key behavior of the current implementation is that OCSF object-typed fields are resolved into nested Arrow structs rather than flattened into strings when the object definition is available.

For example, the tests verify that `cve.epss` becomes a struct whose fields match the standalone `epss` object schema.

```python
cve_schema = generator.build_object_schema("cve")
epss_field = cve_schema.field("epss")
```

The resulting `epss_field.type` is a struct type.

## Array handling

If an OCSF attribute is marked as an array, `SchemaGenerator` wraps the resolved Arrow type in `pa.list_(...)`.

## Cycle protection

Object graphs can contain self-references or longer cycles. The generator protects against import and recursion loops by falling back to `pa.string()` when it detects a cycle during nested object expansion.

That fallback is intentionally conservative: correctness and termination win over speculative recursion.

## Relationship to generated schema files

`SchemaGenerator` is the runtime API.

`scripts/generate_schema_module.py` is a code generator that uses the same schema metadata to write Python files to disk. Use the runtime API when you want schemas immediately in memory; use generated files when you want checked-in, versioned artifacts.
