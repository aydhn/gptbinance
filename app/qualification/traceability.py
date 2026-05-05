from app.data_governance.models import DataContract, TrustVerdict
from typing import Dict, List
from app.qualification.models import TraceabilityEntry
from app.qualification.requirements import get_all_requirements

# In a real system, this would be dynamically built or loaded from a config.
# For now, it's a static mapping.
_MAPPINGS: Dict[str, TraceabilityEntry] = {
    "REQ-001": TraceabilityEntry(
        req_id="REQ-001",
        scenario_ids=["neg-unauthorized-live"],
        evidence_refs=["ops-gate-logs"],
        is_covered=True,
    ),
    "REQ-002": TraceabilityEntry(
        req_id="REQ-002",
        scenario_ids=["gold-risk-to-exec", "neg-risk-bypass"],
        evidence_refs=["risk-approved-intent"],
        is_covered=True,
    ),
    "REQ-003": TraceabilityEntry(
        req_id="REQ-003",
        scenario_ids=["neg-stale-approval"],
        evidence_refs=["control-audit"],
        is_covered=True,
    ),
    "REQ-004": TraceabilityEntry(
        req_id="REQ-004",
        scenario_ids=["gold-restore-dry-run"],
        evidence_refs=["security-audit"],
        is_covered=True,
    ),
    "REQ-005": TraceabilityEntry(
        req_id="REQ-005",
        scenario_ids=["gold-upgrade-dry-run", "neg-upgrade-no-backup"],
        evidence_refs=["backup-metadata"],
        is_covered=True,
    ),
    "REQ-006": TraceabilityEntry(
        req_id="REQ-006",
        scenario_ids=["contract-evidence-chain"],
        evidence_refs=["integrity-report"],
        is_covered=True,
    ),
    "REQ-007": TraceabilityEntry(
        req_id="REQ-007",
        scenario_ids=["neg-mainnet-chaos"],
        evidence_refs=["resilience-summary"],
        is_covered=True,
    ),
    "REQ-008": TraceabilityEntry(
        req_id="REQ-008",
        scenario_ids=["neg-missing-secret-live"],
        evidence_refs=["security-posture"],
        is_covered=True,
    ),
    "REQ-009": TraceabilityEntry(
        req_id="REQ-009",
        scenario_ids=["gold-portfolio-concentration"],
        evidence_refs=["portfolio-report"],
        is_covered=True,
    ),
}


def build_traceability_matrix() -> List[TraceabilityEntry]:
    matrix = []
    for req in get_all_requirements():
        if req.req_id in _MAPPINGS:
            matrix.append(_MAPPINGS[req.req_id])
        else:
            matrix.append(TraceabilityEntry(req_id=req.req_id, is_covered=False))
    return matrix


def get_uncovered_requirements() -> List[str]:
    matrix = build_traceability_matrix()
    return [entry.req_id for entry in matrix if not entry.is_covered]
