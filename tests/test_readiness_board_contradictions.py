from app.readiness_board.contradictions import ContradictionDetector
from app.readiness_board.models import ReadinessDomainVerdict
from app.readiness_board.enums import ReadinessDomain, DomainVerdict, ContradictionClass


def test_detect_contradictions():
    detector = ContradictionDetector()
    verdicts = {
        ReadinessDomain.POLICY: ReadinessDomainVerdict(
            domain=ReadinessDomain.POLICY, verdict=DomainVerdict.BLOCK
        ),
        ReadinessDomain.QUALIFICATION: ReadinessDomainVerdict(
            domain=ReadinessDomain.QUALIFICATION, verdict=DomainVerdict.PASS
        ),
    }
    conflicts = detector.detect(verdicts)
    assert len(conflicts) == 1
    assert conflicts[0].contradiction_class == ContradictionClass.EXPERIMENT_VS_POLICY
