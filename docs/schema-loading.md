# Schema loading

Generated schema modules are versioned by directory name, for example `schema/1.8.0/...`, and category directories also contain numeric prefixes such as `2_findings/`.

That means normal Python imports are not enough for every case, because:

- version directories contain dots (`1.8.0`)
- class files contain numeric prefixes (`2002_vulnerability_finding.py`)

The supported loading pattern is `importlib.util.spec_from_file_location`.

## Load a specific version and category

```python
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

init_path = Path("src/py_ocsf_arrow/schema/1.8.0/categories/2_findings/__init__.py")
spec = spec_from_file_location("findings", init_path)
assert spec is not None and spec.loader is not None

module = module_from_spec(spec)
spec.loader.exec_module(module)

schema = module.get_vulnerability_finding_schema()
```

## Resolve the default OCSF version dynamically

This mirrors the test-backed usage in `test/test_generated_schema_module.py`.

```python
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

from ocsf.api.client import OcsfApiClient
from py_ocsf_arrow.base import CACHE_DIR

client = OcsfApiClient(cache_dir=CACHE_DIR)
default_version = client.get_default_version()

init_path = (
    Path("src/py_ocsf_arrow/schema")
    / default_version
    / "categories"
    / "2_findings"
    / "__init__.py"
)
spec = spec_from_file_location("findings", init_path)
assert spec is not None and spec.loader is not None

module = module_from_spec(spec)
spec.loader.exec_module(module)

schema = module.VULNERABILITY_FINDING_SCHEMA
```

## Prefer the runtime API when possible

If you do not specifically need generated Python files, the runtime API avoids path-based imports entirely:

```python
from py_ocsf_arrow import SchemaGenerator

generator = SchemaGenerator.init(version="default")
schema = generator.build_class_schema("vulnerability_finding")
```

## Why the generated files use `importlib` internally

Generated class files also load their object dependencies with `importlib`. That design avoids invalid dotted imports such as:

```python
from py_ocsf_arrow.schema.1.8.0.objects.cve import CVE_SCHEMA
```

which would be invalid Python syntax because `1.8.0` is not a legal dotted package segment.
