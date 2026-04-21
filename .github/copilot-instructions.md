# Project Guidelines

## Mission and current state

- This repository is the early Python seed of an OCSF Arrow ecosystem. The long-term goal is to extract security-data normalisation from a monolith into reusable, pip-installable packages that produce OCSF-compliant Apache Arrow tables.
- The current repo is still close to a template: `main.py` is a placeholder launcher and `pyproject.toml` is the source of truth for project metadata, dependencies, and tool configuration.
- Treat work here as foundational `ocsf-arrow` work unless the user explicitly asks for broader ecosystem scaffolding.

## Architectural intent

- Keep the core library focused on Arrow-native OCSF primitives:
  - OCSF enums and lookup tables
  - Arrow schemas for OCSF classes
  - builder or container APIs that validate batches and emit `pyarrow.Table` or `polars.DataFrame`
- Keep clear boundaries:
  - core Arrow/OCSF logic belongs here
  - provider-specific transforms belong in a future `ocsf-transforms` package
  - HTTP/API clients stay separate from both

## Data and validation preferences

- Prefer columnar processing and batch validation over per-row validation for real workloads.
- When implementing mapping or validation logic, favor `polars` + `pyarrow` interop and Arrow schema enforcement instead of row-by-row Pydantic or dataclass validation.
- Use `IntEnum` for OCSF code tables and mapping helpers where that improves clarity.
- Verify OCSF field names, class IDs, and enum semantics against the [OCSF Schema Browser](https://schema.ocsf.io/) before hard-coding them.
- Treat the [OCSF examples repository](https://github.com/ocsf/examples) as reference material, not a gold standard.

## Working in this repo today

- Use `uv` for environment and dependency management. For normal development, sync with `uv sync --extra dev`.
- Run the project with `uv run python main.py` or the installed script `uv run main`.
- Run tests with `uv run pytest`.
- Target Python 3.14 or newer and keep code compatible with the interpreter version declared in `pyproject.toml`.
- Pytest is already configured to discover tests from the `tests/` directory. Add new tests there instead of ad hoc test files in the repository root.
- Pytest markers `unit`, `integration`, `performance`, and `slow` are reserved in the project config. Use them consistently when adding tests.
- Prefer keeping new tooling and package configuration in `pyproject.toml` when the tool supports it instead of introducing extra config files.
- Keep entry points thin. If the project grows beyond a trivial launcher, move reusable logic into a package directory and leave `main.py` as a small launcher.
- Treat the devcontainer and `flake.nix` as the supported bootstrap paths. Avoid changing startup scripts or environment setup unless the task actually requires it.
- The devcontainer post-create step already installs the dev dependencies and creates `uv-sync-dev` and `uv-sync-all` helper commands. Reuse those workflows instead of introducing parallel bootstrap commands.
- Follow the repository formatter settings. Black is the default formatter in the workspace.
- Documentation is intentionally minimal. When behavior or setup changes, update `README.md` with the user-facing impact.

## Future-state guidance

- The broader design notes point toward a monorepo with `ocsf-arrow`, `ocsf-transforms`, and separate provider clients, but that structure does not exist in this repository yet.
- Do not invent future-state files, commands, or tooling (for example `just quality`, workspace packages, or Rust build plumbing) unless the user explicitly asks to add them.
- Rust is a future optimization path, not the default next step. Prove API shape and correctness in Python first.

## Style and implementation bias

- Keep implementations straightforward, typed where helpful, and easy to extract into reusable packages.
- Avoid speculative abstractions and framework-building before there is a concrete consumer.
- If you need an API design reference for Arrow-backed container or builder ergonomics, the user's existing [`http-to-arrow` README](https://github.com/ProxayFox/proxay-pylibs/blob/main/src/http_to_arrow/README.md) is a useful precedent.
