import uuid
from typing import List
from app.liability_plane.models import ConsequenceAllocationRecord, ProofNote
from app.liability_plane.enums import ConsequenceClass
from app.liability_plane.repository import LiabilityRepository

class ConsequenceManager:
    def __init__(self, repository: LiabilityRepository):
        self.repository = repository

    def add_consequence(self, liability_id: str, cons_class: ConsequenceClass, bearer: str, description: str, notes: List[ProofNote]) -> ConsequenceAllocationRecord:
        record = self.repository.get_liability_record(liability_id)
        if not record:
            raise ValueError(f"Liability {liability_id} not found.")

        cons_record = ConsequenceAllocationRecord(
            record_id=str(uuid.uuid4()),
            liability_id=liability_id,
            consequence_class=cons_class,
            bearer=bearer,
            description=description,
            proof_notes=notes
        )
        record.consequences.append(cons_record)
        self.repository.storage.save(record)
        return cons_record
