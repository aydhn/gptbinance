from app.evidence_graph.models import QueryRequest, QueryResult
from app.evidence_graph.enums import CompletenessClass
from app.evidence_graph.artefacts import ArtefactRegistry
from app.evidence_graph.relations import RelationRegistry


class GraphQueryEngine:
    def __init__(
        self, artefact_registry: ArtefactRegistry, relation_registry: RelationRegistry
    ):
        self.artefact_registry = artefact_registry
        self.relation_registry = relation_registry

    def execute_query(self, request: QueryRequest) -> QueryResult:
        # Simple exact match filtering based on scope
        results = []
        for artefact in self.artefact_registry.list_artefacts():
            if (
                request.target_scope.symbol
                and artefact.scope.symbol != request.target_scope.symbol
            ):
                continue
            if (
                request.target_scope.profile
                and artefact.scope.profile != request.target_scope.profile
            ):
                continue
            results.append(artefact)

        # Collect relevant edges
        edges = []
        for r in results:
            edges.extend(self.relation_registry.get_relations_for_source(r.id))
            edges.extend(self.relation_registry.get_relations_for_target(r.id))

        # Deduplicate edges
        edges = list({e.edge_id: e for e in edges}.values())

        return QueryResult(
            artefacts=results,
            relations=edges,
            completeness=CompletenessClass.COMPLETE,
            redaction_notes=[],
        )
