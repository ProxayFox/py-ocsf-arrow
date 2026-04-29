# Architecture

## Mission

`py-ocsf-arrow` exists to turn OCSF metadata into Arrow-native schema building blocks that are reusable, typed, and easy to integrate into larger security data pipelines.

## Workspace packages

The repository is a `uv` workspace containing three packages:

- **`py-ocsf-arrow`** (`py_ocsf_arrow`) — the core library for Arrow-native OCSF primitives.
- **`py-ocsf-clickhouse`** (`py_ocsf_clickhouse`) — ClickHouse backend, depends on the core Arrow package. Currently a scaffold.
- **`py-ocsf-postgresql`** (`py_ocsf_postgresql`) — PostgreSQL backend, depends on the core Arrow package. Currently a scaffold.

Backend packages import Arrow primitives (e.g. `SchemaGenerator`, `TypeMapper`) from `py_ocsf_arrow` through a workspace dependency. They do not duplicate core logic.

## Current implemented layers

### `OCSFArrow`

Shared base for loading OCSF schemas, resolving versions, and filtering extension/profile attributes.

### `TypeMapper`

Maps OCSF scalar and derived types to Arrow scalar types.

### `SchemaGenerator`

Builds runtime `pyarrow.Schema` objects for classes and objects, including nested struct expansion.

### `generate_schema_module.py`

Writes version-isolated Python schema modules to `src/py_ocsf_arrow/schema/<version>/...`.

### Promotion analysis and transform pipeline

The repository also includes an opt-in promotion-analysis workflow that:

1. scores OCSF objects for standalone-table suitability
2. emits operator-facing summary, JSON, or CSV reports
3. can post-process generated class schemas to replace promoted embedded objects
  with foreign-key fields and emit standalone promoted-object schemas

This workflow does not change the default schema view. Base-only runtime loading
and generated schema modules remain the default behavior unless an operator runs
the analysis/transform tooling explicitly.

## Version isolation

Generated schema files are isolated by OCSF version:

```text
schema/
  1.0.0/
  1.1.0/
  1.8.0/
```

Each version contains its own:

- `objects/`
- `categories/`

This prevents a schema generated from one OCSF release from accidentally importing object definitions from another.

## Why generated imports use `importlib`

Two naming constraints make ordinary imports awkward:

1. version directories contain dots, for example `1.8.0`
2. generated class files begin with numeric UIDs, for example `2002_vulnerability_finding.py`

Because of that, both the generated loader packages and the generated schema files use `importlib.util.spec_from_file_location` instead of ordinary dotted imports.

## Boundaries

### In scope today

- OCSF schema loading
- Arrow type mapping
- runtime schema generation
- generated versioned schema modules
- opt-in promotion analysis and transform reporting

### Out of scope today

- ClickHouse DDL generation (package scaffolded, implementation pending)
- PostgreSQL DDL generation (package scaffolded, implementation pending)
- provider-specific transforms
- API clients for vendor data sources
- batch builder/container APIs
- a polished end-user ingestion workflow

Those remain valid design targets, but they should be documented as roadmap items rather than implied current features.
