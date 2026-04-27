from __future__ import annotations

import csv
import json
from io import StringIO

from py_ocsf_arrow.promotion import ObjectAnalysis, Verdict
from py_ocsf_arrow.promotion_report import format_summary, to_csv, to_json


def _analysis(
    name: str,
    verdict: Verdict,
    composite_score: float,
    *,
    caption: str | None = None,
) -> ObjectAnalysis:
    return ObjectAnalysis(
        name=name,
        caption=caption or name.title(),
        attr_count=4,
        scalar_attr_count=3,
        object_attr_count=1,
        class_fan_in=2,
        object_fan_in=1,
        fan_out=1,
        depth=2,
        has_identity_field=True,
        subtree_weight=12,
        complexity_score=0.6,
        connectivity_score=0.4,
        entity_score=1.0,
        storage_amplification_score=0.1,
        queryability_score=0.5,
        composite_score=composite_score,
        verdict=verdict,
        effective_depth=2,
        pass2_benefit=3.5,
        overridden=False,
    )


def test_json_output_is_valid():
    results = [
        _analysis("device", Verdict.PROMOTE, 0.9),
        _analysis("os", Verdict.EMBED, 0.2),
    ]

    payload = json.loads(to_json(results))

    assert len(payload) == 2
    assert payload[0]["name"] == "device"
    assert payload[0]["verdict"] == "PROMOTE"
    assert "class_fan_in" in payload[0]
    assert "pass2_benefit" in payload[0]


def test_csv_output_is_valid():
    results = [
        _analysis("device", Verdict.PROMOTE, 0.9),
        _analysis("os", Verdict.EMBED, 0.2),
    ]

    rows = list(csv.reader(StringIO(to_csv(results))))

    assert rows[0] == [
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
    assert len(rows) == 3


def test_summary_includes_all_verdict_counts():
    results = [
        _analysis("device", Verdict.PROMOTE, 0.9),
        _analysis("user", Verdict.REVIEW, 0.5),
        _analysis("os", Verdict.EMBED, 0.2),
    ]

    summary = format_summary(results)

    assert "PROMOTE: 1" in summary
    assert "REVIEW: 1" in summary
    assert "EMBED: 1" in summary


def test_empty_results_handled():
    assert json.loads(to_json([])) == []

    rows = list(csv.reader(StringIO(to_csv([]))))
    assert len(rows) == 1
    assert rows[0][0] == "name"

    summary = format_summary([])
    assert "Total objects: 0" in summary
    assert "PROMOTE: 0" in summary
    assert "REVIEW: 0" in summary
    assert "EMBED: 0" in summary
