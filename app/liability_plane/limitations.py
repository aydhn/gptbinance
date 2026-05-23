import uuid
from typing import List
from app.liability_plane.models import LimitationRecord, ProofNote
from app.liability_plane.enums import LimitationClass
from app.liability_plane.repository import LiabilityRepository

class LimitationManager:
    def __init__(self, repository: LiabilityRepository):
        self.repository = repository

    def add_limitation(self, liability_id: str, lim_class: LimitationClass, description: str, notes: List[ProofNote]) -> LimitationRecord:
        record = self.repository.get_liability_record(liability_id)
        if not record:
            raise ValueError(f"Liability {liability_id} not found.")

        lim_record = LimitationRecord(
            record_id=str(uuid.uuid4()),
            liability_id=liability_id,
            limitation_class=lim_class,
            description=description,
            proof_notes=notes
        )
        record.limitation.append(lim_record)
        self.repository.storage.save(record)
        return lim_record
