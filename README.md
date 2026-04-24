# py-ocsf-arrow

Python seed for an OCSF Arrow ecosystem: reusable libraries that turn security-provider data into OCSF-compliant Apache Arrow tables.

> [!WARNING]
> This repository is still pre-alpha. The architecture and API examples below describe the intended direction; the current implementation is mostly scaffolding with a placeholder launcher.

## Why this project exists

Security reporting pipelines often grow inside a monolith as one-off transformation code. That usually works right up until it very much does not.

The goal of `py-ocsf-arrow` is to extract that logic into reusable Python packages that:

- normalize provider data into OCSF-compliant tables
- standardize on [OCSF](https://schema.ocsf.io/) as the contract layer
- use [Apache Arrow](https://arrow.apache.org/) as the schema and exchange format
- prefer columnar [Polars](https://pola.rs/) transforms over row-by-row validation
- keep provider-specific mapping logic separate from the core OCSF/Arrow primitives

## Planned architecture

```text
Raw provider data (Microsoft Defender, CrowdStrike, Tenable, ...)
  ↓
Provider client package
  ↓
Polars DataFrame
  ↓
Provider-specific transforms (`ocsf-transforms`)
  ↓
OCSF-mapped DataFrame
  ↓
Arrow-native builder/schema layer (`ocsf-arrow`)
  ↓
Validated `pyarrow.Table`
```

## Package boundaries

### `ocsf-arrow`

The core layer for Arrow-native OCSF primitives.

- OCSF `IntEnum` code tables and lookup helpers
- Arrow schemas for OCSF classes such as Vulnerability Finding and Detection Finding
- builder or container APIs that validate batches and emit `pyarrow.Table` or `polars.DataFrame`

### `ocsf-transforms`

The provider-mapping layer that sits above the core library.

- provider-specific rename maps and enum mappings
- columnar Polars transformations
- end-to-end fixtures that prove a provider payload can become a valid OCSF table

### Provider clients

Separate packages for HTTP/API access.

- fetch raw provider data
- handle authentication and pagination
- stay decoupled from OCSF and Arrow internals

## Design principles

| Decision | Direction | Why |
| --- | --- | --- |
| Schema contract | Arrow schemas | Columnar, explicit, and interoperable |
| Validation model | Arrow casting over per-row models | Better fit for large batches and clearer schema failures |
| Transform engine | Polars | Columnar operations with strong Arrow interop |
| Enum strategy | `IntEnum` lookup tables | Clearer OCSF code handling without inventing a custom system |
| Project split | Core vs transforms vs clients | Keeps responsibilities small and extractable |
| Performance path | Python first, Rust later | Prove the API before optimizing the engine room |

## Current repository status

Today this repository is the seed project, not the finished library. At the moment it contains:

- a placeholder `main.py` that prints a greeting
- a minimal `pyproject.toml`
- empty `src/` and `test/` directories
- development scaffolding via `.devcontainer/` and `flake.nix`
- no implementation modules or runtime dependencies yet

That means the following are still planned work:

- [ ] OCSF enum tables and lookup helpers
- [ ] Arrow schemas for key OCSF classes
- [ ] batch builder or container APIs
- [ ] provider-specific transforms, starting with Defender vulnerability mappings
- [ ] tests, fixtures, and usage examples

## Repository layout today

```text
.
├── .devcontainer/          # VS Code dev container and Dockerfile
├── .github/                # Copilot and repository automation files
├── src/                    # Reserved for future package code
├── test/                   # Placeholder test directory
├── flake.nix               # Nix development shell
├── main.py                 # Placeholder launcher
├── pyproject.toml          # Project metadata
└── README.md
```

## Local development

### Dev container

The dev container is based on `mcr.microsoft.com/devcontainers/python:3-3.14-trixie` and installs `uv` plus editor tooling.

### With `uv`

```bash
uv sync
uv run python main.py
```

### Generate callable schema modules

Use the generator script to materialize OCSF class schemas as importable Python code, organized by category:

```bash
uv run scripts/generate_schema_module.py
```

By default, this generates all OCSF classes into:

- `src/py_ocsf_arrow/schema/objects/` — shared object schema files
- `src/py_ocsf_arrow/schema/categories/<uid>_<name>/` — class files grouped by OCSF category

You can generate a single class instead:

```bash
uv run scripts/generate_schema_module.py --class-name vulnerability_finding
```

Use the category package to import a generated schema:

```python
import importlib

findings = importlib.import_module("py_ocsf_arrow.schema.categories.2_findings")
schema = findings.get_vulnerability_finding_schema()
```

### With Nix

```bash
nix develop
```

> [!NOTE]
> `pyproject.toml` targets Python 3.14+, and the dev container matches that target. `flake.nix` currently provisions Python 3.13, so the Nix shell should be aligned before treating it as the authoritative runtime for the package.

## Target API shape

The following example shows the intended API direction. It is illustrative only and is **not implemented yet**.

```python
from ocsf_arrow import VulnerabilityFinding
from ocsf_transforms.defender import map_vulnerabilities

# 1. Fetch raw provider data using a separate client package
defender_df = fetch_from_defender_api()

# 2. Map raw fields to OCSF with columnar Polars operations
ocsf_df = map_vulnerabilities(defender_df)

# 3. Validate and materialize an Arrow table
builder = VulnerabilityFinding()
builder.consume(ocsf_df.to_dicts())
table = builder.to_table()
```

## Roadmap

The implementation plan is intentionally incremental:

1. **Foundation** — finish packaging, tooling, and repository layout
2. **`ocsf-arrow` core** — implement OCSF enums, Arrow schemas, and builder APIs
3. **`ocsf-transforms`** — add a first real provider mapping for Defender vulnerability data
4. **Real-world proof** — wire the packages into the existing security reporting project
5. **Stabilize** — improve docs, tests, typing, and packaging

Rust remains a possible future optimization path, but only after the Python API and behavior are proven with real workloads.

## Reference material

- [OCSF Schema Browser](https://schema.ocsf.io/)
- [OCSF Examples repository](https://github.com/ocsf/examples)
- [Apache Arrow](https://arrow.apache.org/)
- [Polars](https://pola.rs/)
- [Existing `http-to-arrow` README](https://github.com/ProxayFox/proxay-pylibs/blob/main/src/http_to_arrow/README.md)

## License

This project is licensed under the [Apache License 2.0](./LICENSE).
