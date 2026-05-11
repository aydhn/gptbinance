from app.compliance_plane.models import EvidenceRequirement, ControlObjectiveRef
from app.compliance_plane.enums import EvidenceClass
from typing import List, Dict


class EvidenceRegistry:
    def __init__(self):
        self._requirements: Dict[str, EvidenceRequirement] = {}

    def register_evidence_requirement(self, req: EvidenceRequirement) -> None:
        self._requirements[req.evidence_req_id] = req

    def get_evidence_requirements_for_control(
        self, control_id: str
    ) -> List[EvidenceRequirement]:
        return [
            r
            for r in self._requirements.values()
            if r.control_ref.control_id == control_id
        ]
