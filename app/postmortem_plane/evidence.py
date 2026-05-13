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

    def bind_security_evidence(self, security_detections_refs: list, secret_lifecycle_refs: list, patch_rotation_history_refs: list, exposure_records_refs: list):
        self.security_detections_refs = security_detections_refs
        self.secret_lifecycle_refs = secret_lifecycle_refs
        self.patch_rotation_history_refs = patch_rotation_history_refs
        self.exposure_records_refs = exposure_records_refs
