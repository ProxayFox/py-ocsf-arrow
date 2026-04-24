# Getting started

## Current scope

`py-ocsf-arrow` is currently focused on schema work:

- `OCSFArrow` loads and filters OCSF schema metadata
- `TypeMapper` maps OCSF scalar and derived types to `pyarrow`
- `SchemaGenerator` builds `pyarrow.Schema` objects at runtime
- `scripts/generate_schema_module.py` writes versioned Python schema modules to disk

It is **not yet** a full end-to-end ingestion or validation framework.

## Prerequisites

- Python 3.14+
- [`uv`](https://docs.astral.sh/uv/)
- network access the first time OCSF schemas are fetched, unless the cache is already warm

## Install dependencies

For local development plus docs tooling:

```bash
uv sync --group dev --extra docs
```

If you only need the runtime dependencies:

```bash
uv sync
```

## Run the placeholder entry point

The repository still includes a thin `main.py` launcher:

```bash
uv run python main.py
```

For most real work, you will use either the runtime Python API or the schema generator script instead.

## Build schemas at runtime

```python
from py_ocsf_arrow import SchemaGenerator

generator = SchemaGenerator.init(version="default")

cve_schema = generator.build_object_schema("cve")
print(cve_schema)

vulnerability_schema = generator.build_class_schema("vulnerability_finding")
print(vulnerability_schema)
```

## Build the docs locally

```bash
just docs-build
just docs-serve
```

`docs-build` runs MkDocs in strict mode, so broken links and similar issues fail fast instead of sneaking into later CI.

## Where to go next

- [Schema generation](schema-generation.md)
- [Schema loading](schema-loading.md)
- [OCSFArrow API](api/ocsf-arrow.md)
