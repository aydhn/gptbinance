from typing import Dict, List, Optional
from app.supply_chain_plane.models import DependencyRecord, ComponentRef
from app.supply_chain_plane.exceptions import InvalidDependencyGraph


class DependencyRegistry:
    def __init__(self):
        self._dependencies: Dict[str, DependencyRecord] = {}

    def register_dependency(self, dependency: DependencyRecord) -> None:
        self._dependencies[dependency.dependency_id] = dependency

    def get_dependencies_for_component(
        self, component_id: str
    ) -> List[DependencyRecord]:
        return [
            d
            for d in self._dependencies.values()
            if d.source_component.component_id == component_id
        ]

    def get_dependencies_targeting_component(
        self, target_component_id: str
    ) -> List[DependencyRecord]:
        return [
            d
            for d in self._dependencies.values()
            if d.target_component.component_id == target_component_id
        ]
