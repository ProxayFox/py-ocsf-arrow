"""Reporting helpers for object-promotion analysis results."""

from __future__ import annotations

import csv
import io
import json
from collections import Counter

from .promotion import ObjectAnalysis, Verdict


def _sorted_results(results: list[ObjectAnalysis]) -> list[ObjectAnalysis]:
    """Return *results* sorted by composite score descending."""

    return sorted(results, key=lambda result: result.composite_score, reverse=True)


def _analysis_to_dict(result: ObjectAnalysis) -> dict[str, object]:
    """Convert one analysis result into a JSON-serializable mapping."""

    return {
        "name": result.name,
        "caption": result.caption,
        "attr_count": result.attr_count,
        "scalar_attr_count": result.scalar_attr_count,
        "object_attr_count": result.object_attr_count,
        "class_fan_in": result.class_fan_in,
        "object_fan_in": result.object_fan_in,
        "fan_out": result.fan_out,
        "depth": result.depth,
        "has_identity_field": result.has_identity_field,
        "subtree_weight": result.subtree_weight,
        "complexity_score": result.complexity_score,
        "connectivity_score": result.connectivity_score,
        "entity_score": result.entity_score,
        "storage_amplification_score": result.storage_amplification_score,
        "queryability_score": result.queryability_score,
        "composite_score": result.composite_score,
        "verdict": result.verdict.value,
        "effective_depth": result.effective_depth,
        "pass2_benefit": result.pass2_benefit,
        "overridden": result.overridden,
    }


def to_json(results: list[ObjectAnalysis]) -> str:
    """Serialize promotion-analysis results as pretty-printed JSON."""

    payload = [_analysis_to_dict(result) for result in _sorted_results(results)]
    return json.dumps(payload, indent=2)


def to_csv(results: list[ObjectAnalysis]) -> str:
    """Serialize promotion-analysis results as CSV with a fixed column order."""

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(
        [
            "name",
            "caption",
            "verdict",
            "composite_score",
            "complexity",
            "connectivity",
            "entity_score",
            "storage_amplification",
            "queryability",
            "class_fan_in",
            "object_fan_in",
            "fan_out",
            "depth",
            "subtree_weight",
            "attr_count",
            "effective_depth",
            "pass2_benefit",
            "overridden",
        ]
    )
    for result in _sorted_results(results):
        writer.writerow(
            [
                result.name,
                result.caption,
                result.verdict.value,
                result.composite_score,
                result.complexity_score,
                result.connectivity_score,
                result.entity_score,
                result.storage_amplification_score,
                result.queryability_score,
                result.class_fan_in,
                result.object_fan_in,
                result.fan_out,
                result.depth,
                result.subtree_weight,
                result.attr_count,
                result.effective_depth,
                result.pass2_benefit,
                result.overridden,
            ]
        )
    return output.getvalue()


def _format_ranked_section(title: str, results: list[ObjectAnalysis]) -> list[str]:
    """Format a ranked summary section for *results*."""

    lines = [title]
    if not results:
        lines.append("  (none)")
        return lines

    for index, result in enumerate(results, start=1):
        lines.append(
            f"  {index}. {result.name} ({result.caption}) - {result.composite_score:.6f}"
        )
    return lines


def format_summary(results: list[ObjectAnalysis]) -> str:
    """Return a human-readable summary of promotion-analysis verdicts."""

    ranked_results = _sorted_results(results)
    counts = Counter(result.verdict for result in ranked_results)
    promotes = [
        result for result in ranked_results if result.verdict == Verdict.PROMOTE
    ]
    reviews = [result for result in ranked_results if result.verdict == Verdict.REVIEW]
    embeds = [result for result in ranked_results if result.verdict == Verdict.EMBED]

    lines = [
        "Promotion analysis summary",
        f"Total objects: {len(ranked_results)}",
        f"PROMOTE: {counts[Verdict.PROMOTE]}",
        f"REVIEW: {counts[Verdict.REVIEW]}",
        f"EMBED: {counts[Verdict.EMBED]}",
        "",
    ]
    lines.extend(_format_ranked_section("PROMOTE objects:", promotes))
    lines.append("")
    lines.extend(_format_ranked_section("REVIEW objects:", reviews))
    lines.append("")
    lines.extend(_format_ranked_section("Top 5 EMBED near-misses:", embeds[:5]))
    return "\n".join(lines)
