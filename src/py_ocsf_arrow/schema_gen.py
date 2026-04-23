import pyarrow as pa
from functools import cached_property

# Local Imports
from . import TypeMapper, OCSFArrow


class SchemaGenerationError(Exception):
    """Custom exception for schema generation errors."""

    pass


class SchemaGenerator(OCSFArrow):
    """Class to handle generation of PyArrow schemas from OCSF event class definitions."""

    @cached_property
    def _type_mapper(self) -> TypeMapper:
        """Return a cached type mapper sharing this generator's client and schema."""
        return TypeMapper(
            client=self.client,
            version=self.version,
            schema=self.schema,
            _ignored_attr=self._ignored_attr,
        )

    def ocsf_type_to_arrow(
        self, type_name: str, is_array: bool = False, version: str = "default"
    ) -> pa.DataType:
        """Convert an OCSF type_name to a PyArrow type."""
        if version == "default" or version == self.version:
            arrow_type = self._type_mapper.OCSF_TO_ARROW.get(type_name)
        else:
            arrow_type = TypeMapper.init(version=version).OCSF_TO_ARROW.get(type_name)

        if arrow_type is None:
            # Unknown or object type — store as JSON string
            arrow_type = pa.string()

        if is_array:
            return pa.list_(arrow_type)

        return arrow_type

    def build_arrow_schema(self, class_name: str) -> pa.Schema:
        """
        Build a PyArrow schema from an OCSF event class definition.

        class_name: e.g. "vulnerability_finding"
        """
        # Select the Class
        event_class = self.schema.classes[class_name]

        fields = []
        for attr_name, attr in sorted(event_class.attributes.items()):
            # Skip any attributes that are part of extensions or profiles we are ignoring
            if attr_name in self._ignored_attr:
                continue

            arrow_type = self.ocsf_type_to_arrow(
                type_name=attr.type,
                is_array=getattr(attr, "is_array", False),
                version=getattr(attr, "version", "default"),
            )
            nullable = attr.requirement != "required"

            fields.append(pa.field(attr_name, arrow_type, nullable=nullable))

        return pa.schema(fields)
