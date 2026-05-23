import uuid
from typing import List
from app.liability_plane.models import CausationRecord, ProofNote
from app.liability_plane.enums import CausationClass
from app.liability_plane.repository import LiabilityRepository

class CausationManager:
    def __init__(self, repository: LiabilityRepository):
        self.repository = repository

    def add_causation(self, liability_id: str, caus_class: CausationClass, actor: str, description: str, notes: List[ProofNote]) -> CausationRecord:
        record = self.repository.get_liability_record(liability_id)
        if not record:
            raise ValueError(f"Liability {liability_id} not found.")

        caus_record = CausationRecord(
            record_id=str(uuid.uuid4()),
            liability_id=liability_id,
            causation_class=caus_class,
            actor=actor,
            description=description,
            proof_notes=notes
        )
        record.causation.append(caus_record)
        self.repository.storage.save(record)
        return caus_record
