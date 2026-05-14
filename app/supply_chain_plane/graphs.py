from typing import Dict, List, Set
from app.supply_chain_plane.models import DependencyTree, DependencyRecord, ComponentRef
from app.supply_chain_plane.dependencies import DependencyRegistry


class DependencyGraphBuilder:
    def __init__(self, registry: DependencyRegistry):
        self.registry = registry

    def build_tree(self, tree_id: str, root_ref: ComponentRef) -> DependencyTree:
        visited: Set[str] = set()
        dependencies: List[DependencyRecord] = []
        cycle_warnings: List[str] = []

        def traverse(comp_ref: ComponentRef, path: List[str]):
            if comp_ref.component_id in path:
                cycle_warnings.append(
                    f"Cycle detected: {' -> '.join(path)} -> {comp_ref.component_id}"
                )
                return

            if comp_ref.component_id in visited:
                return

            visited.add(comp_ref.component_id)
            path.append(comp_ref.component_id)

            deps = self.registry.get_dependencies_for_component(comp_ref.component_id)
            for dep in deps:
                dependencies.append(dep)
                traverse(dep.target_component, list(path))

        traverse(root_ref, [])

        return DependencyTree(
            tree_id=tree_id,
            root_component=root_ref,
            dependencies=dependencies,
            has_cycles=len(cycle_warnings) > 0,
            cycle_warnings=cycle_warnings,
        )
