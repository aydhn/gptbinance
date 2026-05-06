from app.reviews.models import ReviewEvidencePackRef
from typing import List


class EvidenceEngine:
    def assemble_pack(self, refs: List[str]) -> List[ReviewEvidencePackRef]:
        return [ReviewEvidencePackRef(evidence_id=ref) for ref in refs]

    def verify_pack(self, pack: List[ReviewEvidencePackRef]) -> bool:
        return len(pack) > 0
