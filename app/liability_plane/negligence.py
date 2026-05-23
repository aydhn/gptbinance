import uuid
from typing import List
from app.liability_plane.models import NegligenceRecord, ProofNote
from app.liability_plane.enums import NegligenceClass
from app.liability_plane.repository import LiabilityRepository

class NegligenceManager:
    def __init__(self, repository: LiabilityRepository):
        self.repository = repository

    def add_negligence(self, liability_id: str, neg_class: NegligenceClass, actor: str, notes: List[ProofNote]) -> NegligenceRecord:
        record = self.repository.get_liability_record(liability_id)
        if not record:
            raise ValueError(f"Liability {liability_id} not found.")

        neg_record = NegligenceRecord(
            record_id=str(uuid.uuid4()),
            liability_id=liability_id,
            negligence_class=neg_class,
            actor=actor,
            proof_notes=notes
        )
        record.negligence.append(neg_record)
        self.repository.storage.save(record)
        return neg_record
