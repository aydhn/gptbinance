import uuid
from typing import List
from app.liability_plane.models import CostBearerRecord, ProofNote
from app.liability_plane.enums import CostBearerClass
from app.liability_plane.repository import LiabilityRepository

class CostBearerManager:
    def __init__(self, repository: LiabilityRepository):
        self.repository = repository

    def add_cost_bearer(self, liability_id: str, bearer_class: CostBearerClass, actor: str, notes: List[ProofNote]) -> CostBearerRecord:
        record = self.repository.get_liability_record(liability_id)
        if not record:
            raise ValueError(f"Liability {liability_id} not found.")

        cb_record = CostBearerRecord(
            record_id=str(uuid.uuid4()),
            liability_id=liability_id,
            bearer_class=bearer_class,
            actor=actor,
            proof_notes=notes
        )
        record.cost_bearers.append(cb_record)
        self.repository.storage.save(record)
        return cb_record
