import pyarrow as pa

from py_ocsf_arrow import SchemaGenerator


class TestSchemaGenerator:
    generator = SchemaGenerator.init(version="default")

    def test_object_attribute_can_be_struct(self):
        """`cve.epss` should resolve as a nested `epss` struct, not plain string."""
        cve_schema = self.generator.build_object_schema("cve")

        epss_field = cve_schema.field("epss")
        assert pa.types.is_struct(epss_field.type)

    def test_cve_epss_struct_matches_epss_object_schema(self):
        """Nested `cve.epss` struct fields should match the standalone `epss` schema."""
        cve_schema = self.generator.build_object_schema("cve")
        epss_schema = self.generator.build_object_schema("epss")

        epss_struct_type = cve_schema.field("epss").type
        assert pa.types.is_struct(epss_struct_type)

        nested_schema = pa.schema(list(epss_struct_type))
        assert nested_schema.equals(epss_schema)
