# `OCSFArrow`

`OCSFArrow` is the shared base class for the runtime helpers in `py-ocsf-arrow`.

## Purpose

It is responsible for:

- constructing or reusing an `OcsfApiClient`
- resolving the requested OCSF version
- loading the matching `OcsfSchema`
- computing which extension/profile attributes should be ignored

## Factory method

```python
from py_ocsf_arrow.base import OCSFArrow

base = OCSFArrow.init(version="default")
```

Because `init()` is a classmethod, calling it on a subclass returns that subclass:

```python
from py_ocsf_arrow import SchemaGenerator

generator = SchemaGenerator.init(version="1.8.0")
```

## Parameters

### `version`

Supported forms:

- `"default"` — resolve to the current default version from the OCSF API
- an explicit version string such as `"1.8.0"`

If the version is not supported by the upstream API, `init()` raises `ValueError`.

### `cache`

Controls the API cache directory:

- `True` — use the repository cache directory (`.cache/`)
- `False` — disable local caching
- `str | Path` — use a custom cache location

### `client`

Pass an existing `OcsfApiClient` when you want to share cache and HTTP behavior across multiple helper objects.

### `ext` and `prf`

These are **include lists**, not ignore lists.

If you pass:

```python
SchemaGenerator.init(ext=["linux"], prf=["cloud"])
```

then only those selected extension/profile attributes are kept. Attributes from unselected profiles/extensions are ignored.

If you pass `None` for either parameter, the current implementation ignores all attributes from that group.

## Returned state

Instances expose:

- `client` — the active `OcsfApiClient`
- `version` — the resolved version string
- `schema` — the loaded `OcsfSchema`
- `_ignored_attr` — the internal set of attribute names filtered out by profile/extension selection

`_ignored_attr` is an internal implementation detail and should be treated as such.
