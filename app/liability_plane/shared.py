import uuid
from typing import List, Dict
from app.liability_plane.models import SharedLiabilityRecord, ProofNote
from app.liability_plane.enums import SharedLiabilityClass
from app.liability_plane.repository import LiabilityRepository

class SharedLiabilityManager:
    def __init__(self, repository: LiabilityRepository):
        self.repository = repository

    def add_shared_liability(self, liability_id: str, shared_class: SharedLiabilityClass, actors: List[str], allocations: Dict[str, float], notes: List[ProofNote]) -> SharedLiabilityRecord:
        record = self.repository.get_liability_record(liability_id)
        if not record:
            raise ValueError(f"Liability {liability_id} not found.")

        shared_record = SharedLiabilityRecord(
            record_id=str(uuid.uuid4()),
            liability_id=liability_id,
            shared_class=shared_class,
            actors=actors,
            allocations=allocations,
            proof_notes=notes
        )
        record.shared.append(shared_record)
        self.repository.storage.save(record)
        return shared_record
