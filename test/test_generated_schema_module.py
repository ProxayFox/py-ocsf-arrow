import pyarrow as pa

from py_ocsf_arrow.schema.findings import (
    VULNERABILITY_FINDING_SCHEMA,
    get_vulnerability_finding_schema,
)


def test_generated_schema_module_is_callable() -> None:
    schema = get_vulnerability_finding_schema()
    assert isinstance(schema, pa.Schema)


def test_generated_schema_constant_is_schema() -> None:
    assert isinstance(VULNERABILITY_FINDING_SCHEMA, pa.Schema)
    assert "vulnerabilities" in VULNERABILITY_FINDING_SCHEMA.names
