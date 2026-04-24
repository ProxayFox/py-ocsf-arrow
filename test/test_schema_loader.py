"""Tests for SchemaLoader and module-level schema loading helpers."""

import pytest
import pyarrow as pa

from py_ocsf_arrow import SchemaLoader, load_class_schema, load_object_schema


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture(scope="module")
def loader() -> SchemaLoader:
    """A SchemaLoader pinned to 1.8.0 so tests are reproducible."""
    return SchemaLoader("1.8.0")


# ---------------------------------------------------------------------------
# Version resolution
# ---------------------------------------------------------------------------


class TestAvailableVersions:
    def test_returns_list(self):
        versions = SchemaLoader.available_versions()
        assert isinstance(versions, list)
        assert len(versions) > 0

    def test_sorted_newest_first(self):
        versions = SchemaLoader.available_versions()
        # All entries should parse as dotted integers.
        for v in versions:
            assert all(part.isdigit() for part in v.split("."))
        # First entry should be >= last entry by version tuple.
        first = tuple(int(x) for x in versions[0].split("."))
        last = tuple(int(x) for x in versions[-1].split("."))
        assert first >= last

    def test_excludes_pre_releases(self):
        versions = SchemaLoader.available_versions()
        for v in versions:
            assert "-rc" not in v
            assert "-dev" not in v


class TestVersionResolution:
    def test_default_resolves_to_highest_installed(self):
        loader = SchemaLoader("default")
        expected = SchemaLoader.available_versions()[0]
        assert loader.version == expected

    def test_explicit_version_accepted(self):
        loader = SchemaLoader("1.8.0")
        assert loader.version == "1.8.0"

    def test_missing_version_raises(self):
        with pytest.raises(FileNotFoundError, match="No generated schema"):
            SchemaLoader("0.0.0")


# ---------------------------------------------------------------------------
# Class schema loading
# ---------------------------------------------------------------------------


class TestLoadClass:
    def test_returns_pyarrow_schema(self, loader: SchemaLoader):
        schema = loader.load_class("vulnerability_finding")
        assert isinstance(schema, pa.Schema)

    def test_vulnerability_finding_has_expected_field(self, loader: SchemaLoader):
        schema = loader.load_class("vulnerability_finding")
        assert "vulnerabilities" in schema.names

    def test_detection_finding_returns_schema(self, loader: SchemaLoader):
        schema = loader.load_class("detection_finding")
        assert isinstance(schema, pa.Schema)

    def test_unknown_class_raises(self, loader: SchemaLoader):
        with pytest.raises(KeyError, match="not found"):
            loader.load_class("not_a_real_class")

    def test_cached_category_module_reused(self, loader: SchemaLoader):
        # Loading two classes from the same category should reuse the cached module.
        loader.load_class("vulnerability_finding")
        loader.load_class("detection_finding")
        # One cache entry for the 2_findings category.
        assert any("2_findings" in k for k in loader._category_cache)


# ---------------------------------------------------------------------------
# Object schema loading
# ---------------------------------------------------------------------------


class TestLoadObject:
    def test_returns_pyarrow_schema(self, loader: SchemaLoader):
        schema = loader.load_object("cve")
        assert isinstance(schema, pa.Schema)

    def test_cve_has_epss_struct_field(self, loader: SchemaLoader):
        """cve.epss should be a nested struct, not a plain string."""
        schema = loader.load_object("cve")
        epss_field = schema.field("epss")
        assert pa.types.is_struct(epss_field.type)

    def test_epss_object_loads(self, loader: SchemaLoader):
        schema = loader.load_object("epss")
        assert isinstance(schema, pa.Schema)

    def test_unknown_object_raises(self, loader: SchemaLoader):
        with pytest.raises(KeyError, match="not found"):
            loader.load_object("not_a_real_object")


# ---------------------------------------------------------------------------
# Discovery helpers
# ---------------------------------------------------------------------------


class TestAvailableClasses:
    def test_returns_list_of_strings(self, loader: SchemaLoader):
        classes = loader.available_classes()
        assert isinstance(classes, list)
        assert all(isinstance(c, str) for c in classes)

    def test_includes_vulnerability_finding(self, loader: SchemaLoader):
        assert "vulnerability_finding" in loader.available_classes()

    def test_no_duplicates(self, loader: SchemaLoader):
        classes = loader.available_classes()
        assert len(classes) == len(set(classes))


class TestAvailableObjects:
    def test_returns_list_of_strings(self, loader: SchemaLoader):
        objects = loader.available_objects()
        assert isinstance(objects, list)
        assert all(isinstance(o, str) for o in objects)

    def test_includes_cve(self, loader: SchemaLoader):
        assert "cve" in loader.available_objects()

    def test_no_init_in_list(self, loader: SchemaLoader):
        assert "__init__" not in loader.available_objects()


# ---------------------------------------------------------------------------
# Module-level convenience helpers
# ---------------------------------------------------------------------------


class TestModuleLevelHelpers:
    def test_load_class_schema(self):
        schema = load_class_schema("vulnerability_finding", version="1.8.0")
        assert isinstance(schema, pa.Schema)

    def test_load_object_schema(self):
        schema = load_object_schema("cve", version="1.8.0")
        assert isinstance(schema, pa.Schema)

    def test_load_class_default_version(self):
        # Should work without specifying a version.
        schema = load_class_schema("vulnerability_finding")
        assert isinstance(schema, pa.Schema)

    def test_load_object_default_version(self):
        schema = load_object_schema("cve")
        assert isinstance(schema, pa.Schema)
