import uuid
from typing import List
from app.liability_plane.models import StrictLiabilityRecord, ProofNote
from app.liability_plane.enums import StrictLiabilityClass
from app.liability_plane.repository import LiabilityRepository

class StrictLiabilityManager:
    def __init__(self, repository: LiabilityRepository):
        self.repository = repository

    def add_strict_liability(self, liability_id: str, strict_class: StrictLiabilityClass, actor: str, caveats: str, notes: List[ProofNote]) -> StrictLiabilityRecord:
        record = self.repository.get_liability_record(liability_id)
        if not record:
            raise ValueError(f"Liability {liability_id} not found.")

        strict_record = StrictLiabilityRecord(
            record_id=str(uuid.uuid4()),
            liability_id=liability_id,
            strict_liability_class=strict_class,
            actor=actor,
            caveats=caveats,
            proof_notes=notes
        )
        record.strict_liability.append(strict_record)
        self.repository.storage.save(record)
        return strict_record
