from app.compliance_plane.models import (
    ControlMapping,
    ComplianceRequirementRef,
    ControlObjectiveRef,
)
from app.compliance_plane.enums import EvidenceClass
from typing import List, Optional
from app.compliance_plane.exceptions import InvalidControlMapping


class MappingRegistry:
    def __init__(self):
        self._mappings: List[ControlMapping] = []

    def register_mapping(self, mapping: ControlMapping) -> None:
        if not mapping.requirement_refs or not mapping.control_ref:
            raise InvalidControlMapping("Mapping must have requirements and a control.")
        self._mappings.append(mapping)

    def get_mappings_for_requirement(self, req_id: str) -> List[ControlMapping]:
        return [
            m
            for m in self._mappings
            if any(r.requirement_id == req_id for r in m.requirement_refs)
        ]

    def get_mappings_for_control(self, control_id: str) -> List[ControlMapping]:
        return [m for m in self._mappings if m.control_ref.control_id == control_id]

    def list_mappings(self) -> List[ControlMapping]:
        return self._mappings
