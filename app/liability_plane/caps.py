import uuid
from typing import List
from app.liability_plane.models import LiabilityCapRecord, ProofNote
from app.liability_plane.enums import LiabilityCapClass
from app.liability_plane.repository import LiabilityRepository

class CapManager:
    def __init__(self, repository: LiabilityRepository):
        self.repository = repository

    def add_cap(self, liability_id: str, cap_class: LiabilityCapClass, amount: float, currency: str, notes: List[ProofNote]) -> LiabilityCapRecord:
        record = self.repository.get_liability_record(liability_id)
        if not record:
            raise ValueError(f"Liability {liability_id} not found.")

        cap_record = LiabilityCapRecord(
            record_id=str(uuid.uuid4()),
            liability_id=liability_id,
            cap_class=cap_class,
            amount=amount,
            currency=currency,
            proof_notes=notes
        )
        record.caps.append(cap_record)
        self.repository.storage.save(record)
        return cap_record
