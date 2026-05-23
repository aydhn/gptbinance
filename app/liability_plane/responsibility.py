import uuid
from typing import List
from app.liability_plane.models import ResponsibilityRecord, ProofNote
from app.liability_plane.enums import ResponsibilityClass
from app.liability_plane.repository import LiabilityRepository

class ResponsibilityManager:
    def __init__(self, repository: LiabilityRepository):
        self.repository = repository

    def add_responsibility(self, liability_id: str, resp_class: ResponsibilityClass, actor: str, description: str, notes: List[ProofNote]) -> ResponsibilityRecord:
        record = self.repository.get_liability_record(liability_id)
        if not record:
            raise ValueError(f"Liability {liability_id} not found.")

        resp_record = ResponsibilityRecord(
            record_id=str(uuid.uuid4()),
            liability_id=liability_id,
            responsibility_class=resp_class,
            actor=actor,
            description=description,
            proof_notes=notes
        )
        record.responsibility.append(resp_record)
        self.repository.storage.save(record)
        return resp_record
