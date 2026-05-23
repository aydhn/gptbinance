import uuid
from typing import List
from app.liability_plane.models import SeveralLiabilityRecord, ProofNote
from app.liability_plane.enums import SeveralLiabilityClass
from app.liability_plane.repository import LiabilityRepository

class SeveralLiabilityManager:
    def __init__(self, repository: LiabilityRepository):
        self.repository = repository

    def add_several_liability(self, liability_id: str, several_class: SeveralLiabilityClass, actor: str, exposure: float, notes: List[ProofNote]) -> SeveralLiabilityRecord:
        record = self.repository.get_liability_record(liability_id)
        if not record:
            raise ValueError(f"Liability {liability_id} not found.")

        sev_record = SeveralLiabilityRecord(
            record_id=str(uuid.uuid4()),
            liability_id=liability_id,
            several_class=several_class,
            actor=actor,
            exposure_amount=exposure,
            proof_notes=notes
        )
        record.several.append(sev_record)
        self.repository.storage.save(record)
        return sev_record
