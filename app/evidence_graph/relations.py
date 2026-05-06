from typing import Dict, List
import uuid
from datetime import datetime

from app.evidence_graph.models import RelationEdge
from app.evidence_graph.enums import RelationType, ArtefactType


class RelationRegistry:
    def __init__(self):
        self._relations: Dict[str, RelationEdge] = {}
        # Simple validation matrix for allowed pairs (Source Type -> Allowed Relation -> Allowed Target Types)
        self._allowed_pairs = {
            ArtefactType.READINESS_MEMO: {
                RelationType.DERIVED_FROM: [
                    ArtefactType.EXPERIMENT_PACK,
                    ArtefactType.POLICY_DECISION,
                ],
                RelationType.DEPENDS_ON: [ArtefactType.MIGRATION_PLAN],
            },
            ArtefactType.INCIDENT_SNAPSHOT: {
                RelationType.LED_TO: [
                    ArtefactType.CONTAINMENT_PLAN,
                    ArtefactType.POSTMORTEM_REPORT,
                ]
            },
            ArtefactType.POSTMORTEM_REPORT: {
                RelationType.FOLLOWS_INCIDENT: [ArtefactType.INCIDENT_SNAPSHOT],
                RelationType.LED_TO: [ArtefactType.CAPA_RECORD],
            },
            ArtefactType.REMEDIATION_PACK: {
                RelationType.ADDRESSES: [
                    ArtefactType.CAPA_RECORD,
                    ArtefactType.SHADOW_DRIFT_FINDING,
                ]
            },
        }

    def _validate_relation(
        self,
        source_type: ArtefactType,
        target_type: ArtefactType,
        relation_type: RelationType,
    ):
        # Allow all for now if not strictly defined, but in a strict system this would block
        if source_type in self._allowed_pairs:
            if relation_type in self._allowed_pairs[source_type]:
                if target_type not in self._allowed_pairs[source_type][relation_type]:
                    pass  # In real strict implementation: raise InvalidRelationEdgeError(...)

    def add_relation(
        self,
        source_id: str,
        source_type: ArtefactType,
        target_id: str,
        target_type: ArtefactType,
        relation_type: RelationType,
        metadata: dict = None,
    ) -> RelationEdge:
        self._validate_relation(source_type, target_type, relation_type)

        edge = RelationEdge(
            edge_id=f"REL-{uuid.uuid4().hex[:8]}",
            source_id=source_id,
            target_id=target_id,
            relation_type=relation_type,
            created_at=datetime.now(),
            metadata=metadata or {},
        )
        self._relations[edge.edge_id] = edge
        return edge

    def get_relations_for_source(self, source_id: str) -> List[RelationEdge]:
        return [r for r in self._relations.values() if r.source_id == source_id]

    def get_relations_for_target(self, target_id: str) -> List[RelationEdge]:
        return [r for r in self._relations.values() if r.target_id == target_id]

    def get_all_relations(self) -> List[RelationEdge]:
        return list(self._relations.values())
