# Schema generation

The generator script materializes versioned Python schema modules from OCSF metadata.

## Why generate modules?

Direct runtime schema generation is convenient, but generated modules help when you want:

- checked-in schema files for review and diffing
- version-isolated schema trees
- importable constants and helper functions for specific OCSF classes
- future automation around new OCSF releases

## Command line interface

The generator lives at `scripts/generate_schema_module.py`.

### Generate all stable versions

```bash
uv run scripts/generate_schema_module.py
```

Equivalent shortcut:

```bash
just generate
```

`--version all` is the default. It enumerates available versions from the OCSF API and skips pre-release versions containing `-rc` or `-dev`.

### Generate a single stable version

```bash
uv run scripts/generate_schema_module.py --version 1.8.0
```

Shortcut:

```bash
just generate 1.8.0
```

### Generate only one class

```bash
uv run scripts/generate_schema_module.py \
  --version default \
  --class-name vulnerability_finding
```

## Explicit pre-release generation

`--version all` skips pre-releases on purpose, but you can still target one explicitly if the OCSF API supports it:

```bash
uv run scripts/generate_schema_module.py --version 1.9.0-dev
```

## Output layout

Generated files are written under `src/py_ocsf_arrow/schema/<version>/`.

```text
src/py_ocsf_arrow/schema/
  1.8.0/
    __init__.py
    objects/
      __init__.py
      cve.py
      epss.py
      ...
    categories/
      __init__.py
      2_findings/
        __init__.py
        2001_security_finding.py
        2002_vulnerability_finding.py
        ...
```

## Design notes

### Version isolation

Each OCSF version gets its own `objects/` and `categories/` tree. This avoids mixing schemas from different upstream releases.

### Category grouping

Class files are grouped by OCSF category UID and name, for example:

- `1_system_activity/`
- `2_findings/`
- `4_network_activity/`

### Generated helpers

Each category `__init__.py` exposes a stable loader-style API:

- `get_vulnerability_finding_schema()`
- `VULNERABILITY_FINDING_SCHEMA`

## When to use the runtime API instead

If you only need a `pyarrow.Schema` in-process, the direct Python API is usually simpler:

```python
from py_ocsf_arrow import SchemaGenerator

generator = SchemaGenerator.init(version="1.8.0")
schema = generator.build_class_schema("vulnerability_finding")
```

Use generated modules when reproducibility, checked-in artifacts, or release automation matter more than simplicity.

## Promotion analysis workflow

Schema generation remains the default path, but the repository also provides an
operator-facing promotion analysis CLI at `scripts/analyze_promotions.py`.

It can be used to:

- identify which OCSF objects are good candidates for promotion into standalone
  tables or schemas
- review the scoring output as summary text, JSON, or CSV
- optionally run the opt-in transformation step that rewrites promoted embedded
  objects into foreign-key fields

The workflow is intentionally opt-in. Running the analysis or transform CLI does
**not** change the repository's default base-only schema generation or loading
behavior.

### Analysis-only usage

Example usage:

```bash
uv run scripts/analyze_promotions.py \
  --version 1.8.0 \
  --format summary \
  --override metadata=EMBED \
  --override endpoint=EMBED
```

This writes the report to `stdout`. The default `--format summary` output is a
human-readable verdict summary; use `--include-scores` to append a per-object
breakdown of the composite and per-axis scores.

### Export machine-readable reports

Use `--format json` or `--format csv` when the results need to feed downstream
review, automation, or ad hoc spreadsheet work.

```bash
uv run scripts/analyze_promotions.py \
  --version 1.8.0 \
  --format json \
  --output outputs/promotion-analysis-1.8.0.json \
  --override metadata=EMBED \
  --override endpoint=EMBED
```

`--output` writes the rendered report to a file instead of `stdout` and creates
parent directories as needed.

### Run the transform pipeline

To write transformed schemas as serialized Arrow schema files:

```bash
uv run scripts/analyze_promotions.py \
  --version 1.8.0 \
  --transform \
  --transform-output outputs/promotion-transform \
  --override metadata=EMBED \
  --override endpoint=EMBED
```

When `--transform` is enabled, the report still goes to `stdout`, while an
operator-facing transform summary is written to `stderr`. If
`--transform-output` is set, the CLI writes Arrow-serialized schema artifacts to
the target directory using this layout:

```text
outputs/promotion-transform/
  classes/
    <class-name>.arrow
    ...
  promoted/
    <object-name>.arrow
    ...
  manifest.json
```

The generated `manifest.json` records the number of transformed class schemas,
the number of promoted standalone schemas, and any warnings emitted by the
transform step.

### Flag reference

| Flag | Purpose |
| --- | --- |
| `--version` | Required OCSF version to analyze, for example `1.8.0` or `default`. |
| `--override NAME=VERDICT` | Force a verdict for a specific object. Repeat the flag to supply multiple overrides. |
| `--promote-threshold` | Override the composite-score threshold used to assign `PROMOTE`. |
| `--review-threshold` | Override the composite-score threshold used to assign `REVIEW`. |
| `--format` | Render the analysis as `summary`, `json`, or `csv`. |
| `--output` | Write the rendered report to a file instead of `stdout`. |
| `--include-scores` | In `summary` mode, append a per-object score breakdown. |
| `--transform` | Run the promotion-aware schema transformation pipeline after analysis. |
| `--strict-review` | In transform mode, treat any remaining `REVIEW` verdict as a failure instead of leaving the object embedded. |
| `--transform-output` | Directory where transformed `.arrow` schema files and `manifest.json` should be written. |

### Overrides and verdict handling

Overrides are operator-supplied and follow `NAME=VERDICT`, for example
`metadata=EMBED`. Verdict names are case-insensitive on input and are validated
against the script's supported verdict set.

In non-strict mode, objects that remain `REVIEW` stay embedded in the rewritten
class schemas. This lets operators generate transformed outputs while keeping
borderline cases explicit and reviewable.

### What the outputs mean

- `summary` is best for interactive review in a terminal.
- `json` is best for downstream tooling or richer inspection.
- `csv` is convenient for spreadsheet-style analysis.
- `classes/*.arrow` contains the transformed class schemas.
- `promoted/*.arrow` contains standalone schemas for promoted objects.
- `manifest.json` captures counts and warnings from the transform run.

Use the analysis-only mode when you want to inspect likely promotion candidates
without generating any new schema artifacts. Use transform mode when you want to
materialize the foreign-key rewrite and promoted object schemas for further
experimentation.
