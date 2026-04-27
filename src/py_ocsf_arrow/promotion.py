"""Analyze OCSF objects for promotion suitability.

This module implements a configurable five-axis scoring model for deciding
whether an OCSF object looks like a candidate for promotion into a standalone
schema/table or should remain embedded.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from .object_graph import (
    AttributeLike,
    ObjectNode,
    SchemaLike,
    WithAttributesLike,
    build_dependency_graph,
    calc_depth,
    calc_subtree_weight,
)


class Verdict(str, Enum):
    """Promotion verdict emitted by the scoring model."""

    PROMOTE = "PROMOTE"
    REVIEW = "REVIEW"
    EMBED = "EMBED"


@dataclass(slots=True)
class ScoringConfig:
    """Hold configurable parameters for object-promotion scoring.

    The defaults are intentionally based on the real OCSF 1.8.0 metrics already
    observed in this repository:

    - ``device`` has subtree weight 313, fan-in 87, and fan-out 10
    - ``fingerprint`` has subtree weight 3, fan-in 97, and fan-out 0
    - ``os`` has subtree weight 13, fan-in 6, and fan-out 0

    These defaults therefore aim for:

    - subtree weight denominator large enough that mid-sized objects still have
      range below saturation, while very large objects like ``device`` cap out
    - fan-in denominator near the observed high fan-in range so widely reused
      objects do not all immediately collapse to the same value
    - fan-out denominator slightly above the observed ``device`` fan-out so the
      largest current objects land around 0.8–0.9 instead of clipping at 1.0
    - storage denominator large enough that tiny leaf/value objects remain near
      zero even with very high fan-in, while large embedded entities still show
      measurable duplication pressure
    """

    complexity_weight: float = 0.25
    connectivity_weight: float = 0.25
    entity_weight: float = 0.25
    storage_weight: float = 0.10
    queryability_weight: float = 0.15

    subtree_weight_denominator: float = 150.0
    depth_denominator: float = 3.0
    fan_in_denominator: float = 100.0
    fan_out_denominator: float = 12.0
    storage_denominator: float = 500_000.0

    complexity_subtree_factor_weight: float = 0.6
    complexity_depth_factor_weight: float = 0.4
    connectivity_fan_in_factor_weight: float = 0.4
    connectivity_fan_out_factor_weight: float = 0.6

    promote_threshold: float = 0.55
    review_threshold: float = 0.35
    avg_bytes_per_attr: float = 15.0
    depth_penalty_per_level: float = 10.0
    update_benefit_value: float = 20.0
    pass2_promote_threshold: float = 15.0
    pass2_review_threshold: float = 0.0

    identity_signal_names: frozenset[str] = field(
        default_factory=lambda: frozenset(
            {"uid", "uuid", "id", "name", "hostname", "ip"}
        )
    )
    value_signal_names: frozenset[str] = field(
        default_factory=lambda: frozenset(
            {"algorithm", "algorithm_id", "value", "label", "color"}
        )
    )
    value_meta_field_names: frozenset[str] = field(
        default_factory=lambda: frozenset({"caption", "type", "type_id"})
    )

    def __post_init__(self) -> None:
        """Validate threshold ordering and denominator ranges."""

        axis_weights = [
            self.complexity_weight,
            self.connectivity_weight,
            self.entity_weight,
            self.storage_weight,
            self.queryability_weight,
        ]
        if any(weight < 0.0 for weight in axis_weights):
            raise ValueError("Axis weights must be non-negative")
        if sum(axis_weights) <= 0.0:
            raise ValueError("At least one axis weight must be positive")

        denominators = [
            self.subtree_weight_denominator,
            self.depth_denominator,
            self.fan_in_denominator,
            self.fan_out_denominator,
            self.storage_denominator,
        ]
        if any(denominator <= 0.0 for denominator in denominators):
            raise ValueError("Normalization denominators must be positive")

        if self.promote_threshold < self.review_threshold:
            raise ValueError("promote_threshold must be >= review_threshold")


def _clamp_score(value: float) -> float:
    """Clamp *value* to the inclusive 0.0–1.0 scoring range."""

    return max(0.0, min(value, 1.0))


def _resolve_object_reference(attr: AttributeLike, schema: SchemaLike) -> str | None:
    """Return the referenced child object name for *attr*, if any."""

    object_type = getattr(attr, "object_type", None)
    if object_type and object_type in schema.objects:
        return object_type

    type_name = getattr(attr, "type", None)
    if type_name and type_name in schema.objects:
        return type_name

    return None


def _is_value_shaped(
    attr_names: set[str],
    config: ScoringConfig,
) -> bool:
    """Return True when *attr_names* only describe a value-like wrapper."""

    if not attr_names:
        return False
    allowed = config.value_signal_names | config.value_meta_field_names
    return all(attr_name in allowed for attr_name in attr_names)


@dataclass(slots=True)
class ObjectAnalysis:
    """Capture raw metrics, factor scores, and the final verdict for one object."""

    name: str
    caption: str
    attr_count: int
    scalar_attr_count: int
    object_attr_count: int
    class_fan_in: int
    object_fan_in: int
    fan_out: int
    depth: int
    has_identity_field: bool
    subtree_weight: int
    complexity_score: float
    connectivity_score: float
    entity_score: float
    storage_amplification_score: float
    queryability_score: float
    composite_score: float
    verdict: Verdict
    effective_depth: int | None = None
    pass2_benefit: float | None = None
    overridden: bool = False


def analyze_object(
    name: str,
    obj_def: WithAttributesLike,
    schema: SchemaLike,
    node: ObjectNode,
    config: ScoringConfig | None = None,
) -> ObjectAnalysis:
    """Analyze one OCSF object and return its promotion score breakdown."""

    cfg = ScoringConfig() if config is None else config

    attr_names = set(obj_def.attributes)
    object_attr_count = 0
    for attr in obj_def.attributes.values():
        if _resolve_object_reference(attr, schema) is not None:
            object_attr_count += 1

    attr_count = len(obj_def.attributes)
    scalar_attr_count = attr_count - object_attr_count

    class_fan_in = sum(1 for kind, _, _ in node.referenced_by if kind == "class")
    object_fan_in = sum(1 for kind, _, _ in node.referenced_by if kind == "object")
    total_fan_in = class_fan_in + object_fan_in
    fan_out = len(node.references)

    depth = calc_depth(name, schema)
    subtree_weight = calc_subtree_weight(name, schema)

    has_identity_field = bool(attr_names & set(cfg.identity_signal_names))
    value_shaped = _is_value_shaped(attr_names, cfg)

    complexity_weight_factor = _clamp_score(
        subtree_weight / cfg.subtree_weight_denominator
    )
    complexity_depth_factor = _clamp_score(depth / cfg.depth_denominator)
    complexity_score = (
        cfg.complexity_subtree_factor_weight * complexity_weight_factor
        + cfg.complexity_depth_factor_weight * complexity_depth_factor
    )

    fan_in_factor = _clamp_score(total_fan_in / cfg.fan_in_denominator)
    fan_out_factor = _clamp_score(fan_out / cfg.fan_out_denominator)
    connectivity_score = (
        cfg.connectivity_fan_in_factor_weight * fan_in_factor
        + cfg.connectivity_fan_out_factor_weight * fan_out_factor
    )

    if has_identity_field and not value_shaped:
        entity_score = 1.0
    elif has_identity_field and value_shaped:
        entity_score = 0.5
    elif object_attr_count > 0 and not value_shaped:
        entity_score = 0.3
    else:
        entity_score = 0.0

    storage_amplification_score = _clamp_score(
        (
            subtree_weight
            * cfg.avg_bytes_per_attr
            * total_fan_in
            / cfg.storage_denominator
        )
    )

    if has_identity_field and scalar_attr_count >= 4:
        queryability_score = 1.0
    elif has_identity_field and scalar_attr_count >= 2:
        queryability_score = 0.5
    else:
        queryability_score = 0.0

    composite_score = (
        complexity_score * cfg.complexity_weight
        + connectivity_score * cfg.connectivity_weight
        + entity_score * cfg.entity_weight
        + storage_amplification_score * cfg.storage_weight
        + queryability_score * cfg.queryability_weight
    )

    if composite_score >= cfg.promote_threshold:
        verdict = Verdict.PROMOTE
    elif composite_score >= cfg.review_threshold:
        verdict = Verdict.REVIEW
    else:
        verdict = Verdict.EMBED

    return ObjectAnalysis(
        name=name,
        caption=obj_def.caption or name,
        attr_count=attr_count,
        scalar_attr_count=scalar_attr_count,
        object_attr_count=object_attr_count,
        class_fan_in=class_fan_in,
        object_fan_in=object_fan_in,
        fan_out=fan_out,
        depth=depth,
        has_identity_field=has_identity_field,
        subtree_weight=subtree_weight,
        complexity_score=complexity_score,
        connectivity_score=connectivity_score,
        entity_score=entity_score,
        storage_amplification_score=storage_amplification_score,
        queryability_score=queryability_score,
        composite_score=composite_score,
        verdict=verdict,
    )


def _estimate_storage_savings(analysis: ObjectAnalysis, config: ScoringConfig) -> float:
    """Convert the normalized storage score into a pass-2 benefit proxy.

    Pass 1 keeps storage amplification normalized to the 0.0–1.0 range. For
    pass 2 we scale that score into the same rough band as the depth penalty and
    update-benefit values so deeper nested objects can be demoted meaningfully
    without recomputing a second, unrelated storage model.
    """

    return analysis.storage_amplification_score * config.pass2_promote_threshold


def _effective_depth(
    analysis: ObjectAnalysis,
    graph: dict[str, ObjectNode],
    pass1_verdicts: dict[str, Verdict],
) -> int:
    """Return the effective fact-table depth used by pass 2.

    The return values follow the planning rules:

    - ``1`` when an object is directly referenced by at least one class
    - ``2`` when it is only referenced by objects and at least one parent was
      already a pass-1 ``PROMOTE``
    - ``3`` as the representative value for ``3+`` when all known parents are
      nested/non-promoted objects
    - ``0`` when the object has no known parents in the provided schema view
    """

    if analysis.class_fan_in > 0:
        return 1
    if analysis.object_fan_in <= 0:
        return 0

    object_parents = {
        parent_name
        for parent_kind, parent_name, _ in graph[analysis.name].referenced_by
        if parent_kind == "object"
    }
    if any(
        pass1_verdicts.get(parent_name) == Verdict.PROMOTE
        for parent_name in object_parents
    ):
        return 2
    return 3


def run_promotion_analysis(
    schema: SchemaLike,
    config: ScoringConfig | None = None,
    overrides: dict[str, Verdict] | None = None,
) -> list[ObjectAnalysis]:
    """Run the full two-pass promotion analysis for every object in *schema*.

    This is the primary public entry point for downstream consumers. It:

    1. builds the full dependency graph
    2. runs pass-1 per-object scoring
    3. applies pass-2 depth/benefit adjustments to non-promoted objects
    4. applies final operator overrides
    5. returns the full analysis sorted by composite score descending
    """

    cfg = ScoringConfig() if config is None else config
    override_map = {} if overrides is None else overrides

    graph = build_dependency_graph(schema)
    analyses: list[ObjectAnalysis] = []
    for name, obj_def in schema.objects.items():
        analyses.append(analyze_object(name, obj_def, schema, graph[name], config=cfg))

    pass1_verdicts = {analysis.name: analysis.verdict for analysis in analyses}

    for analysis in analyses:
        if analysis.verdict == Verdict.PROMOTE:
            continue

        analysis.effective_depth = _effective_depth(analysis, graph, pass1_verdicts)
        storage_savings_estimate = _estimate_storage_savings(analysis, cfg)
        update_benefit = (
            cfg.update_benefit_value if analysis.has_identity_field else 0.0
        )
        analysis.pass2_benefit = (
            storage_savings_estimate
            + update_benefit
            - (analysis.effective_depth * cfg.depth_penalty_per_level)
        )

        if analysis.effective_depth <= 1:
            continue

        if analysis.pass2_benefit <= cfg.pass2_review_threshold:
            analysis.verdict = Verdict.EMBED
        elif analysis.pass2_benefit <= cfg.pass2_promote_threshold:
            analysis.verdict = Verdict.REVIEW
        else:
            analysis.verdict = Verdict.PROMOTE

    for analysis in analyses:
        if analysis.name not in override_map:
            continue
        analysis.verdict = override_map[analysis.name]
        analysis.overridden = True

    return sorted(analyses, key=lambda analysis: analysis.composite_score, reverse=True)
