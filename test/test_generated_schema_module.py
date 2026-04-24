import importlib

import pyarrow as pa

_findings = importlib.import_module("py_ocsf_arrow.schema.categories.2_findings")
get_vulnerability_finding_schema = _findings.get_vulnerability_finding_schema
VULNERABILITY_FINDING_SCHEMA = _findings.VULNERABILITY_FINDING_SCHEMA


def test_generated_schema_module_is_callable() -> None:
    schema = get_vulnerability_finding_schema()
    assert isinstance(schema, pa.Schema)


def test_generated_schema_constant_is_schema() -> None:
    assert isinstance(VULNERABILITY_FINDING_SCHEMA, pa.Schema)
    assert "vulnerabilities" in VULNERABILITY_FINDING_SCHEMA.names
