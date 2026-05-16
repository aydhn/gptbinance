from typing import Dict, List
from app.program_plane.models import DependencyEdge
from app.program_plane.exceptions import InvalidDependencyEdge

class DependencyEdgeRegistry:
    def __init__(self):
        self._edges: Dict[str, DependencyEdge] = {}

    def register(self, edge: DependencyEdge):
        if not edge.source_id or not edge.target_id:
            raise InvalidDependencyEdge("Hidden dependency edge")
        self._edges[edge.dependency_id] = edge

    def get_dependencies(self, target_id: str) -> List[DependencyEdge]:
        return [e for e in self._edges.values() if e.target_id == target_id]
