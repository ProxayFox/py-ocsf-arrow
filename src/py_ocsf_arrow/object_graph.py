"""Build and analyze OCSF object dependency graphs.

This module provides a small analysis layer over the live ``ocsf-lib`` schema
model. It records which OCSF objects are referenced by classes and other
objects, and exposes cycle-safe helpers for simple structural metrics such as
maximum nesting depth and subtree weight.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Protocol


class AttributeLike(Protocol):
    """Protocol for schema attributes used by the graph analysis helpers."""

    @property
    def type(self) -> str | None:
        """Return the declared OCSF type name for the attribute."""
        ...

    @property
    def object_type(self) -> str | None:
        """Return the referenced OCSF object name for object attributes."""
        ...


class WithAttributesLike(Protocol):
    """Protocol for schema classes and objects that expose attributes."""

    @property
    def name(self) -> str:
        """Return the schema object or class name."""
        ...

    @property
    def caption(self) -> str | None:
        """Return the optional human-readable label."""
        ...

    @property
    def attributes(self) -> Mapping[str, AttributeLike]:
        """Return the attribute mapping for the schema container."""
        ...


class SchemaLike(Protocol):
    """Protocol for schema views accepted by the graph helpers."""

    @property
    def classes(self) -> Mapping[str, WithAttributesLike]:
        """Return the schema's event classes by name."""
        ...

    @property
    def objects(self) -> Mapping[str, WithAttributesLike]:
        """Return the schema's reusable objects by name."""
        ...


@dataclass(slots=True)
class ObjectNode:
    """Represent one OCSF object and its graph relationships.

    Attributes
    ----------
    name:
        The object name/key from the OCSF schema.
    caption:
        Human-readable object label.
    referenced_by:
        List of ``(parent_kind, parent_name, attr_name)`` tuples recording who
        references this object. ``parent_kind`` is either ``"class"`` or
        ``"object"``.
    references:
        Set of child object names referenced by this object.
    """

    name: str
    caption: str
    referenced_by: list[tuple[str, str, str]] = field(default_factory=list)
    references: set[str] = field(default_factory=set)


def _iter_attributes(parent: WithAttributesLike):
    """Return the attribute items for *parent*.

    The live ``ocsf-lib`` model exposes attributes as a mapping, and the tests
    for this module use the same shape for synthetic fixtures.
    """

    return parent.attributes.items()


def _resolve_object_reference(
    attr: AttributeLike, available_objects: Mapping[str, WithAttributesLike]
) -> str | None:
    """Return the referenced object name for *attr*, if any.

    ``ocsf-lib`` exposes both ``object_type`` and ``type`` on ``OcsfAttr``.
    Prefer ``object_type`` when present, and fall back to ``type`` only when it
    matches a known object name in the provided schema view.
    """

    object_type = getattr(attr, "object_type", None)
    if object_type and object_type in available_objects:
        return object_type

    type_name = getattr(attr, "type", None)
    if type_name and type_name in available_objects:
        return type_name

    return None


def _object_children(name: str, schema: SchemaLike) -> set[str]:
    """Return the child object names referenced by object *name*."""

    if name not in schema.objects:
        return set()

    child_names: set[str] = set()
    parent = schema.objects[name]
    objects = schema.objects
    for _, attr in _iter_attributes(parent):
        child_name = _resolve_object_reference(attr, objects)
        if child_name is not None:
            child_names.add(child_name)

    return child_names


def build_dependency_graph(schema: SchemaLike) -> dict[str, ObjectNode]:
    """Build a complete directed object dependency graph from *schema*.

    The graph includes:

    - class-to-object references in ``ObjectNode.referenced_by``
    - object-to-object references in both ``referenced_by`` and ``references``

    Unknown object references are skipped silently so partial or synthetic
    schema views can still be analyzed.
    """

    objects = schema.objects
    classes = schema.classes

    graph: dict[str, ObjectNode] = {
        name: ObjectNode(name=name, caption=obj.caption or name)
        for name, obj in objects.items()
    }

    for class_name, event_class in classes.items():
        for attr_name, attr in _iter_attributes(event_class):
            child_name = _resolve_object_reference(attr, objects)
            if child_name is None:
                continue
            graph[child_name].referenced_by.append(("class", class_name, attr_name))

    for object_name, obj in objects.items():
        node = graph[object_name]
        for attr_name, attr in _iter_attributes(obj):
            child_name = _resolve_object_reference(attr, objects)
            if child_name is None:
                continue
            node.references.add(child_name)
            graph[child_name].referenced_by.append(("object", object_name, attr_name))

    return graph


def calc_depth(
    name: str,
    schema: SchemaLike,
    cache: dict[str, int] | None = None,
) -> int:
    """Return the maximum nested object depth below object *name*.

    A leaf object has depth ``0``. Cycles are broken by treating the repeated
    branch as already explored, preventing infinite recursion.
    """

    memo = {} if cache is None else cache

    def _inner(object_name: str, visiting: set[str]) -> int:
        if object_name in memo:
            return memo[object_name]
        if object_name in visiting or object_name not in schema.objects:
            return 0

        children = _object_children(object_name, schema)
        if not children:
            memo[object_name] = 0
            return 0

        next_visiting = set(visiting)
        next_visiting.add(object_name)
        depth = max(1 + _inner(child_name, next_visiting) for child_name in children)
        memo[object_name] = depth
        return depth

    return _inner(name, set())


def calc_subtree_weight(
    name: str,
    schema: SchemaLike,
    visited: set[str] | None = None,
) -> int:
    """Return the cycle-safe recursive attribute count for object *name*.

    The weight includes the root object's own attribute count plus the weights
    of nested child objects reachable from it. Once an object has been visited
    on the current traversal path, it is not counted again.
    """

    seen = set() if visited is None else set(visited)
    if name in seen or name not in schema.objects:
        return 0

    seen.add(name)

    obj = schema.objects[name]
    weight = len(obj.attributes)
    for child_name in _object_children(name, schema):
        weight += calc_subtree_weight(child_name, schema, seen)

    return weight
