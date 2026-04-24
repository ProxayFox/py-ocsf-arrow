# py-ocsf-arrow

Python seed for an OCSF Arrow ecosystem: reusable libraries that turn security-provider data into OCSF-compliant Apache Arrow tables.

> [!WARNING]
> This repository is still pre-alpha. The architecture and API examples below describe the intended direction; the current implementation is mostly scaffolding with a placeholder launcher.

Full project documentation now lives under [`docs/`](docs/) and can be built locally with `just docs-build` or served with `just docs-serve`.

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

Today this repository is still the seed project, but it has moved beyond a blank template. At the moment it contains:

- runtime helpers in `src/py_ocsf_arrow/` for OCSF schema loading, type mapping, and Arrow schema generation
- a generator script that materializes versioned schema modules under `src/py_ocsf_arrow/schema/<version>/`
- tests covering type mapping, nested object struct generation, and generated-module loading
- MkDocs-based documentation scaffolding under `docs/` plus `mkdocs.yml`
- development scaffolding via `.devcontainer/`, `flake.nix`, `justfile`, and `pyproject.toml`

That means the following are still planned work:

- [ ] batch builder or container APIs
- [ ] provider-specific transforms, starting with Defender vulnerability mappings
- [ ] richer end-to-end examples built from real provider data
- [ ] API stabilization and packaging polish

## Repository layout today

```text
.
├── .devcontainer/          # VS Code dev container and Dockerfile
├── .github/                # Copilot and repository automation files
├── docs/                   # MkDocs site content
├── scripts/                # Code generation utilities
├── src/
│   └── py_ocsf_arrow/      # Runtime helpers and generated schema modules
├── test/                   # Tests for mapping, schema generation, and loading
├── flake.nix               # Nix development shell
├── justfile                # Local development shortcuts
├── main.py                 # Placeholder launcher
├── mkdocs.yml              # MkDocs site configuration
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

For contributor workflows including docs and tests:

```bash
uv sync --group dev --extra docs
```

### Generate callable schema modules

Use the generator script to materialize OCSF class schemas as importable Python code, organized by version and category:

```bash
# Generate all stable OCSF versions (default)
uv run scripts/generate_schema_module.py

# Or use the justfile shortcut
just generate

# Generate a single version
just generate 1.8.0

# Generate only one class across all versions
uv run scripts/generate_schema_module.py --class-name vulnerability_finding
```

This produces a versioned directory tree under `src/py_ocsf_arrow/schema/`:

```text
schema/
  1.0.0/
    objects/        ← shared object schema files for this version
    categories/     ← class files grouped by OCSF category
      2_findings/
        2002_vulnerability_finding.py
        ...
  1.1.0/
    ...
  1.8.0/
    ...
```

Use `importlib` to load a versioned schema (version directories contain dots):

```python
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

init_path = Path("src/py_ocsf_arrow/schema/1.8.0/categories/2_findings/__init__.py")
spec = spec_from_file_location("findings", init_path)
mod = module_from_spec(spec)
spec.loader.exec_module(mod)

schema = mod.get_vulnerability_finding_schema()
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
