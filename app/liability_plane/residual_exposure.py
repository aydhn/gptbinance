import uuid
from typing import List
from app.liability_plane.models import ResidualExposureRecord, ProofNote
from app.liability_plane.enums import ResidualExposureClass
from app.liability_plane.repository import LiabilityRepository

class ResidualExposureManager:
    def __init__(self, repository: LiabilityRepository):
        self.repository = repository

    def add_residual_exposure(self, liability_id: str, exp_class: ResidualExposureClass, actor: str, description: str, notes: List[ProofNote]) -> ResidualExposureRecord:
        record = self.repository.get_liability_record(liability_id)
        if not record:
            raise ValueError(f"Liability {liability_id} not found.")

        exp_record = ResidualExposureRecord(
            record_id=str(uuid.uuid4()),
            liability_id=liability_id,
            exposure_class=exp_class,
            actor=actor,
            description=description,
            proof_notes=notes
        )
        record.residual_exposure.append(exp_record)
        self.repository.storage.save(record)
        return exp_record


def check_harmed_party_rights(harmed_party_id: str, rights_registry) -> str:
    """Checks if a harmed party has open claims in the rights plane."""
    active_claims = rights_registry.get_active_claims_for_beneficiary(harmed_party_id)
    if active_claims:
        return "explicit caution: liability capped but beneficiary rights still open"
    return "trusted"
