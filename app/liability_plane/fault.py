import uuid
from typing import List
from app.liability_plane.models import FaultRecord, ProofNote
from app.liability_plane.enums import FaultClass
from app.liability_plane.repository import LiabilityRepository

class FaultManager:
    def __init__(self, repository: LiabilityRepository):
        self.repository = repository

    def add_fault(self, liability_id: str, fault_class: FaultClass, actor: str, notes: List[ProofNote]) -> FaultRecord:
        record = self.repository.get_liability_record(liability_id)
        if not record:
            raise ValueError(f"Liability {liability_id} not found.")

        fault_record = FaultRecord(
            record_id=str(uuid.uuid4()),
            liability_id=liability_id,
            fault_class=fault_class,
            actor=actor,
            proof_notes=notes
        )
        record.fault.append(fault_record)
        self.repository.storage.save(record)
        return fault_record
