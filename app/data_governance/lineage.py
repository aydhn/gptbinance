from typing import Dict, List, Optional
from app.data_governance.models import LineageNode, LineageEdge, DatasetRef
from app.data_governance.enums import LineageEdgeType
from app.data_governance.exceptions import LineageIntegrityError


class LineageGraph:
    def __init__(self):
        self._nodes: Dict[str, LineageNode] = {}
        self._edges: List[LineageEdge] = []

    def add_node(self, node: LineageNode):
        self._nodes[node.node_id] = node

    def add_edge(self, source_id: str, target_id: str, edge_type: LineageEdgeType):
        if source_id not in self._nodes or target_id not in self._nodes:
            raise LineageIntegrityError("Source or target node does not exist")
        # simple cycle guard
        if self._path_exists(target_id, source_id):
            raise LineageIntegrityError("Cycle detected in lineage graph")

        self._edges.append(
            LineageEdge(source_id=source_id, target_id=target_id, edge_type=edge_type)
        )

    def _path_exists(self, start: str, end: str, visited=None) -> bool:
        if visited is None:
            visited = set()
        if start == end:
            return True
        visited.add(start)
        for edge in self._edges:
            if edge.source_id == start and edge.target_id not in visited:
                if self._path_exists(edge.target_id, end, visited):
                    return True
        return False

    def get_upstream(self, node_id: str) -> List[LineageNode]:
        upstream_nodes = []
        for edge in self._edges:
            if edge.target_id == node_id:
                upstream_nodes.append(self._nodes[edge.source_id])
        return upstream_nodes

    def get_downstream(self, node_id: str) -> List[LineageNode]:
        downstream_nodes = []
        for edge in self._edges:
            if edge.source_id == node_id:
                downstream_nodes.append(self._nodes[edge.target_id])
        return downstream_nodes
