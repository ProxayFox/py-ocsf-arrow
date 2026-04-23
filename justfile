# Optional local shortcuts layered over the existing uv workflows.

set shell := ["bash", "-euo", "pipefail", "-c"]

default:
    @just --list

help:
    @just --list

# --- Development ---
lint:
    uv run ruff check .

lint-fix:
    uv run ruff check --fix .

format:
    uv run ruff format .

format-check:
    uv run ruff format --check .

#  --- Testing ---
test:
    uv run pytest -q

test-all:
    uv run pytest --runslow -q

typecheck:
    uv run ty check --project .

quality:
    if ! just lint; then just lint-fix; fi
    if ! just format-check; then just format; fi
    just typecheck
    just test
    
docs-build:
    uv run --extra docs mkdocs build --strict

docs-serve:
    uv run --extra docs mkdocs serve

docs-validate:
    uv run --extra docs mkdocs build --strict