# Project status

## Maturity

`py-ocsf-arrow` is **pre-alpha**.

That means the project is already useful for experimentation and internal iteration, but the public API and generated layout should still be treated as moving targets.

## Implemented today

- version-aware OCSF schema loading through `ocsf-lib`
- profile/extension filtering in `OCSFArrow`
- OCSF-to-Arrow scalar and derived type mapping in `TypeMapper`
- runtime `pyarrow.Schema` generation in `SchemaGenerator`
- nested struct resolution for object-typed OCSF fields
- versioned schema-module generation under `src/py_ocsf_arrow/schema/<version>/`
- tests covering type mapping, nested struct generation, and generated-module loading

## Planned but not implemented yet

- builder/container APIs for Arrow tables
- provider-specific transform packages such as `ocsf-transforms`
- richer end-to-end examples built from real provider data
- long-term API stabilization and packaging polish

## Known rough edges

- generated schemas are loaded with `importlib` instead of clean package imports because version directories intentionally preserve upstream version strings like `1.8.0`
- the runtime API is small and intentionally low-level right now
- docs are being built out alongside the codebase, not after stabilization

## Practical expectation

Use this project when you want:

- a grounded base for OCSF/Arrow experimentation
- versioned schema artifacts tied to upstream OCSF releases
- a place to iterate on API shape before wider packaging

Do not treat it as a fully stable end-user SDK yet. That badge has not been earned, and the repo would probably blush if we tried to pin it on too early.
