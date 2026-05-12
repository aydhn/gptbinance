from typing import List
from app.postmortem_plane.models import EvidenceReviewRecord
from app.postmortem_plane.exceptions import PostmortemPlaneError

class EvidenceBuilder:
    @staticmethod
    def build_review(evidence_id: str, e_type: str, freshness: str, notes: str, contradictions: List[str] = None) -> EvidenceReviewRecord:
        if not notes:
             raise PostmortemPlaneError("Sufficiency notes are required for evidence")
        return EvidenceReviewRecord(
            evidence_id=evidence_id,
            evidence_type=e_type,
            freshness=freshness,
            sufficiency_notes=notes,
            contradictory_evidence_refs=contradictions or [],
            telemetry_refs=[]
        )

class PostmortemEvidenceMigrationRef:
    def causal_chain_evidence(self):
        pass
