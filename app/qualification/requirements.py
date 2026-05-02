from typing import Dict, List
from app.qualification.enums import QualificationScope, RequirementCriticality
from app.qualification.models import RequirementRef

REQUIREMENT_REGISTRY: Dict[str, RequirementRef] = {
    "REQ-001": RequirementRef(
        req_id="REQ-001",
        description="Mainnet live execution is locked by default.",
        criticality=RequirementCriticality.CRITICAL,
        scope=QualificationScope.EXECUTION,
    ),
    "REQ-002": RequirementRef(
        req_id="REQ-002",
        description="Intent must be risk-approved before execution.",
        criticality=RequirementCriticality.CRITICAL,
        scope=QualificationScope.RISK,
    ),
    "REQ-003": RequirementRef(
        req_id="REQ-003",
        description="Stale control approvals cannot authorize an action.",
        criticality=RequirementCriticality.CRITICAL,
        scope=QualificationScope.CONTROL,
    ),
    "REQ-004": RequirementRef(
        req_id="REQ-004",
        description="Restore apply requires explicit authorization.",
        criticality=RequirementCriticality.CRITICAL,
        scope=QualificationScope.SECURITY,
    ),
    "REQ-005": RequirementRef(
        req_id="REQ-005",
        description="Backup freshness is required before release upgrade.",
        criticality=RequirementCriticality.HIGH,
        scope=QualificationScope.RELEASE,
    ),
    "REQ-006": RequirementRef(
        req_id="REQ-006",
        description="Evidence chain verification must be available.",
        criticality=RequirementCriticality.HIGH,
        scope=QualificationScope.SECURITY,
    ),
    "REQ-007": RequirementRef(
        req_id="REQ-007",
        description="Resilience experiments cannot run on mainnet by default.",
        criticality=RequirementCriticality.CRITICAL,
        scope=QualificationScope.RESILIENCE,
    ),
    "REQ-008": RequirementRef(
        req_id="REQ-008",
        description="Missing critical secrets block live readiness.",
        criticality=RequirementCriticality.CRITICAL,
        scope=QualificationScope.SYSTEM_WIDE,
    ),
    "REQ-009": RequirementRef(
        req_id="REQ-009",
        description="Portfolio concentration controls must be visible.",
        criticality=RequirementCriticality.HIGH,
        scope=QualificationScope.PORTFOLIO,
    ),
}


def get_requirement(req_id: str) -> RequirementRef:
    return REQUIREMENT_REGISTRY.get(req_id)


def get_all_requirements() -> List[RequirementRef]:
    return list(REQUIREMENT_REGISTRY.values())
