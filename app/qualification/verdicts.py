from app.qualification.models import QualificationScore, QualificationVerdict
from app.qualification.enums import (
    QualificationProfile,
    GoNoGoVerdict,
    CertificationVerdict,
)


def evaluate_verdict(
    profile: QualificationProfile, score: QualificationScore
) -> QualificationVerdict:
    verdict = QualificationVerdict(
        profile=profile,
        verdict=CertificationVerdict.BLOCKED,
        go_no_go=GoNoGoVerdict.BLOCKED,
    )

    if score.critical_findings_count > 0:
        verdict.blockers.append(
            f"Found {score.critical_findings_count} critical findings."
        )
        verdict.verdict = CertificationVerdict.BLOCKED
        verdict.go_no_go = GoNoGoVerdict.NO_GO
        return verdict

    if score.evidence_completeness < 1.0:
        verdict.blockers.append("Evidence pack is incomplete.")
        verdict.verdict = CertificationVerdict.FAIL
        verdict.go_no_go = GoNoGoVerdict.NO_GO
        return verdict

    if score.overall_score >= 0.95:
        verdict.verdict = CertificationVerdict.PASS
        if profile == QualificationProfile.FULL_LIVE:
            # Special case, normally blocked
            verdict.go_no_go = GoNoGoVerdict.BLOCKED
            verdict.warnings.append(
                "Full live default blocked. Needs explicit manual override if required."
            )
        elif profile == QualificationProfile.CANARY_LIVE_CAUTION_READY:
            verdict.go_no_go = GoNoGoVerdict.LIMITED_GO
        else:
            verdict.go_no_go = GoNoGoVerdict.GO

    elif score.overall_score >= 0.80:
        verdict.verdict = CertificationVerdict.CAUTION
        verdict.go_no_go = GoNoGoVerdict.CAUTION
        verdict.warnings.append("Score is marginal. Proceed with caution.")
    else:
        verdict.verdict = CertificationVerdict.FAIL
        verdict.go_no_go = GoNoGoVerdict.NO_GO
        verdict.blockers.append(f"Overall score {score.overall_score:.2f} is too low.")

    return verdict
