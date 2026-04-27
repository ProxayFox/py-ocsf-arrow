from __future__ import annotations

from dataclasses import dataclass, field

import pyarrow as pa
import pytest

from py_ocsf_arrow.promotion import ObjectAnalysis, Verdict
from py_ocsf_arrow.schema_transform import (
    TransformConfig,
    apply_promotions,
    build_promoted_schema,
    transform_field,
    transform_schema,
)


@dataclass(slots=True)
class FakeTypeInfo:
    type_name: str | None
    type: str | None


@dataclass(slots=True)
class FakeAttr:
    type: str | None = None
    object_type: str | None = None
    is_array: bool = False
    requirement: str = "optional"


@dataclass(slots=True)
class FakeContainer:
    caption: str | None = None
    attributes: dict[str, FakeAttr] = field(default_factory=dict)


@dataclass(slots=True)
class FakeSchema:
    classes: dict[str, FakeContainer] = field(default_factory=dict)
    objects: dict[str, FakeContainer] = field(default_factory=dict)
    types: dict[str, FakeTypeInfo] = field(default_factory=dict)


def _analysis(name: str, verdict: Verdict) -> ObjectAnalysis:
    return ObjectAnalysis(
        name=name,
        caption=name.title(),
        attr_count=1,
        scalar_attr_count=1,
        object_attr_count=0,
        class_fan_in=0,
        object_fan_in=0,
        fan_out=0,
        depth=0,
        has_identity_field=False,
        subtree_weight=1,
        complexity_score=0.0,
        connectivity_score=0.0,
        entity_score=0.0,
        storage_amplification_score=0.0,
        queryability_score=0.0,
        composite_score=0.0,
        verdict=verdict,
    )


def _object_field_metadata(
    object_type: str, prefix: str = "ocsf"
) -> dict[bytes, bytes]:
    return {f"{prefix}.object_type".encode("utf-8"): object_type.encode("utf-8")}


class TestTransformField:
    def test_scalar_field_passes_through_unchanged(self):
        field = pa.field("name", pa.utf8())

        transformed = transform_field(field, {"device"}, TransformConfig())

        assert transformed.equals(field)

    def test_non_promoted_struct_field_passes_through_unchanged(self):
        field = pa.field("os", pa.struct([pa.field("name", pa.utf8())]))

        transformed = transform_field(field, {"device"}, TransformConfig())

        assert transformed.equals(field)

    def test_promoted_struct_field_replaced_with_fk(self):
        field = pa.field("device", pa.struct([pa.field("uid", pa.utf8())]))

        transformed = transform_field(field, {"device"}, TransformConfig())

        assert transformed.name == "device_uid"
        assert transformed.type == pa.utf8()
        assert transformed.metadata is not None

    def test_promoted_list_of_struct_replaced_with_list_of_fk(self):
        field = pa.field(
            "device",
            pa.list_(pa.struct([pa.field("uid", pa.utf8())])),
        )

        transformed = transform_field(field, {"device"}, TransformConfig())

        assert transformed.name == "device_uid"
        assert pa.types.is_list(transformed.type)
        assert transformed.type.value_type == pa.utf8()

    def test_fk_metadata_is_correct(self):
        field = pa.field(
            "device",
            pa.struct([pa.field("uid", pa.utf8())]),
            metadata={b"existing": b"value"},
        )

        transformed = transform_field(field, {"device"}, TransformConfig())
        metadata = transformed.metadata or {}

        assert metadata[b"existing"] == b"value"
        assert metadata[b"ocsf.ref_table"] == b"device"
        assert metadata[b"ocsf.ref_field"] == b"uid"
        assert metadata[b"ocsf.original_object"] == b"device"
        assert metadata[b"ocsf.original_field"] == b"device"


class TestTransformSchema:
    def test_schema_level_metadata_preserved(self):
        schema = pa.schema(
            [pa.field("device", pa.struct([pa.field("uid", pa.utf8())]))],
            metadata={b"schema": b"meta"},
        )

        transformed = transform_schema(schema, {"device"})

        assert transformed.metadata == schema.metadata
        assert transformed.field("device_uid").type == pa.utf8()


class TestBuildPromotedSchema:
    def test_promoted_object_standalone_schema_generation(self):
        schema = FakeSchema(
            objects={
                "device": FakeContainer(
                    caption="Device",
                    attributes={
                        "uid": FakeAttr(type="string_t", requirement="required"),
                        "name": FakeAttr(type="string_t"),
                        "os": FakeAttr(type="os", object_type="os"),
                        "owner": FakeAttr(type="user", object_type="user"),
                    },
                ),
                "os": FakeContainer(
                    caption="OS",
                    attributes={"name": FakeAttr(type="string_t")},
                ),
                "user": FakeContainer(
                    caption="User",
                    attributes={
                        "uid": FakeAttr(type="string_t", requirement="required")
                    },
                ),
            },
            types={},
        )

        promoted_schema = build_promoted_schema(
            "device",
            schema.objects["device"],
            schema,
            {"device", "user"},
        )

        assert promoted_schema.field("uid").type == pa.utf8()
        assert promoted_schema.field("name").type == pa.utf8()
        assert pa.types.is_struct(promoted_schema.field("os").type)
        assert promoted_schema.field("owner_uid").type == pa.utf8()
        assert promoted_schema.metadata is not None
        assert promoted_schema.metadata[b"ocsf.schema_kind"] == b"promoted_object"
        assert promoted_schema.metadata[b"ocsf.object_name"] == b"device"


class TestApplyPromotions:
    def test_review_handling_non_strict(self):
        schema = FakeSchema(
            classes={
                "finding": FakeContainer(
                    attributes={"user": FakeAttr(type="user", object_type="user")}
                )
            },
            objects={
                "user": FakeContainer(attributes={"uid": FakeAttr(type="string_t")})
            },
        )
        class_schema = pa.schema(
            [pa.field("user", pa.struct([pa.field("uid", pa.utf8())]))]
        )

        result = apply_promotions(
            {"finding": class_schema},
            schema,
            [_analysis("user", Verdict.REVIEW)],
            TransformConfig(strict_review=False),
        )

        assert (
            result.class_schemas["finding"].field("user").type
            == class_schema.field("user").type
        )
        assert result.promoted_schemas == {}

    def test_review_handling_strict(self):
        schema = FakeSchema(
            classes={
                "finding": FakeContainer(
                    attributes={"user": FakeAttr(type="user", object_type="user")}
                )
            },
            objects={
                "user": FakeContainer(attributes={"uid": FakeAttr(type="string_t")})
            },
        )
        class_schema = pa.schema(
            [pa.field("user", pa.struct([pa.field("uid", pa.utf8())]))]
        )

        with pytest.raises(ValueError, match="REVIEW verdicts"):
            apply_promotions(
                {"finding": class_schema},
                schema,
                [_analysis("user", Verdict.REVIEW)],
                TransformConfig(strict_review=True),
            )

    def test_full_apply_promotions_orchestration(self):
        schema = FakeSchema(
            classes={
                "finding_a": FakeContainer(
                    attributes={
                        "device": FakeAttr(type="device", object_type="device"),
                        "fingerprint": FakeAttr(
                            type="fingerprint", object_type="fingerprint"
                        ),
                        "user": FakeAttr(type="user", object_type="user"),
                    }
                ),
                "finding_b": FakeContainer(
                    attributes={"device": FakeAttr(type="device", object_type="device")}
                ),
            },
            objects={
                "device": FakeContainer(
                    attributes={
                        "uid": FakeAttr(type="string_t", requirement="required")
                    }
                ),
                "fingerprint": FakeContainer(
                    attributes={"value": FakeAttr(type="string_t")}
                ),
                "user": FakeContainer(
                    attributes={
                        "uid": FakeAttr(type="string_t", requirement="required")
                    }
                ),
            },
        )
        class_schemas = {
            "finding_a": pa.schema(
                [
                    pa.field("device", pa.struct([pa.field("uid", pa.utf8())])),
                    pa.field("fingerprint", pa.struct([pa.field("value", pa.utf8())])),
                    pa.field("user", pa.struct([pa.field("uid", pa.utf8())])),
                ]
            ),
            "finding_b": pa.schema(
                [pa.field("device", pa.struct([pa.field("uid", pa.utf8())]))]
            ),
        }
        analyses = [
            _analysis("device", Verdict.PROMOTE),
            _analysis("fingerprint", Verdict.EMBED),
            _analysis("user", Verdict.REVIEW),
        ]

        result = apply_promotions(class_schemas, schema, analyses, TransformConfig())

        assert result.class_schemas["finding_a"].field("device_uid").type == pa.utf8()
        assert pa.types.is_struct(
            result.class_schemas["finding_a"].field("fingerprint").type
        )
        assert pa.types.is_struct(result.class_schemas["finding_a"].field("user").type)
        assert list(result.promoted_schemas) == ["device"]
        assert result.verdicts["device"] == Verdict.PROMOTE

    def test_empty_promoted_set(self):
        schema = FakeSchema(
            classes={
                "finding": FakeContainer(
                    attributes={
                        "fingerprint": FakeAttr(
                            type="fingerprint", object_type="fingerprint"
                        )
                    }
                )
            },
            objects={
                "fingerprint": FakeContainer(
                    attributes={"value": FakeAttr(type="string_t")}
                )
            },
        )
        class_schema = pa.schema(
            [pa.field("fingerprint", pa.struct([pa.field("value", pa.utf8())]))]
        )

        result = apply_promotions(
            {"finding": class_schema},
            schema,
            [_analysis("fingerprint", Verdict.EMBED)],
        )

        assert result.class_schemas["finding"].equals(class_schema)
        assert result.promoted_schemas == {}

    def test_warnings_collected(self):
        schema = FakeSchema(
            classes={
                "finding": FakeContainer(
                    attributes={"device": FakeAttr(type="device", object_type="device")}
                )
            },
            objects={
                "device": FakeContainer(
                    attributes={
                        "uid": FakeAttr(type="string_t", requirement="required")
                    }
                )
            },
        )
        class_schema = pa.schema([pa.field("device", pa.utf8())])

        result = apply_promotions(
            {"finding": class_schema},
            schema,
            [_analysis("device", Verdict.PROMOTE)],
        )

        assert result.warnings
        assert "non-struct type" in result.warnings[0]
        assert result.class_schemas["finding"].field("device").type == pa.utf8()
