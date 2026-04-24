# Documentation workflow

## Build the site

```bash
just docs-build
```

This runs MkDocs in strict mode.

## Serve the site locally

```bash
just docs-serve
```

## Validate in CI-style mode

```bash
just docs-validate
```

Right now `docs-validate` and `docs-build` are intentionally equivalent. Keeping both names makes it easier to separate local habits from future CI jobs.

## Writing guidelines

- keep examples grounded in code that exists today
- prefer examples backed by tests when possible
- clearly label roadmap material instead of mixing it into current usage docs
- avoid documenting speculative APIs as if they already shipped

## Good sources for examples

- `test/test_schema_generator.py` — nested object struct generation
- `test/test_generated_schema_module.py` — versioned schema loading with `importlib`
- `scripts/generate_schema_module.py` — current generator flags and output layout

## Updating README vs MkDocs

Use:

- `README.md` for the quick repository overview
- `docs/` for fuller usage, architecture, and contributor guidance

If a section starts getting long or workflow-specific, it probably belongs in `docs/`.
