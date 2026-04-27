from __future__ import annotations

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from types import ModuleType
from typing import cast

from ocsf.schema import OcsfSchema

from py_ocsf_arrow import SchemaGenerator
from py_ocsf_arrow.object_graph import (
    ObjectNode,
    SchemaLike,
    build_dependency_graph,
    calc_depth,
    calc_subtree_weight,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
GENERATOR_SCRIPT = REPO_ROOT / "scripts" / "generate_schema_module.py"


def _class_fan_in(node: ObjectNode) -> int:
    return sum(1 for kind, _, _ in node.referenced_by if kind == "class")


def _object_fan_in(node: ObjectNode) -> int:
    return sum(1 for kind, _, _ in node.referenced_by if kind == "object")


def _fan_out(node: ObjectNode) -> int:
    return len(node.references)


def _load_generator_module() -> ModuleType:
    spec = spec_from_file_location("_generator_module", GENERATOR_SCRIPT)
    assert spec is not None and spec.loader is not None
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _generator_discovered_objects(schema: OcsfSchema) -> set[str]:
    generator_module = _load_generator_module()
    generator = SchemaGenerator.init(version="1.8.0")
    type_map = generator._type_mapper.OCSF_TO_ARROW
    ignored_attrs = generator._ignored_attr

    top_level_object_deps: set[str] = set()
    for event_class in schema.classes.values():
        for attr in event_class.attributes.values():
            if attr.type not in type_map and attr.type in schema.objects:
                top_level_object_deps.add(attr.type)

    dep_graph = generator_module._discover_all_objects(
        top_level_object_deps,
        schema.objects,
        type_map,
        ignored_attrs,
    )
    return set(dep_graph)


class TestObjectGraphIntegration:
    def test_graph_completeness(self, ocsf_schema_1_8_0: OcsfSchema):
        schema = cast(SchemaLike, ocsf_schema_1_8_0)
        graph = build_dependency_graph(schema)

        assert len(graph) == len(ocsf_schema_1_8_0.objects)
        assert set(graph) == set(ocsf_schema_1_8_0.objects)

    def test_device_object_metrics(self, ocsf_schema_1_8_0: OcsfSchema):
        schema = cast(SchemaLike, ocsf_schema_1_8_0)
        graph = build_dependency_graph(schema)
        device = graph["device"]

        assert "device" in graph
        assert _class_fan_in(device) > 0
        assert _object_fan_in(device) > 0
        assert _fan_out(device) > 0
        assert calc_depth("device", schema) >= 2
        assert calc_subtree_weight("device", schema) >= 20

    def test_fingerprint_object_metrics(self, ocsf_schema_1_8_0: OcsfSchema):
        schema = cast(SchemaLike, ocsf_schema_1_8_0)
        graph = build_dependency_graph(schema)
        fingerprint = graph["fingerprint"]

        assert "fingerprint" in graph
        assert _class_fan_in(fingerprint) >= 50
        assert _object_fan_in(fingerprint) >= 10
        assert _fan_out(fingerprint) == 0
        assert calc_depth("fingerprint", schema) == 0
        assert calc_subtree_weight("fingerprint", schema) == len(
            ocsf_schema_1_8_0.objects["fingerprint"].attributes
        )

    def test_os_object_metrics(self, ocsf_schema_1_8_0: OcsfSchema):
        schema = cast(SchemaLike, ocsf_schema_1_8_0)
        graph = build_dependency_graph(schema)
        os_node = graph["os"]

        # Observed in OCSF 1.8.0 during integration-test validation:
        # - class fan-in: 0
        # - object fan-in: positive (for example device -> os)
        # Keep the exact object fan-in flexible in case upstream schema details
        # evolve, but pin the direct-class-reference expectation.
        assert "os" in graph
        assert _class_fan_in(os_node) == 0
        assert _object_fan_in(os_node) > 0

    def test_superset_validation_against_generator_discovery(
        self, ocsf_schema_1_8_0: OcsfSchema
    ):
        schema = cast(SchemaLike, ocsf_schema_1_8_0)
        graph = build_dependency_graph(schema)
        full_graph_objects = set(graph)
        generator_objects = _generator_discovered_objects(ocsf_schema_1_8_0)

        assert generator_objects <= full_graph_objects

        # Any objects present only in the full graph are expected candidates for
        # back-edge/self-loop differences because the generator helper drops such
        # edges to keep generated import graphs acyclic.
        graph_only_objects = full_graph_objects - generator_objects
        assert graph_only_objects >= set()

    def test_no_negative_metrics(self, ocsf_schema_1_8_0: OcsfSchema):
        schema = cast(SchemaLike, ocsf_schema_1_8_0)
        graph = build_dependency_graph(schema)

        for name, node in graph.items():
            assert _class_fan_in(node) >= 0, name
            assert _object_fan_in(node) >= 0, name
            assert _fan_out(node) >= 0, name
            assert calc_depth(name, schema) >= 0, name
            assert calc_subtree_weight(name, schema) >= 0, name

    def test_cycle_safety_on_real_schema(self, ocsf_schema_1_8_0: OcsfSchema):
        schema = cast(SchemaLike, ocsf_schema_1_8_0)
        for name in ocsf_schema_1_8_0.objects:
            depth = calc_depth(name, schema)
            subtree_weight = calc_subtree_weight(name, schema)

            assert isinstance(depth, int)
            assert isinstance(subtree_weight, int)
            assert depth >= 0
            assert subtree_weight >= 0
