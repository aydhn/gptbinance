# admission.py
from typing import Dict, List, Optional
from app.insolvency_plane.models import ClaimAdmissionRecord
from app.insolvency_plane.exceptions import InvalidClaimAdmissionError

class ClaimAdmissionManager:
    def __init__(self):
        self.admissions: Dict[str, ClaimAdmissionRecord] = {}

    def admit_claim(self, admission: ClaimAdmissionRecord):
        self.admissions[admission.admission_id] = admission

    def get_admission(self, admission_id: str) -> Optional[ClaimAdmissionRecord]:
        return self.admissions.get(admission_id)

    def get_admission_for_claim(self, claim_id: str) -> Optional[ClaimAdmissionRecord]:
        for admission in self.admissions.values():
            if admission.claim_id == claim_id:
                return admission
        return None

    def list_admissions(self) -> List[ClaimAdmissionRecord]:
        return list(self.admissions.values())
