"""Smoke tests verifying that workspace packages are importable and
that backend packages can reach py_ocsf_arrow symbols."""

import pytest


@pytest.mark.unit
class TestPackageImports:
    """Verify each workspace member is importable."""

    def test_arrow_package_importable(self):
        import py_ocsf_arrow

        assert hasattr(py_ocsf_arrow, "TypeMapper")
        assert hasattr(py_ocsf_arrow, "SchemaGenerator")
        assert hasattr(py_ocsf_arrow, "SchemaLoader")

    def test_clickhouse_package_importable(self):
        import py_ocsf_clickhouse

        assert hasattr(py_ocsf_clickhouse, "SchemaGenerator")
        assert hasattr(py_ocsf_clickhouse, "TypeMapper")

    def test_postgresql_package_importable(self):
        import py_ocsf_postgresql

        assert hasattr(py_ocsf_postgresql, "SchemaGenerator")
        assert hasattr(py_ocsf_postgresql, "TypeMapper")


@pytest.mark.unit
class TestCrossPackageDependency:
    """Verify backend packages resolve Arrow symbols through the workspace."""

    def test_clickhouse_uses_arrow_type_mapper(self):
        from py_ocsf_arrow import TypeMapper as ArrowTypeMapper
        from py_ocsf_clickhouse import TypeMapper as CHTypeMapper

        assert ArrowTypeMapper is CHTypeMapper

    def test_postgresql_uses_arrow_type_mapper(self):
        from py_ocsf_arrow import TypeMapper as ArrowTypeMapper
        from py_ocsf_postgresql import TypeMapper as PGTypeMapper

        assert ArrowTypeMapper is PGTypeMapper
