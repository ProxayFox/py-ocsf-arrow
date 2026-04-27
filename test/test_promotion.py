from __future__ import annotations

from dataclasses import dataclass, field
from typing import cast

import pytest

from py_ocsf_arrow.object_graph import SchemaLike, build_dependency_graph
from py_ocsf_arrow.promotion import ScoringConfig, Verdict, analyze_object


@dataclass(slots=True)
class FakeAttr:
    type: str | None = None
    object_type: str | None = None


@dataclass(slots=True)
class FakeContainer:
    name: str
    caption: str
    attributes: dict[str, FakeAttr] = field(default_factory=dict)


@dataclass(slots=True)
class FakeSchema:
    classes: dict[str, FakeContainer] = field(default_factory=dict)
    objects: dict[str, FakeContainer] = field(default_factory=dict)


def _scalar_attr(type_name: str = "string_t") -> FakeAttr:
    return FakeAttr(type=type_name, object_type=None)


def _object_attr(object_name: str) -> FakeAttr:
    return FakeAttr(type=object_name, object_type=object_name)


def _analyze(schema: FakeSchema, object_name: str, config: ScoringConfig | None = None):
    typed_schema = cast(SchemaLike, schema)
    graph = build_dependency_graph(typed_schema)
    return analyze_object(
        object_name,
        typed_schema.objects[object_name],
        typed_schema,
        graph[object_name],
        config=config,
    )


class TestPromotionScoring:
    def test_entity_like_object_scores_high(self):
        schema = FakeSchema(
            classes={
                **{
                    f"class_{i}": FakeContainer(
                        name=f"class_{i}",
                        caption=f"Class {i}",
                        attributes={"entity": _object_attr("entity")},
                    )
                    for i in range(15)
                }
            },
            objects={
                "entity": FakeContainer(
                    name="entity",
                    caption="Entity",
                    attributes={
                        "uid": _scalar_attr(),
                        "name": _scalar_attr(),
                        "hostname": _scalar_attr(),
                        "ip": _scalar_attr(),
                        "owner": _scalar_attr(),
                        "region": _scalar_attr(),
                        "os": _object_attr("os"),
                        "location": _object_attr("location"),
                        "user": _object_attr("user"),
                        "network": _object_attr("network"),
                    },
                ),
                "os": FakeContainer(
                    name="os",
                    caption="OS",
                    attributes={
                        "name": _scalar_attr(),
                        "version": _scalar_attr(),
                        "build": _scalar_attr(),
                        "kernel": _object_attr("kernel"),
                    },
                ),
                "kernel": FakeContainer(
                    name="kernel",
                    caption="Kernel",
                    attributes={
                        "release": _scalar_attr(),
                        "arch": _scalar_attr(),
                        "family": _scalar_attr(),
                    },
                ),
                "location": FakeContainer(
                    name="location",
                    caption="Location",
                    attributes={
                        "city": _scalar_attr(),
                        "country": _scalar_attr(),
                        "region": _scalar_attr(),
                        "geo": _object_attr("geo"),
                    },
                ),
                "geo": FakeContainer(
                    name="geo",
                    caption="Geo",
                    attributes={
                        "lat": _scalar_attr(),
                        "lon": _scalar_attr(),
                        "timezone": _scalar_attr(),
                    },
                ),
                "user": FakeContainer(
                    name="user",
                    caption="User",
                    attributes={
                        "uid": _scalar_attr(),
                        "name": _scalar_attr(),
                        "email": _scalar_attr(),
                        "group": _object_attr("group"),
                    },
                ),
                "group": FakeContainer(
                    name="group",
                    caption="Group",
                    attributes={
                        "name": _scalar_attr(),
                        "scope": _scalar_attr(),
                        "desc": _scalar_attr(),
                    },
                ),
                "network": FakeContainer(
                    name="network",
                    caption="Network",
                    attributes={
                        "subnet": _scalar_attr(),
                        "vpc": _scalar_attr(),
                        "zone": _scalar_attr(),
                        "interface": _object_attr("interface"),
                    },
                ),
                "interface": FakeContainer(
                    name="interface",
                    caption="Interface",
                    attributes={
                        "name": _scalar_attr(),
                        "mac": _scalar_attr(),
                        "speed": _scalar_attr(),
                    },
                ),
            },
        )

        analysis = _analyze(schema, "entity")

        assert analysis.entity_score == 1.0
        assert analysis.composite_score > 0.55
        assert analysis.verdict == Verdict.PROMOTE

    def test_value_like_object_scores_low(self):
        schema = FakeSchema(
            classes={
                **{
                    f"class_{i}": FakeContainer(
                        name=f"class_{i}",
                        caption=f"Class {i}",
                        attributes={"fingerprint": _object_attr("fingerprint")},
                    )
                    for i in range(40)
                }
            },
            objects={
                "fingerprint": FakeContainer(
                    name="fingerprint",
                    caption="Fingerprint",
                    attributes={
                        "algorithm": _scalar_attr(),
                        "algorithm_id": _scalar_attr("integer_t"),
                        "value": _scalar_attr(),
                    },
                )
            },
        )

        analysis = _analyze(schema, "fingerprint")

        assert analysis.entity_score == 0.0
        assert analysis.composite_score < 0.35
        assert analysis.verdict == Verdict.EMBED

    def test_high_fan_in_value_shape_stays_embed(self):
        schema = FakeSchema(
            classes={
                **{
                    f"class_{i}": FakeContainer(
                        name=f"class_{i}",
                        caption=f"Class {i}",
                        attributes={"hash": _object_attr("fingerprint")},
                    )
                    for i in range(80)
                }
            },
            objects={
                "wrapper": FakeContainer(
                    name="wrapper",
                    caption="Wrapper",
                    attributes={"hash": _object_attr("fingerprint")},
                ),
                "fingerprint": FakeContainer(
                    name="fingerprint",
                    caption="Fingerprint",
                    attributes={
                        "algorithm": _scalar_attr(),
                        "algorithm_id": _scalar_attr("integer_t"),
                        "value": _scalar_attr(),
                    },
                ),
            },
        )

        analysis = _analyze(schema, "fingerprint")

        assert analysis.class_fan_in >= 80
        assert analysis.fan_out == 0
        assert analysis.verdict == Verdict.EMBED

    def test_object_with_subobjects_but_no_identity_gets_partial_entity_score(self):
        schema = FakeSchema(
            objects={
                "resource_bundle": FakeContainer(
                    name="resource_bundle",
                    caption="Resource Bundle",
                    attributes={
                        "desc": _scalar_attr(),
                        "device": _object_attr("device"),
                    },
                ),
                "device": FakeContainer(
                    name="device",
                    caption="Device",
                    attributes={"uid": _scalar_attr(), "name": _scalar_attr()},
                ),
            }
        )

        analysis = _analyze(schema, "resource_bundle")

        assert analysis.object_attr_count > 0
        assert analysis.has_identity_field is False
        assert analysis.entity_score == 0.3

    def test_exact_promote_threshold_is_promote(self):
        schema = FakeSchema(
            objects={
                "queryable": FakeContainer(
                    name="queryable",
                    caption="Queryable",
                    attributes={
                        "uid": _scalar_attr(),
                        "name": _scalar_attr(),
                        "host": _scalar_attr(),
                        "region": _scalar_attr(),
                    },
                )
            }
        )
        config = ScoringConfig(
            complexity_weight=0.0,
            connectivity_weight=0.0,
            entity_weight=0.0,
            storage_weight=0.0,
            queryability_weight=0.55,
            promote_threshold=0.55,
            review_threshold=0.35,
        )

        analysis = _analyze(schema, "queryable", config=config)

        assert analysis.composite_score == pytest.approx(0.55)
        assert analysis.verdict == Verdict.PROMOTE

    def test_exact_review_threshold_is_review(self):
        schema = FakeSchema(
            objects={
                "queryable": FakeContainer(
                    name="queryable",
                    caption="Queryable",
                    attributes={
                        "uid": _scalar_attr(),
                        "name": _scalar_attr(),
                        "host": _scalar_attr(),
                        "region": _scalar_attr(),
                    },
                )
            }
        )
        config = ScoringConfig(
            complexity_weight=0.0,
            connectivity_weight=0.0,
            entity_weight=0.0,
            storage_weight=0.0,
            queryability_weight=0.35,
            promote_threshold=0.55,
            review_threshold=0.35,
        )

        analysis = _analyze(schema, "queryable", config=config)

        assert analysis.composite_score == pytest.approx(0.35)
        assert analysis.verdict == Verdict.REVIEW

    def test_below_review_threshold_is_embed(self):
        schema = FakeSchema(
            objects={
                "queryable": FakeContainer(
                    name="queryable",
                    caption="Queryable",
                    attributes={
                        "uid": _scalar_attr(),
                        "name": _scalar_attr(),
                        "host": _scalar_attr(),
                        "region": _scalar_attr(),
                    },
                )
            }
        )
        config = ScoringConfig(
            complexity_weight=0.0,
            connectivity_weight=0.0,
            entity_weight=0.0,
            storage_weight=0.0,
            queryability_weight=0.34,
            promote_threshold=0.55,
            review_threshold=0.35,
        )

        analysis = _analyze(schema, "queryable", config=config)

        assert analysis.composite_score == pytest.approx(0.34)
        assert analysis.verdict == Verdict.EMBED

    def test_custom_scoring_config_changes_composite(self):
        schema = FakeSchema(
            objects={
                "entity": FakeContainer(
                    name="entity",
                    caption="Entity",
                    attributes={
                        "uid": _scalar_attr(),
                        "name": _scalar_attr(),
                        "region": _scalar_attr(),
                        "device": _object_attr("device"),
                    },
                ),
                "device": FakeContainer(
                    name="device",
                    caption="Device",
                    attributes={"uid": _scalar_attr(), "name": _scalar_attr()},
                ),
            }
        )

        default_analysis = _analyze(schema, "entity")
        custom_analysis = _analyze(
            schema,
            "entity",
            config=ScoringConfig(
                complexity_weight=0.0,
                connectivity_weight=0.0,
                entity_weight=1.0,
                storage_weight=0.0,
                queryability_weight=0.0,
            ),
        )

        assert custom_analysis.composite_score != default_analysis.composite_score
        assert custom_analysis.composite_score == pytest.approx(
            custom_analysis.entity_score
        )

    @pytest.mark.parametrize(
        ("attributes", "expected_queryability"),
        [
            ({"uid", "name", "owner", "region"}, 1.0),
            ({"uid", "name"}, 0.5),
            ({"algorithm", "value"}, 0.0),
        ],
    )
    def test_queryability_tiers(
        self, attributes: set[str], expected_queryability: float
    ):
        schema = FakeSchema(
            objects={
                "candidate": FakeContainer(
                    name="candidate",
                    caption="Candidate",
                    attributes={attr: _scalar_attr() for attr in attributes},
                )
            }
        )

        analysis = _analyze(schema, "candidate")

        assert analysis.queryability_score == expected_queryability

    def test_complexity_uses_subtree_weight_and_depth(self):
        schema = FakeSchema(
            objects={
                "deep": FakeContainer(
                    name="deep",
                    caption="Deep",
                    attributes={"mid": _object_attr("mid")},
                ),
                "mid": FakeContainer(
                    name="mid",
                    caption="Mid",
                    attributes={"leaf": _object_attr("leaf")},
                ),
                "leaf": FakeContainer(
                    name="leaf",
                    caption="Leaf",
                    attributes={"value": _scalar_attr()},
                ),
                "shallow": FakeContainer(
                    name="shallow",
                    caption="Shallow",
                    attributes={
                        "leaf_flat": _object_attr("leaf_flat"),
                        "value": _scalar_attr(),
                    },
                ),
                "leaf_flat": FakeContainer(
                    name="leaf_flat",
                    caption="Leaf Flat",
                    attributes={"value": _scalar_attr()},
                ),
            }
        )

        deep_analysis = _analyze(schema, "deep")
        shallow_analysis = _analyze(schema, "shallow")

        assert deep_analysis.subtree_weight == shallow_analysis.subtree_weight
        assert deep_analysis.depth > shallow_analysis.depth
        assert deep_analysis.complexity_score > shallow_analysis.complexity_score
