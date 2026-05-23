import uuid
from typing import List
from app.liability_plane.models import RecourseAllocationRecord, ProofNote
from app.liability_plane.repository import LiabilityRepository

class RecourseManager:
    def __init__(self, repository: LiabilityRepository):
        self.repository = repository

    def add_recourse(self, liability_id: str, recourse_type: str, target: str, notes: List[ProofNote]) -> RecourseAllocationRecord:
        record = self.repository.get_liability_record(liability_id)
        if not record:
            raise ValueError(f"Liability {liability_id} not found.")

        rec_record = RecourseAllocationRecord(
            record_id=str(uuid.uuid4()),
            liability_id=liability_id,
            recourse_type=recourse_type,
            target_actor=target,
            proof_notes=notes
        )
        record.recourse.append(rec_record)
        self.repository.storage.save(record)
        return rec_record
