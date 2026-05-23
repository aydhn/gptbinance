import uuid
from typing import List
from app.liability_plane.models import ContributionRecord, ProofNote
from app.liability_plane.enums import ContributionClass
from app.liability_plane.repository import LiabilityRepository

class ContributionManager:
    def __init__(self, repository: LiabilityRepository):
        self.repository = repository

    def add_contribution(self, liability_id: str, cont_class: ContributionClass, actor: str, percentage: float, notes: List[ProofNote]) -> ContributionRecord:
        record = self.repository.get_liability_record(liability_id)
        if not record:
            raise ValueError(f"Liability {liability_id} not found.")

        cont_record = ContributionRecord(
            record_id=str(uuid.uuid4()),
            liability_id=liability_id,
            contribution_class=cont_class,
            actor=actor,
            percentage=percentage,
            proof_notes=notes
        )
        record.contribution.append(cont_record)
        self.repository.storage.save(record)
        return cont_record
