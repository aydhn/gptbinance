from typing import List
from app.qualification.models import (
    ScenarioResult,
    ContractCheckResult,
    ForbiddenActionCheck,
    QualificationFinding,
    QualificationScore,
    EvidencePack,
)
from app.qualification.enums import RequirementCriticality


def calculate_score(
    scenarios: List[ScenarioResult],
    contracts: List[ContractCheckResult],
    forbidden: List[ForbiddenActionCheck],
    findings: List[QualificationFinding],
    evidence_pack: EvidencePack,
) -> QualificationScore:

    score = QualificationScore()

    if scenarios:
        score.golden_path_pass_rate = sum(1 for s in scenarios if s.passed) / len(
            scenarios
        )
    else:
        score.golden_path_pass_rate = 1.0

    if forbidden:
        score.negative_test_pass_rate = sum(
            1 for f in forbidden if f.was_blocked
        ) / len(forbidden)
    else:
        score.negative_test_pass_rate = 1.0

    if contracts:
        score.contract_verification_score = sum(1 for c in contracts if c.passed) / len(
            contracts
        )
    else:
        score.contract_verification_score = 1.0

    score.evidence_completeness = 1.0 if evidence_pack.is_complete else 0.5

    score.critical_findings_count = sum(
        1
        for f in findings
        if f.criticality == RequirementCriticality.CRITICAL and not f.is_waived
    )
    score.waived_findings_count = sum(1 for f in findings if f.is_waived)

    # Simplified overall score formula
    score.overall_score = (
        score.golden_path_pass_rate * 0.3
        + score.negative_test_pass_rate * 0.3
        + score.contract_verification_score * 0.2
        + score.evidence_completeness * 0.2
    )

    if score.critical_findings_count > 0:
        score.overall_score = 0.0  # Force zero if critical findings remain

    return score
