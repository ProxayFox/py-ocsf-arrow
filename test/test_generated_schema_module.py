from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import pyarrow as pa

from ocsf.api.client import OcsfApiClient
from py_ocsf_arrow.base import CACHE_DIR

# Resolve the default OCSF version so the test always points at the right
# versioned directory, even when new releases are published.
_client = OcsfApiClient(cache_dir=CACHE_DIR)
_default_version = _client.get_default_version()

_findings_init = (
    Path(__file__).resolve().parents[1]
    / "src"
    / "py_ocsf_arrow"
    / "schema"
    / _default_version
    / "categories"
    / "2_findings"
    / "__init__.py"
)
_spec = spec_from_file_location(
    f"py_ocsf_arrow.schema.{_default_version}.categories.2_findings",
    _findings_init,
)
assert _spec is not None and _spec.loader is not None
_findings = module_from_spec(_spec)
_findings.__package__ = f"py_ocsf_arrow.schema.{_default_version}.categories.2_findings"
_spec.loader.exec_module(_findings)

get_vulnerability_finding_schema = _findings.get_vulnerability_finding_schema
VULNERABILITY_FINDING_SCHEMA = _findings.VULNERABILITY_FINDING_SCHEMA


def test_generated_schema_module_is_callable() -> None:
    schema = get_vulnerability_finding_schema()
    assert isinstance(schema, pa.Schema)


def test_generated_schema_constant_is_schema() -> None:
    assert isinstance(VULNERABILITY_FINDING_SCHEMA, pa.Schema)
    assert "vulnerabilities" in VULNERABILITY_FINDING_SCHEMA.names
