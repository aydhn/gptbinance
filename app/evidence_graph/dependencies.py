from typing import List, Set

from app.evidence_graph.artefacts import ArtefactRegistry
from app.evidence_graph.relations import RelationRegistry
from app.evidence_graph.models import DependencyTraversal, ArtefactRecord
from app.evidence_graph.enums import RelationType
from app.evidence_graph.exceptions import DependencyTraversalError


class DependencyEngine:
    def __init__(
        self, artefact_registry: ArtefactRegistry, relation_registry: RelationRegistry
    ):
        self.artefact_registry = artefact_registry
        self.relation_registry = relation_registry

    def find_dependents(self, artefact_id: str) -> DependencyTraversal:
        start_node = self.artefact_registry.get_artefact(artefact_id)
        if not start_node:
            raise DependencyTraversalError(f"Artefact {artefact_id} not found")

        visited: Set[str] = set()
        dependents: List[ArtefactRecord] = []
        invalidated_by: List[ArtefactRecord] = []

        queue = [artefact_id]

        while queue:
            curr = queue.pop(0)
            if curr in visited:
                continue
            visited.add(curr)

            edges = self.relation_registry.get_relations_for_target(curr)
            for edge in edges:
                target_node = self.artefact_registry.get_artefact(edge.source_id)
                if not target_node:
                    continue

                if edge.relation_type == RelationType.INVALIDATED_BY:
                    invalidated_by.append(target_node)
                elif edge.relation_type in [
                    RelationType.DEPENDS_ON,
                    RelationType.DERIVED_FROM,
                    RelationType.SUPPORTS,
                ]:
                    # If target DEPENDS_ON curr (meaning target is the source of the edge, but we are looking forward)
                    # Actually if target depends on source, source is target of DEPENDS_ON.
                    pass

                # Simplification: treat all forward edges as dependents for this analysis
                if target_node not in dependents and curr != artefact_id:
                    dependents.append(target_node)
                elif curr == artefact_id and target_node not in dependents:
                    dependents.append(target_node)

                queue.append(edge.target_id)

        return DependencyTraversal(
            start_id=artefact_id,
            dependents=dependents,
            invalidated_by=invalidated_by,
            fanout_count=len(dependents),
        )
