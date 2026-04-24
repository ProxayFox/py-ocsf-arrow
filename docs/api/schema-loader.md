# `SchemaLoader`

`SchemaLoader` provides a clean API for loading generated Arrow schemas from the versioned schema modules under `src/py_ocsf_arrow/schema/<version>/`.

You do not need to write any `importlib` boilerplate yourself.

## Quick start

```python
from py_ocsf_arrow import SchemaLoader

loader = SchemaLoader("1.8.0")
schema = loader.load_class("vulnerability_finding")
```

## Install generated schemas first

`SchemaLoader` reads from files that must be generated first:

```bash
just generate
```

Or for a single version:

```bash
just generate 1.8.0
```

## Load a class schema

```python
from py_ocsf_arrow import SchemaLoader

loader = SchemaLoader("1.8.0")
schema = loader.load_class("vulnerability_finding")
```

## Load an object schema

```python
schema = loader.load_object("cve")
```

## Use the default (latest) version

Omit the version or pass `"default"` to use the highest installed stable version automatically:

```python
from py_ocsf_arrow import SchemaLoader

loader = SchemaLoader()  # or SchemaLoader("default")
schema = loader.load_class("vulnerability_finding")
print(f"Loaded from version {loader.version}")
```

## Module-level convenience helpers

```python
from py_ocsf_arrow import load_class_schema, load_object_schema

vuln_schema = load_class_schema("vulnerability_finding", version="1.8.0")
cve_schema  = load_object_schema("cve", version="1.8.0")
```

These are thin wrappers around `SchemaLoader` and are the shortest path when you need a one-off schema.

## Discover available content

```python
from py_ocsf_arrow import SchemaLoader

# All installed versions, newest-first
SchemaLoader.available_versions()
# ['1.8.0', '1.7.0', ...]

loader = SchemaLoader("1.8.0")

# All classes in this version
loader.available_classes()
# ['compliance_finding', 'detection_finding', ..., 'vulnerability_finding']

# All objects in this version
loader.available_objects()
# ['account', 'analytic', 'cve', 'cvss', ...]
```

## Using the schema with PyArrow

Once you have a `pa.Schema`, normal PyArrow operations apply:

```python
import pyarrow as pa
from py_ocsf_arrow import load_class_schema

schema = load_class_schema("vulnerability_finding", version="1.8.0")

# Validate or cast a list of records
table = pa.Table.from_pylist(records, schema=schema)

# Inspect fields
for field in schema:
    print(f"{field.name}: {field.type}")
```

## Profile and extension filtering

Generated schemas include **all** OCSF profile and extension attributes.
By default, `SchemaLoader` strips them so you get a base-only schema.

### Base schema (default — no profiles)

```python
loader = SchemaLoader("1.8.0")
schema = loader.load_class("vulnerability_finding")
# Only base fields — no cloud, host, security_control, etc.
```

### Include specific profiles

```python
loader = SchemaLoader("1.8.0", prf=["cloud", "host"])
schema = loader.load_class("vulnerability_finding")
# Base fields + cloud and host profile attributes
```

### Include specific extensions

```python
loader = SchemaLoader("1.8.0", ext=["linux"])
schema = loader.load_class("vulnerability_finding")
# Base fields + attributes from the linux extension's implied profiles
```

### Include all profiles

```python
loader = SchemaLoader("1.8.0")
all_profiles = loader.available_profiles()
all_extensions = loader.available_extensions()

full_loader = SchemaLoader("1.8.0", prf=all_profiles, ext=all_extensions)
schema = full_loader.load_class("vulnerability_finding")
# All 73 fields for vulnerability_finding in v1.8.0
```

### Module-level helper with profiles

```python
from py_ocsf_arrow import load_class_schema

schema = load_class_schema(
    "vulnerability_finding", version="1.8.0", prf=["cloud"]
)
```

### Semantics

| Parameter            | Effect                                                         |
| -------------------- | -------------------------------------------------------------- |
| `prf=None` (default) | Exclude all profile attributes (base only)                     |
| `prf=[]`             | Same as `None` — exclude all                                   |
| `prf=["cloud"]`      | Include only cloud profile attributes                          |
| `ext=None` (default) | Exclude all extension-contributed attributes                   |
| `ext=["linux"]`      | Include attributes from the Linux extension's implied profiles |

!!! note
    Profile filtering applies to **class schemas only**. Object schemas are
    not modified by profiles in OCSF, so `load_object()` always returns the
    full object schema regardless of `ext`/`prf` settings.

## Discover available profiles and extensions

```python
loader = SchemaLoader("1.8.0")

loader.available_profiles()
# ['ai_operation', 'cloud', 'container', 'data_classification', ...]

loader.available_extensions()
# ['linux', 'macos', 'win']
```

## Notes

- `SchemaLoader` caches the category module per instance, so loading multiple classes from the same category (e.g. two findings) only loads the category `__init__.py` once.
- Version directories use exact OCSF version strings (`1.8.0`, not `v1_8_0`), which is why this loader exists — those directory names cannot be used as Python import segments.
- Profile metadata is stored in `_profiles.json` per version directory, written at generation time. If the file is missing, re-run `just generate`.
- If you want schemas without generating files first, use the runtime API instead: [`SchemaGenerator`](schema-generator.md).
