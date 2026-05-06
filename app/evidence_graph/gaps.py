from typing import List
import uuid

from app.evidence_graph.models import GraphGapFinding
from app.evidence_graph.enums import GraphGapSeverity
from app.evidence_graph.artefacts import ArtefactRegistry
from app.evidence_graph.relations import RelationRegistry


class GapDetector:
    def __init__(
        self, artefact_registry: ArtefactRegistry, relation_registry: RelationRegistry
    ):
        self.artefact_registry = artefact_registry
        self.relation_registry = relation_registry

    def find_gaps(self) -> List[GraphGapFinding]:
        gaps = []
        # Find dangling relations (target missing)
        for rel in self.relation_registry.get_all_relations():
            target = self.artefact_registry.get_artefact(rel.target_id)
            if not target:
                gaps.append(
                    GraphGapFinding(
                        gap_id=f"GAP-{uuid.uuid4().hex[:8]}",
                        severity=GraphGapSeverity.CRITICAL,
                        description=f"Dangling relation {rel.edge_id} to missing target {rel.target_id}",
                        affected_artefacts=[rel.source_id, rel.target_id],
                        suggested_action="Investigate missing artefact or remove relation",
                    )
                )
        return gaps
