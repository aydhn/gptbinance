from datetime import datetime
import uuid

from app.evidence_graph.models import EvidencePack
from app.evidence_graph.enums import CompletenessClass
from app.evidence_graph.lineage import LineageEngine


class EvidencePackBuilder:
    def __init__(self, lineage_engine: LineageEngine):
        self.lineage_engine = lineage_engine

    def build_pack(self, pack_type: str, anchor_id: str) -> EvidencePack:
        # Traverse both directions or specify scope
        backward = self.lineage_engine.traverse(anchor_id, direction="BACKWARD")

        # Deduplicate
        artefacts = list({a.id: a for a in backward.visited_artefacts}.values())
        edges = backward.edges

        return EvidencePack(
            pack_id=f"PACK-{uuid.uuid4().hex[:8]}",
            pack_type=pack_type,
            created_at=datetime.now(),
            artefacts=artefacts,
            relations=edges,
            completeness=CompletenessClass.COMPLETE
            if artefacts
            else CompletenessClass.MISSING_CRITICAL,
        )
