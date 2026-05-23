import uuid
from typing import List
from app.liability_plane.models import DutyToMitigateRecord, ProofNote
from app.liability_plane.enums import DutyToMitigateClass
from app.liability_plane.repository import LiabilityRepository

class MitigationDutyManager:
    def __init__(self, repository: LiabilityRepository):
        self.repository = repository

    def add_mitigation_duty(self, liability_id: str, duty_class: DutyToMitigateClass, actor: str, status: str, notes: List[ProofNote]) -> DutyToMitigateRecord:
        record = self.repository.get_liability_record(liability_id)
        if not record:
            raise ValueError(f"Liability {liability_id} not found.")

        duty_record = DutyToMitigateRecord(
            record_id=str(uuid.uuid4()),
            liability_id=liability_id,
            duty_class=duty_class,
            actor=actor,
            status=status,
            proof_notes=notes
        )
        record.mitigation_duties.append(duty_record)
        self.repository.storage.save(record)
        return duty_record
