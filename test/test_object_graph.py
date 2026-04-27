from __future__ import annotations

from dataclasses import dataclass, field
from typing import cast

from py_ocsf_arrow.object_graph import (
    ObjectNode,
    SchemaLike,
    build_dependency_graph,
    calc_depth,
    calc_subtree_weight,
)


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


class TestBuildDependencyGraph:
    def test_empty_schema_returns_empty_graph(self):
        schema = cast(SchemaLike, FakeSchema())

        graph = build_dependency_graph(schema)

        assert graph == {}

    def test_single_class_reference_is_recorded(self):
        schema = cast(
            SchemaLike,
            FakeSchema(
                classes={
                    "example_class": FakeContainer(
                        name="example_class",
                        caption="Example Class",
                        attributes={"device": _object_attr("device")},
                    )
                },
                objects={
                    "device": FakeContainer(
                        name="device",
                        caption="Device",
                        attributes={"uid": _scalar_attr()},
                    )
                },
            ),
        )

        graph = build_dependency_graph(schema)

        assert graph["device"] == ObjectNode(
            name="device",
            caption="Device",
            referenced_by=[("class", "example_class", "device")],
            references=set(),
        )

    def test_diamond_dependency_records_object_fan_in(self):
        schema = cast(
            SchemaLike,
            FakeSchema(
                classes={
                    "finding": FakeContainer(
                        name="finding",
                        caption="Finding",
                        attributes={
                            "left": _object_attr("a"),
                            "right": _object_attr("b"),
                        },
                    )
                },
                objects={
                    "a": FakeContainer(
                        name="a",
                        caption="A",
                        attributes={"child": _object_attr("c")},
                    ),
                    "b": FakeContainer(
                        name="b",
                        caption="B",
                        attributes={"child": _object_attr("c")},
                    ),
                    "c": FakeContainer(
                        name="c",
                        caption="C",
                        attributes={"value": _scalar_attr()},
                    ),
                },
            ),
        )

        graph = build_dependency_graph(schema)

        assert len(graph["c"].referenced_by) == 2
        assert sorted(graph["c"].referenced_by) == [
            ("object", "a", "child"),
            ("object", "b", "child"),
        ]
        assert graph["a"].references == {"c"}
        assert graph["b"].references == {"c"}

    def test_self_reference_does_not_error(self):
        schema = cast(
            SchemaLike,
            FakeSchema(
                objects={
                    "process": FakeContainer(
                        name="process",
                        caption="Process",
                        attributes={
                            "uid": _scalar_attr(),
                            "parent_process": _object_attr("process"),
                        },
                    )
                }
            ),
        )

        graph = build_dependency_graph(schema)

        assert graph["process"].references == {"process"}
        assert graph["process"].referenced_by == [
            ("object", "process", "parent_process")
        ]
        assert calc_depth("process", schema) >= 0
        assert calc_subtree_weight("process", schema) >= 1

    def test_unknown_object_reference_is_skipped(self):
        schema = cast(
            SchemaLike,
            FakeSchema(
                classes={
                    "finding": FakeContainer(
                        name="finding",
                        caption="Finding",
                        attributes={"missing": _object_attr("missing_object")},
                    )
                },
                objects={
                    "device": FakeContainer(
                        name="device",
                        caption="Device",
                        attributes={"uid": _scalar_attr()},
                    )
                },
            ),
        )

        graph = build_dependency_graph(schema)

        assert graph["device"].referenced_by == []
        assert graph["device"].references == set()

    def test_fan_in_and_fan_out_counts_match_expected_graph(self):
        schema = cast(
            SchemaLike,
            FakeSchema(
                classes={
                    "finding": FakeContainer(
                        name="finding",
                        caption="Finding",
                        attributes={
                            "device": _object_attr("device"),
                            "user": _object_attr("user"),
                        },
                    )
                },
                objects={
                    "device": FakeContainer(
                        name="device",
                        caption="Device",
                        attributes={
                            "owner": _object_attr("user"),
                            "os": _object_attr("os"),
                        },
                    ),
                    "user": FakeContainer(
                        name="user",
                        caption="User",
                        attributes={"uid": _scalar_attr()},
                    ),
                    "os": FakeContainer(
                        name="os",
                        caption="OS",
                        attributes={"name": _scalar_attr()},
                    ),
                },
            ),
        )

        graph = build_dependency_graph(schema)

        assert len(graph["device"].referenced_by) == 1
        assert len(graph["device"].references) == 2
        assert len(graph["user"].referenced_by) == 2
        assert len(graph["user"].references) == 0
        assert len(graph["os"].referenced_by) == 1
        assert len(graph["os"].references) == 0


class TestDepthAndSubtreeWeight:
    def test_depth_for_simple_chain(self):
        schema = cast(
            SchemaLike,
            FakeSchema(
                objects={
                    "a": FakeContainer(
                        name="a",
                        caption="A",
                        attributes={"b": _object_attr("b")},
                    ),
                    "b": FakeContainer(
                        name="b",
                        caption="B",
                        attributes={"c": _object_attr("c")},
                    ),
                    "c": FakeContainer(
                        name="c",
                        caption="C",
                        attributes={"value": _scalar_attr()},
                    ),
                }
            ),
        )

        assert calc_depth("a", schema) == 2
        assert calc_depth("b", schema) == 1
        assert calc_depth("c", schema) == 0

    def test_subtree_weight_counts_root_and_children(self):
        schema = cast(
            SchemaLike,
            FakeSchema(
                objects={
                    "a": FakeContainer(
                        name="a",
                        caption="A",
                        attributes={
                            "scalar_1": _scalar_attr(),
                            "scalar_2": _scalar_attr(),
                            "child_b": _object_attr("b"),
                            "child_c": _object_attr("c"),
                            "child_unknown": _object_attr("missing"),
                        },
                    ),
                    "b": FakeContainer(
                        name="b",
                        caption="B",
                        attributes={
                            "b1": _scalar_attr(),
                            "b2": _scalar_attr(),
                            "b3": _scalar_attr(),
                        },
                    ),
                    "c": FakeContainer(
                        name="c",
                        caption="C",
                        attributes={
                            "c1": _scalar_attr(),
                            "c2": _scalar_attr(),
                        },
                    ),
                }
            ),
        )

        assert calc_subtree_weight("a", schema) == 10
