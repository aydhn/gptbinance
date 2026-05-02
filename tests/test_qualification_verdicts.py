from app.qualification.verdicts import evaluate_verdict
from app.qualification.models import QualificationScore
from app.qualification.enums import (
    QualificationProfile,
    CertificationVerdict,
    GoNoGoVerdict,
)


def test_evaluate_verdict_pass():
    score = QualificationScore(
        overall_score=1.0, evidence_completeness=1.0, critical_findings_count=0
    )
    verdict = evaluate_verdict(QualificationProfile.TESTNET_EXEC_READY, score)
    assert verdict.verdict == CertificationVerdict.PASS
    assert verdict.go_no_go == GoNoGoVerdict.GO


def test_evaluate_verdict_blocked():
    score = QualificationScore(
        overall_score=0.0, evidence_completeness=1.0, critical_findings_count=1
    )
    verdict = evaluate_verdict(QualificationProfile.TESTNET_EXEC_READY, score)
    assert verdict.verdict == CertificationVerdict.BLOCKED
    assert verdict.go_no_go == GoNoGoVerdict.NO_GO
