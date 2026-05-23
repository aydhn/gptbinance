import uuid
from typing import List
from app.liability_plane.models import LiabilityReadinessBundle, ProofNote
from app.liability_plane.repository import LiabilityRepository

class ReadinessManager:
    def __init__(self, repository: LiabilityRepository):
        self.repository = repository

    def aggregate_readiness(self, liability_id: str, causation: bool, allocation: bool, indemnity: bool, exoneration: bool, exposure: bool, notes: List[ProofNote]) -> LiabilityReadinessBundle:
        return LiabilityReadinessBundle(
            bundle_id=str(uuid.uuid4()),
            liability_id=liability_id,
            causation_clarity=causation,
            allocation_rigor=allocation,
            indemnity_discipline=indemnity,
            exoneration_honesty=exoneration,
            exposure_visibility=exposure,
            proof_notes=notes
        )
