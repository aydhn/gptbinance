import uuid
from typing import List
from app.liability_plane.models import LiabilityTrustVerdict
from app.liability_plane.enums import TrustVerdict
from app.liability_plane.repository import LiabilityRepository

class TrustManager:
    def __init__(self, repository: LiabilityRepository):
        self.repository = repository

    def compute_trust(self, liability_id: str, verdict: TrustVerdict, causation_score: float, allocation_score: float, exoneration_score: float, caveats: List[str], blockers: List[str]) -> LiabilityTrustVerdict:
        record = self.repository.get_liability_record(liability_id)
        if not record:
            raise ValueError(f"Liability {liability_id} not found.")

        trust_verdict = LiabilityTrustVerdict(
            verdict_id=str(uuid.uuid4()),
            liability_id=liability_id,
            verdict=verdict,
            causation_clarity_score=causation_score,
            allocation_rigor_score=allocation_score,
            exoneration_honesty_score=exoneration_score,
            caveats=caveats,
            blockers=blockers
        )
        record.trust_verdict = trust_verdict
        self.repository.storage.save(record)
        return trust_verdict
