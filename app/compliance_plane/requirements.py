from app.compliance_plane.models import ComplianceRequirement
from app.compliance_plane.enums import RequirementClass
from typing import Dict, Any, List


def create_requirement(
    req_id: str,
    req_class: RequirementClass,
    scope: Dict[str, Any],
    owner_id: str,
    satisfaction_criteria: str,
    review_cadence_days: int,
    failure_severity: str,
    lineage_refs: List[str],
    is_mandatory: bool = True,
) -> ComplianceRequirement:
    return ComplianceRequirement(
        requirement_id=req_id,
        requirement_class=req_class,
        scope=scope,
        owner_id=owner_id,
        satisfaction_criteria=satisfaction_criteria,
        review_cadence_days=review_cadence_days,
        failure_severity=failure_severity,
        lineage_refs=lineage_refs,
        is_mandatory=is_mandatory,
    )

def update_security_mappings(req: ComplianceRequirement, security_plane_refs: list):
     req.lineage_refs.extend(security_plane_refs)

class ComplianceRequirement:
    def enforce_rationale_preservation(self):
        pass