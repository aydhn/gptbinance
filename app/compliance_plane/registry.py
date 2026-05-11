from typing import Dict, List, Optional
from app.compliance_plane.models import ComplianceRequirement, ControlObjective
from app.compliance_plane.base import RequirementRegistryBase
from app.compliance_plane.exceptions import InvalidRequirementDefinition


class CanonicalComplianceRegistry(RequirementRegistryBase):
    def __init__(self):
        self._requirements: Dict[str, ComplianceRequirement] = {}
        self._controls: Dict[str, ControlObjective] = {}

    def register_requirement(self, requirement: ComplianceRequirement) -> None:
        if not requirement.requirement_id:
            raise InvalidRequirementDefinition("Requirement ID cannot be empty.")
        self._requirements[requirement.requirement_id] = requirement

    def get_requirement(self, req_id: str) -> Optional[ComplianceRequirement]:
        return self._requirements.get(req_id)

    def list_requirements(self) -> List[ComplianceRequirement]:
        return list(self._requirements.values())

    def register_control(self, control: ControlObjective) -> None:
        if not control.control_id:
            raise InvalidRequirementDefinition("Control ID cannot be empty.")
        self._controls[control.control_id] = control

    def get_control(self, control_id: str) -> Optional[ControlObjective]:
        return self._controls.get(control_id)

    def list_controls(self) -> List[ControlObjective]:
        return list(self._controls.values())
