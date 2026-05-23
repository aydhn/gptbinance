import uuid
from typing import List
from app.liability_plane.models import CulpabilityRecord, ProofNote
from app.liability_plane.enums import CulpabilityClass
from app.liability_plane.repository import LiabilityRepository

class CulpabilityManager:
    def __init__(self, repository: LiabilityRepository):
        self.repository = repository

    def add_culpability(self, liability_id: str, culp_class: CulpabilityClass, actor: str, notes: List[ProofNote]) -> CulpabilityRecord:
        record = self.repository.get_liability_record(liability_id)
        if not record:
            raise ValueError(f"Liability {liability_id} not found.")

        culp_record = CulpabilityRecord(
            record_id=str(uuid.uuid4()),
            liability_id=liability_id,
            culpability_class=culp_class,
            actor=actor,
            proof_notes=notes
        )
        record.culpability.append(culp_record)
        self.repository.storage.save(record)
        return culp_record
