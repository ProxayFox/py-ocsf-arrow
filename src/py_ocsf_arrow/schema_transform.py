"""Opt-in Arrow schema transformation for promoted OCSF objects.

This module implements Contract A for the project:

- non-promoted nested OCSF objects remain embedded as ``pa.struct(...)``
- promoted objects are represented by foreign-key reference fields in parent
  schemas and receive their own standalone Arrow schemas

The transform is intentionally post-processing oriented for class schemas so the
existing generation pipeline remains unchanged and opt-in. Standalone promoted
object schemas are built directly from the live OCSF object definitions because
finished ``pa.Schema`` objects do not preserve enough object-type context for
recursive promoted-child replacement.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Any, Protocol, cast

import pyarrow as pa

from .object_graph import SchemaLike
from .promotion import ObjectAnalysis, Verdict
from .type_map import TypeMapper


class TypeInfoLike(Protocol):
    """Protocol for OCSF type metadata used by scalar Arrow mapping."""

    type_name: str | None
    type: str | None


class WithAttributesLike(Protocol):
    """Protocol for OCSF objects and classes exposing attributes."""

    attributes: Mapping[str, Any]
    caption: str | None


class TransformSchemaLike(SchemaLike, Protocol):
    """Protocol for schema inputs that also expose OCSF type definitions."""

    types: Mapping[str, TypeInfoLike]


ArrowMetadata = dict[bytes | str, bytes | str]


@dataclass(slots=True)
class TransformConfig:
    """Control how promoted-object fields are rewritten into FK fields."""

    fk_type: pa.DataType = field(default_factory=pa.utf8)
    fk_suffix: str = "_uid"
    metadata_prefix: str = "ocsf"
    strict_review: bool = False


@dataclass(slots=True)
class TransformResult:
    """Capture the outcome of applying object-promotion transforms."""

    class_schemas: dict[str, pa.Schema]
    promoted_schemas: dict[str, pa.Schema]
    verdicts: dict[str, Verdict]
    warnings: list[str]


def _metadata_key(prefix: str, suffix: str) -> bytes:
    """Return a schema/field metadata key encoded for Arrow."""

    return f"{prefix}.{suffix}".encode("utf-8")


def _merge_metadata(
    existing: Mapping[bytes, bytes] | None,
    additions: Mapping[bytes, bytes],
) -> dict[bytes, bytes]:
    """Merge Arrow metadata dictionaries without dropping existing entries."""

    merged: dict[bytes, bytes] = dict(existing or {})
    for key, value in additions.items():
        merged[key] = value
    return merged


def _schema_metadata(schema: pa.Schema) -> ArrowMetadata | None:
    """Return schema metadata in a form accepted by Arrow's type stubs."""

    if schema.metadata is None:
        return None
    return cast(ArrowMetadata, dict(schema.metadata))


def _field_object_type(field: pa.Field, config: TransformConfig) -> str | None:
    """Return the OCSF object type encoded on *field*, if present."""

    metadata = field.metadata or {}
    for suffix in ("object_type", "original_object"):
        value = metadata.get(_metadata_key(config.metadata_prefix, suffix))
        if value:
            return value.decode("utf-8")
    return None


def _is_struct_like(field_type: pa.DataType) -> bool:
    """Return True when *field_type* is a struct or list-of-struct."""

    return pa.types.is_struct(field_type) or (
        pa.types.is_list(field_type)
        and pa.types.is_struct(cast(pa.DataType, field_type.value_type))
    )


def _fk_field_name(field_name: str, config: TransformConfig) -> str:
    """Return the foreign-key field name derived from *field_name*."""

    return f"{field_name}{config.fk_suffix}"


def _fk_metadata(
    field: pa.Field,
    object_name: str,
    config: TransformConfig,
) -> dict[bytes, bytes]:
    """Build the metadata payload attached to a transformed FK field."""

    return _merge_metadata(
        field.metadata,
        {
            _metadata_key(config.metadata_prefix, "ref_table"): object_name.encode(
                "utf-8"
            ),
            _metadata_key(config.metadata_prefix, "ref_field"): b"uid",
            _metadata_key(
                config.metadata_prefix, "original_object"
            ): object_name.encode("utf-8"),
            _metadata_key(config.metadata_prefix, "original_field"): field.name.encode(
                "utf-8"
            ),
        },
    )


def _with_object_type_metadata(
    field: pa.Field,
    object_type: str,
    config: TransformConfig,
) -> pa.Field:
    """Return *field* with internal object-type metadata attached."""

    return pa.field(
        field.name,
        field.type,
        nullable=field.nullable,
        metadata=_merge_metadata(
            field.metadata,
            {
                _metadata_key(
                    config.metadata_prefix, "object_type"
                ): object_type.encode("utf-8")
            },
        ),
    )


def transform_field(
    field: pa.Field,
    promoted_objects: set[str],
    config: TransformConfig,
) -> pa.Field:
    """Rewrite a promoted object field into an FK field when possible.

    The transform prefers explicit object-type metadata and falls back to the
    field name when no metadata is present. This keeps standalone synthetic
    schemas easy to test while allowing the orchestrator to enrich real class
    schemas with exact OCSF object-type information.
    """

    object_name = _field_object_type(field, config) or field.name
    if object_name not in promoted_objects:
        return field

    metadata = _fk_metadata(field, object_name, config)
    field_name = _fk_field_name(field.name, config)

    if pa.types.is_struct(field.type):
        return pa.field(
            field_name, config.fk_type, nullable=field.nullable, metadata=metadata
        )

    if pa.types.is_list(field.type) and pa.types.is_struct(field.type.value_type):
        return pa.field(
            field_name,
            pa.list_(config.fk_type),
            nullable=field.nullable,
            metadata=metadata,
        )

    return field


def transform_schema(
    schema: pa.Schema,
    promoted_objects: set[str],
    config: TransformConfig | None = None,
) -> pa.Schema:
    """Transform the top-level fields of *schema* using promotion verdicts."""

    cfg = TransformConfig() if config is None else config
    transformed_fields = [
        transform_field(field, promoted_objects, cfg) for field in schema
    ]
    return pa.schema(transformed_fields, metadata=_schema_metadata(schema))


def _resolve_scalar_arrow_type(
    schema: Any,
    type_name: str | None,
) -> pa.DataType:
    """Resolve a scalar OCSF type name into a PyArrow data type."""

    if type_name is None:
        return pa.string()

    if type_name in TypeMapper._BASE_OCSF_TYPES:
        return TypeMapper._BASE_OCSF_TYPES[type_name]

    type_info = schema.types.get(type_name)
    if type_info and type_info.type in TypeMapper._BASE_OCSF_TYPES:
        return TypeMapper._BASE_OCSF_TYPES[type_info.type]

    return pa.string()


def _build_embedded_struct_type(
    object_name: str,
    schema: Any,
    promoted_objects: set[str],
    config: TransformConfig,
    seen_objects: set[str],
) -> pa.DataType:
    """Build an embedded struct type for a non-promoted nested object.

    Contract A intentionally keeps non-promoted children as nested structs.
    Cycles are broken with a string fallback to mirror the existing generator's
    defensive behavior.
    """

    if object_name in seen_objects:
        return pa.string()

    nested_seen = set(seen_objects)
    nested_seen.add(object_name)
    nested_fields = _build_object_fields(
        schema.objects[object_name],
        schema,
        promoted_objects,
        config,
        nested_seen,
    )
    return pa.struct(nested_fields)


def _build_attribute_field(
    attr_name: str,
    attr: Any,
    schema: Any,
    promoted_objects: set[str],
    config: TransformConfig,
    seen_objects: set[str],
) -> pa.Field:
    """Convert one OCSF attribute into an Arrow field for object schemas."""

    nullable = attr.requirement != "required"
    object_name = attr.object_type if attr.object_type in schema.objects else None

    if object_name is not None:
        if object_name in promoted_objects:
            base_field = pa.field(
                attr_name,
                pa.list_(pa.struct([])) if attr.is_array else pa.struct([]),
                nullable=nullable,
                metadata={
                    _metadata_key(
                        config.metadata_prefix, "object_type"
                    ): object_name.encode("utf-8")
                },
            )
            return transform_field(base_field, promoted_objects, config)

        nested_type = _build_embedded_struct_type(
            object_name,
            schema,
            promoted_objects,
            config,
            seen_objects,
        )
        if attr.is_array:
            nested_type = pa.list_(nested_type)
        return pa.field(attr_name, nested_type, nullable=nullable)

    scalar_type = _resolve_scalar_arrow_type(schema, attr.type)
    if attr.is_array:
        scalar_type = pa.list_(scalar_type)
    return pa.field(attr_name, scalar_type, nullable=nullable)


def _build_object_fields(
    obj_def: Any,
    schema: Any,
    promoted_objects: set[str],
    config: TransformConfig,
    seen_objects: set[str],
) -> list[pa.Field]:
    """Build Arrow fields for a promoted-object schema recursively."""

    return [
        _build_attribute_field(
            attr_name,
            attr,
            schema,
            promoted_objects,
            config,
            seen_objects,
        )
        for attr_name, attr in sorted(obj_def.attributes.items())
    ]


def build_promoted_schema(
    name: str,
    obj_def: Any,
    schema: Any,
    promoted_objects: set[str],
    config: TransformConfig | None = None,
) -> pa.Schema:
    """Build a standalone Arrow schema for one promoted OCSF object.

    Non-promoted children remain embedded structs per Contract A. Promoted
    child objects become FK fields recursively.
    """

    cfg = TransformConfig() if config is None else config
    fields = _build_object_fields(obj_def, schema, promoted_objects, cfg, {name})
    metadata: ArrowMetadata = {
        _metadata_key(cfg.metadata_prefix, "schema_kind"): b"promoted_object",
        _metadata_key(cfg.metadata_prefix, "object_name"): name.encode("utf-8"),
    }
    return pa.schema(fields, metadata=metadata)


def _build_verdict_map(
    analyses: list[ObjectAnalysis],
    overrides: dict[str, Verdict] | None,
) -> dict[str, Verdict]:
    """Return the effective verdict map after overrides."""

    verdicts = {analysis.name: analysis.verdict for analysis in analyses}
    for name, verdict in (overrides or {}).items():
        verdicts[name] = verdict
    return verdicts


def _class_object_types(
    class_name: str,
    schema: SchemaLike,
) -> dict[str, str]:
    """Return a top-level field-name to object-type mapping for one class."""

    if class_name not in schema.classes:
        return {}
    result: dict[str, str] = {}
    for attr_name, attr in schema.classes[class_name].attributes.items():
        object_type = getattr(attr, "object_type", None)
        if object_type and object_type in schema.objects:
            result[attr_name] = object_type
    return result


def apply_promotions(
    class_schemas: dict[str, pa.Schema],
    schema: Any,
    analyses: list[ObjectAnalysis],
    config: TransformConfig | None = None,
    overrides: dict[str, Verdict] | None = None,
) -> TransformResult:
    """Apply promotion verdicts to class schemas and build promoted schemas."""

    cfg = TransformConfig() if config is None else config
    verdicts = _build_verdict_map(analyses, overrides)

    review_objects = sorted(
        name for name, verdict in verdicts.items() if verdict == Verdict.REVIEW
    )
    if cfg.strict_review and review_objects:
        raise ValueError(
            "REVIEW verdicts encountered in strict mode: " + ", ".join(review_objects)
        )

    promoted_objects = {
        name for name, verdict in verdicts.items() if verdict == Verdict.PROMOTE
    }
    warnings: list[str] = []
    transformed_class_schemas: dict[str, pa.Schema] = {}

    for class_name, class_schema in class_schemas.items():
        object_types = _class_object_types(class_name, schema)
        enriched_fields: list[pa.Field] = []
        for schema_field in class_schema:
            object_type = object_types.get(schema_field.name) or _field_object_type(
                schema_field, cfg
            )
            enriched_field = schema_field
            if object_type is not None:
                enriched_field = _with_object_type_metadata(
                    schema_field, object_type, cfg
                )

            promoted_name = object_type or schema_field.name
            if promoted_name in promoted_objects and not _is_struct_like(
                schema_field.type
            ):
                warnings.append(
                    f"Class schema '{class_name}' field '{schema_field.name}' references promoted object "
                    f"'{promoted_name}' but has non-struct type '{schema_field.type}'."
                )

            enriched_fields.append(enriched_field)

        enriched_schema = pa.schema(
            enriched_fields, metadata=_schema_metadata(class_schema)
        )
        transformed_class_schemas[class_name] = transform_schema(
            enriched_schema,
            promoted_objects,
            cfg,
        )

    promoted_schemas = {
        name: build_promoted_schema(
            name, schema.objects[name], schema, promoted_objects, cfg
        )
        for name in sorted(promoted_objects)
        if name in schema.objects
    }

    return TransformResult(
        class_schemas=transformed_class_schemas,
        promoted_schemas=promoted_schemas,
        verdicts=verdicts,
        warnings=warnings,
    )
