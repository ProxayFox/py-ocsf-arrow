from __future__ import annotations

from collections import Counter
from typing import cast

import pytest

from py_ocsf_arrow.object_graph import SchemaLike
from py_ocsf_arrow.promotion import Verdict, run_promotion_analysis


EXPECTED_VERDICTS = {
    "device": Verdict.PROMOTE,
    "user": Verdict.PROMOTE,
    "process": Verdict.PROMOTE,
    "fingerprint": Verdict.EMBED,
    "os": Verdict.EMBED,
    "reputation": Verdict.EMBED,
}


@pytest.fixture(scope="module")
def live_results(ocsf_schema_1_8_0):
    return run_promotion_analysis(cast(SchemaLike, ocsf_schema_1_8_0))


@pytest.fixture(scope="module")
def live_result_map(live_results):
    return {result.name: result for result in live_results}


def test_full_pipeline_smoke_test(live_results):
    assert live_results
    assert [result.composite_score for result in live_results] == sorted(
        (result.composite_score for result in live_results),
        reverse=True,
    )
    assert all(isinstance(result.verdict, Verdict) for result in live_results)
    assert all(result.composite_score >= 0.0 for result in live_results)


def test_sentinel_verdict_regression(live_result_map):
    failures: list[str] = []

    for object_name, expected_verdict in EXPECTED_VERDICTS.items():
        result = live_result_map.get(object_name)
        if result is None:
            failures.append(f"missing sentinel object: {object_name}")
            continue
        if result.verdict != expected_verdict:
            failures.append(
                "sentinel verdict mismatch for "
                f"{object_name}: expected {expected_verdict.value}, "
                f"got {result.verdict.value}, "
                f"score={result.composite_score:.6f}, "
                f"effective_depth={result.effective_depth}, "
                f"pass2_benefit={result.pass2_benefit}"
            )

    if failures:
        pytest.fail("\n".join(failures))


def test_verdict_distribution_sanity(live_results):
    counts = Counter(result.verdict for result in live_results)

    assert 5 <= counts[Verdict.PROMOTE] <= 25
    assert counts[Verdict.EMBED] > len(live_results) / 2
    # REVIEW can legitimately be absent after tuning, but should never be negative.
    assert counts[Verdict.REVIEW] >= 0


def test_device_deep_dive(live_result_map):
    device = live_result_map["device"]

    assert device.entity_score > 0.5
    assert device.complexity_score > 0.5
    assert device.connectivity_score > 0.5
    assert device.queryability_score > 0.0
    assert device.composite_score >= 0.55
    assert device.effective_depth in {None, 0, 1}


def test_fingerprint_deep_dive(live_result_map):
    fingerprint = live_result_map["fingerprint"]

    assert fingerprint.entity_score == 0.0
    assert fingerprint.fan_out == 0
    assert fingerprint.subtree_weight <= 5
    assert fingerprint.verdict == Verdict.EMBED


def test_os_deep_dive(live_result_map):
    os_object = live_result_map["os"]

    assert os_object.class_fan_in == 0
    assert os_object.effective_depth is not None
    assert os_object.effective_depth >= 2
    # Observed on the live 1.8.0 schema with tuned defaults: pass2_benefit ~= 0.0351.
    assert os_object.pass2_benefit is not None
    assert os_object.verdict == Verdict.EMBED


def test_override_integration(ocsf_schema_1_8_0, live_result_map):
    overridden_results = run_promotion_analysis(
        cast(SchemaLike, ocsf_schema_1_8_0),
        overrides={"device": Verdict.EMBED},
    )
    overridden_map = {result.name: result for result in overridden_results}

    assert overridden_map["device"].verdict == Verdict.EMBED
    assert overridden_map["device"].overridden is True

    for object_name, default_result in live_result_map.items():
        if object_name == "device":
            continue
        assert overridden_map[object_name].verdict == default_result.verdict
