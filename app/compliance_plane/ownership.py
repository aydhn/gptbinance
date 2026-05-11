from typing import Dict, List
from app.compliance_plane.models import ComplianceRequirement, ControlObjective


class OwnershipManager:
    def check_orphan_controls(
        self, controls: List[ControlObjective], valid_users: List[str]
    ) -> List[str]:
        return [c.control_id for c in controls if c.owner_id not in valid_users]

    def check_orphan_requirements(
        self, reqs: List[ComplianceRequirement], valid_users: List[str]
    ) -> List[str]:
        return [r.requirement_id for r in reqs if r.owner_id not in valid_users]
