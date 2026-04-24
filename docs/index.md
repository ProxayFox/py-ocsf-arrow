# py-ocsf-arrow

`py-ocsf-arrow` is the Python seed of an OCSF Arrow ecosystem: code that turns OCSF schema metadata into reusable Apache Arrow schemas and versioned Python schema modules.

This project is still **pre-alpha**, but it already supports a useful slice of the eventual design:

- loading OCSF schemas from `ocsf-lib`
- mapping OCSF scalar types to `pyarrow` types
- resolving OCSF object fields into nested Arrow structs
- generating importable Python schema modules by OCSF version and category

## What is implemented today

### Runtime schema generation

You can build `pyarrow.Schema` objects directly from OCSF metadata:

```python
from py_ocsf_arrow import SchemaGenerator

generator = SchemaGenerator.init(version="default")

cve_schema = generator.build_object_schema("cve")
vulnerability_schema = generator.build_class_schema("vulnerability_finding")
```

### Versioned generated schema modules

You can also materialize schemas as Python files under `src/py_ocsf_arrow/schema/<version>/...`:

```bash
just generate
```

That produces version-isolated schema trees such as:

```text
src/py_ocsf_arrow/schema/
  1.8.0/
    objects/
    categories/
      2_findings/
        2002_vulnerability_finding.py
```

## Start here

- [Getting started](getting-started.md) — install dependencies and run the project locally
- [Schema generation](schema-generation.md) — generate versioned schema modules
- [Schema loading](schema-loading.md) — load generated schemas with `importlib`
- [SchemaGenerator API](api/schema-generator.md) — direct runtime API
- [Architecture](architecture.md) — project boundaries and design decisions

## What is not implemented yet

The following are still planned, not shipped:

- Arrow-backed builder/container APIs
- provider-specific transform packages
- end-to-end provider ingestion examples
- a polished, stable public API surface

See [Project status](status.md) for the sharper edges and the honest roadmap.
