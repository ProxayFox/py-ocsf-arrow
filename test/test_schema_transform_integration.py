from __future__ import annotations

import pyarrow as pa
import pytest

from py_ocsf_arrow import SchemaGenerator, SchemaLoader
from py_ocsf_arrow.promotion import Verdict, run_promotion_analysis
from py_ocsf_arrow.schema_transform import (
    TransformConfig,
    TransformResult,
    apply_promotions,
)


OVERRIDES = {"metadata": Verdict.EMBED, "endpoint": Verdict.EMBED}


@pytest.fixture(scope="module")
def inclusive_generator(ocsf_client, ocsf_schema_1_8_0) -> SchemaGenerator:
    """Build a live 1.8.0 generator with all profiles and extensions enabled.

    The promotion analysis operates on the live compiled schema, which includes
    profile-backed attributes such as ``vulnerability_finding.device``. Using a
    profile-inclusive generator keeps the integration test aligned with that
    live model and lets us validate the exact end-to-end transform behavior.
    """

    profiles = list((ocsf_schema_1_8_0.profiles or {}).keys())
    extensions = list((ocsf_schema_1_8_0.extensions or {}).keys())
    return SchemaGenerator.init(
        client=ocsf_client,
        version="1.8.0",
        prf=profiles,
        ext=extensions,
    )


@pytest.fixture(scope="module")
def live_class_schemas(
    inclusive_generator: SchemaGenerator, ocsf_schema_1_8_0
) -> dict[str, pa.Schema]:
    """Build representative live class schemas for the full 1.8.0 surface."""

    return {
        class_name: inclusive_generator.build_class_schema(class_name)
        for class_name in sorted(ocsf_schema_1_8_0.classes)
    }


@pytest.fixture(scope="module")
def base_only_loader() -> SchemaLoader:
    """Provide the repo-default base-only loader path for invariance checks."""

    return SchemaLoader("1.8.0")


@pytest.fixture(scope="module")
def transform_result(
    live_class_schemas: dict[str, pa.Schema],
    ocsf_schema_1_8_0,
) -> TransformResult:
    """Run the full promotion + transformation pipeline once for this module."""

    analyses = run_promotion_analysis(ocsf_schema_1_8_0)
    return apply_promotions(
        live_class_schemas,
        ocsf_schema_1_8_0,
        analyses,
        TransformConfig(strict_review=False),
        overrides=OVERRIDES,
    )


def test_full_pipeline_transforms_all_live_class_schemas(
    live_class_schemas: dict[str, pa.Schema],
    ocsf_schema_1_8_0,
    transform_result: TransformResult,
):
    """The live pipeline should transform every generated 1.8.0 class schema."""

    assert len(live_class_schemas) == len(ocsf_schema_1_8_0.classes)
    assert len(transform_result.class_schemas) == len(live_class_schemas)


def test_vulnerability_finding_device_becomes_fk(
    live_class_schemas: dict[str, pa.Schema],
    transform_result: TransformResult,
):
    """Promoted ``device`` should become ``device_uid`` on vulnerability findings."""

    before = live_class_schemas["vulnerability_finding"]
    after = transform_result.class_schemas["vulnerability_finding"]

    assert pa.types.is_struct(before.field("device").type)
    assert "device" not in after.names
    assert after.field("device_uid").type == pa.utf8()

    metadata = after.field("device_uid").metadata or {}
    assert metadata[b"ocsf.ref_table"] == b"device"
    assert metadata[b"ocsf.ref_field"] == b"uid"
    assert metadata[b"ocsf.original_object"] == b"device"
    assert metadata[b"ocsf.original_field"] == b"device"


def test_metadata_override_keeps_metadata_embedded(
    transform_result: TransformResult,
):
    """Operator overrides should keep ``metadata`` embedded rather than promoted."""

    schema = transform_result.class_schemas["vulnerability_finding"]

    assert transform_result.verdicts["metadata"] == Verdict.EMBED
    assert "metadata_uid" not in schema.names
    assert pa.types.is_struct(schema.field("metadata").type)


def test_endpoint_override_prevents_endpoint_promotion(
    ocsf_schema_1_8_0,
    transform_result: TransformResult,
):
    """The abstract ``endpoint`` object should remain non-promoted under override."""

    endpoint_direct_refs = [
        (class_name, attr_name)
        for class_name, class_obj in ocsf_schema_1_8_0.classes.items()
        for attr_name, attr in class_obj.attributes.items()
        if getattr(attr, "object_type", None) == "endpoint"
    ]

    assert endpoint_direct_refs == []
    assert transform_result.verdicts["endpoint"] == Verdict.EMBED
    assert "endpoint" not in transform_result.promoted_schemas


def test_review_objects_stay_embedded_in_non_strict_mode(
    transform_result: TransformResult,
):
    """REVIEW objects should stay embedded when strict mode is disabled."""

    authentication = transform_result.class_schemas["authentication"]

    assert transform_result.verdicts["http_request"] == Verdict.REVIEW
    assert "http_request_uid" not in authentication.names
    assert pa.types.is_struct(authentication.field("http_request").type)


def test_authentication_network_endpoints_become_foreign_keys(
    transform_result: TransformResult,
):
    """Promoted network endpoints should rewrite both auth endpoint fields."""

    authentication = transform_result.class_schemas["authentication"]

    assert authentication.field("src_endpoint_uid").type == pa.utf8()
    assert authentication.field("dst_endpoint_uid").type == pa.utf8()
    assert "src_endpoint" not in authentication.names
    assert "dst_endpoint" not in authentication.names


def test_promoted_device_schema_keeps_non_promoted_children_embedded(
    transform_result: TransformResult,
):
    """Promoted child objects should become FKs, while embedded children stay structs."""

    device_schema = transform_result.promoted_schemas["device"]

    assert device_schema.field("uid").type == pa.utf8()
    assert device_schema.field("owner_uid").type == pa.utf8()
    assert "owner" not in device_schema.names
    assert pa.types.is_struct(device_schema.field("os").type)

    owner_metadata = device_schema.field("owner_uid").metadata or {}
    assert owner_metadata[b"ocsf.ref_table"] == b"user"
    assert owner_metadata[b"ocsf.original_field"] == b"owner"


def test_promoted_schema_count_and_warnings_are_stable(
    transform_result: TransformResult,
):
    """The live transform should produce a bounded promoted set with no warnings."""

    assert 15 <= len(transform_result.promoted_schemas) <= 25
    assert transform_result.warnings == []


def test_default_loader_schemas_remain_unchanged_after_opt_in_transform(
    base_only_loader: SchemaLoader,
    transform_result: TransformResult,
):
    """The opt-in transform must not mutate the repo's default loader path."""

    _ = transform_result
    before = base_only_loader.load_class("authentication")
    after = base_only_loader.load_class("authentication")

    assert before.equals(after)
    assert "src_endpoint" in after.names
    assert "src_endpoint_uid" not in after.names
