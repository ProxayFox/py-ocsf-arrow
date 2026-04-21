from ocsf.util import get_schema
import pyarrow as pa

from .type_map import OCSF_TO_ARROW


def ocsf_type_to_arrow(type_name: str, is_array: bool = False) -> pa.DataType:
    """Convert an OCSF type_name to a PyArrow type."""
    arrow_type = OCSF_TO_ARROW.get(type_name)

    if arrow_type is None:
        # Unknown or object type — store as JSON string
        arrow_type = pa.string()

    if is_array:
        return pa.list_(arrow_type)

    return arrow_type


def build_arrow_schema(schema, class_name: str) -> pa.Schema:
    """
    Build a PyArrow schema from an OCSF event class definition.

    schema:     The OcsfSchema object from get_schema()
    class_name: e.g. "vulnerability_finding"
    """
    event_class = schema.classes[class_name]
    fields = []

    for attr_name, attr in event_class.attributes.items():
        arrow_type = ocsf_type_to_arrow(
            type_name=attr.type,
            is_array=getattr(attr, "is_array", False),
        )
        nullable = attr.requirement != "required"

        fields.append(pa.field(attr_name, arrow_type, nullable=nullable))

    return pa.schema(fields)
