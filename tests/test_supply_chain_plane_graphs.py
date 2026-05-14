import pytest
from app.supply_chain_plane.models import DependencyRecord, ComponentRef
from app.supply_chain_plane.enums import DependencyClass
from app.supply_chain_plane.dependencies import DependencyRegistry
from app.supply_chain_plane.graphs import DependencyGraphBuilder


def test_dependency_graph_cycle_detection():
    registry = DependencyRegistry()

    comp_a = ComponentRef(component_id="A")
    comp_b = ComponentRef(component_id="B")

    registry.register_dependency(
        DependencyRecord(
            dependency_id="dep-1",
            source_component=comp_a,
            target_component=comp_b,
            dependency_class=DependencyClass.DIRECT,
            criticality="high",
        )
    )
    registry.register_dependency(
        DependencyRecord(
            dependency_id="dep-2",
            source_component=comp_b,
            target_component=comp_a,
            dependency_class=DependencyClass.DIRECT,
            criticality="high",
        )
    )

    builder = DependencyGraphBuilder(registry)
    tree = builder.build_tree("tree-1", comp_a)

    assert tree.has_cycles is True
    assert len(tree.cycle_warnings) > 0
