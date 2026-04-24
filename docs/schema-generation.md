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
