"""Generate PyArrow schemas from OCSF event class and object definitions.

The :class:`SchemaGenerator` builds Arrow schemas at runtime by traversing OCSF
class and object attribute definitions, resolving OCSF types to Arrow data types,
and handling nested objects and array types. It respects profile and extension
filtering to exclude attributes that are not part of the active configuration.

This module provides :class:`SchemaGenerator` and the method :meth:`~SchemaGenerator.ocsf_type_to_arrow`
to convert individual OCSF type names to Arrow types, which is also used for nested
object schema resolution.
"""

from ocsf.schema import OcsfObject
import pyarrow as pa
from functools import cached_property
from collections.abc import Mapping

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

    def _build_fields(
        self,
        attributes: Mapping,
        version: str = "default",
        _seen_objects: set[str] | None = None,
    ) -> list[pa.Field]:
        """Build Arrow fields for a collection of OCSF attributes."""
        fields: list[pa.Field] = []
        for attr_name, attr in sorted(attributes.items()):
            # Skip any attributes that are part of extensions or profiles we are ignoring
            if attr_name in self._ignored_attr:
                continue

            arrow_type = self.ocsf_type_to_arrow(
                type_name=attr.type,
                is_array=getattr(attr, "is_array", False),
                version=getattr(attr, "version", "default") or "default",
                _seen_objects=_seen_objects,
            )
            nullable = attr.requirement != "required"
            fields.append(pa.field(attr_name, arrow_type, nullable=nullable))

        return fields

    def ocsf_type_to_arrow(
        self,
        type_name: str,
        is_array: bool = False,
        version: str = "default",
        _seen_objects: set[str] | None = None,
    ) -> pa.DataType:
        """Convert an OCSF type_name to a PyArrow type."""
        if version == "default" or version == self.version:
            arrow_type = self._type_mapper.OCSF_TO_ARROW.get(type_name)
        else:
            arrow_type = TypeMapper.init(version=version).OCSF_TO_ARROW.get(type_name)

        if arrow_type is None:
            seen = _seen_objects or set()

            # Try to resolve OCSF objects into nested Arrow structs.
            if type_name in seen:
                # Cycle protection fallback.
                arrow_type = pa.string()
            elif type_name in self.schema.objects:
                object_schema = self.schema.objects[type_name]
                nested_seen = set(seen)
                nested_seen.add(type_name)
                nested_fields = self._build_fields(
                    object_schema.attributes,
                    version=version,
                    _seen_objects=nested_seen,
                )
                arrow_type = pa.struct(nested_fields)
            else:
                # Unknown type fallback.
                arrow_type = pa.string()

        if is_array:
            return pa.list_(arrow_type)

        return arrow_type

    def build_class_schema(self, class_name: str) -> pa.Schema:
        """
        Build a PyArrow schema from an OCSF event class definition.

        class_name: e.g. "vulnerability_finding"
        """
        # Select the Class
        event_class = self.schema.classes[class_name]

        fields = self._build_fields(event_class.attributes)

        return pa.schema(fields)

    def build_object_schema(self, object_name: str) -> pa.Schema:
        """Build a PyArrow schema for the OCSF dictionary."""

        dictionary: OcsfObject = self.schema.objects[object_name]

        fields = self._build_fields(dictionary.attributes)

        return pa.schema(fields)
