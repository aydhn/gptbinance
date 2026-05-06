from typing import List, Set

from app.evidence_graph.artefacts import ArtefactRegistry
from app.evidence_graph.relations import RelationRegistry
from app.evidence_graph.models import LineageTraversal, ArtefactRecord, RelationEdge
from app.evidence_graph.enums import TraversalClass, CompletenessClass
from app.evidence_graph.exceptions import LineageTraversalError


class LineageEngine:
    def __init__(
        self, artefact_registry: ArtefactRegistry, relation_registry: RelationRegistry
    ):
        self.artefact_registry = artefact_registry
        self.relation_registry = relation_registry

    def traverse(
        self, start_id: str, direction: TraversalClass, max_depth: int = 10
    ) -> LineageTraversal:
        start_node = self.artefact_registry.get_artefact(start_id)
        if not start_node:
            raise LineageTraversalError(f"Start artefact {start_id} not found")

        visited_nodes: Set[str] = set()
        visited_edges: List[RelationEdge] = []
        result_nodes: List[ArtefactRecord] = []

        queue = [(start_id, 0)]

        while queue:
            current_id, depth = queue.pop(0)

            if current_id in visited_nodes or depth > max_depth:
                continue

            visited_nodes.add(current_id)
            node = self.artefact_registry.get_artefact(current_id)
            if node:
                result_nodes.append(node)

                if direction == TraversalClass.BACKWARD:
                    # Look for relations where current_id is the source (it depends on target)
                    edges = self.relation_registry.get_relations_for_source(current_id)
                    for edge in edges:
                        visited_edges.append(edge)
                        queue.append((edge.target_id, depth + 1))
                else:  # FORWARD
                    # Look for relations where current_id is the target (it is depended on by source)
                    edges = self.relation_registry.get_relations_for_target(current_id)
                    for edge in edges:
                        visited_edges.append(edge)
                        queue.append((edge.source_id, depth + 1))

        completeness = (
            CompletenessClass.COMPLETE
            if len(visited_nodes) > 0
            else CompletenessClass.PARTIAL
        )

        return LineageTraversal(
            start_id=start_id,
            direction=direction,
            visited_artefacts=result_nodes,
            edges=visited_edges,
            completeness=completeness,
        )
