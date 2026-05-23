import uuid
from typing import List
from app.liability_plane.models import IndemnityRecord, ProofNote
from app.liability_plane.enums import IndemnityClass
from app.liability_plane.repository import LiabilityRepository

class IndemnityManager:
    def __init__(self, repository: LiabilityRepository):
        self.repository = repository

    def add_indemnity(self, liability_id: str, ind_class: IndemnityClass, indemnifier: str, indemnitee: str, scope: str, notes: List[ProofNote]) -> IndemnityRecord:
        record = self.repository.get_liability_record(liability_id)
        if not record:
            raise ValueError(f"Liability {liability_id} not found.")

        ind_record = IndemnityRecord(
            record_id=str(uuid.uuid4()),
            liability_id=liability_id,
            indemnity_class=ind_class,
            indemnifier=indemnifier,
            indemnitee=indemnitee,
            scope_description=scope,
            proof_notes=notes
        )
        record.indemnity.append(ind_record)
        self.repository.storage.save(record)
        return ind_record
