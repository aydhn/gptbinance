import uuid
from typing import List
from app.liability_plane.models import ExonerationRecord, ProofNote
from app.liability_plane.enums import ExonerationClass
from app.liability_plane.repository import LiabilityRepository

class ExonerationManager:
    def __init__(self, repository: LiabilityRepository):
        self.repository = repository

    def add_exoneration(self, liability_id: str, ex_class: ExonerationClass, actor: str, basis: str, notes: List[ProofNote]) -> ExonerationRecord:
        record = self.repository.get_liability_record(liability_id)
        if not record:
            raise ValueError(f"Liability {liability_id} not found.")

        ex_record = ExonerationRecord(
            record_id=str(uuid.uuid4()),
            liability_id=liability_id,
            exoneration_class=ex_class,
            actor=actor,
            basis=basis,
            proof_notes=notes
        )
        record.exoneration.append(ex_record)
        self.repository.storage.save(record)
        return ex_record

def settlement_driven_release():
    pass # Added for Phase 124