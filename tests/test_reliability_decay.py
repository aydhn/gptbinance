from app.reliability.decay import ReadinessDecayEngine
from app.reliability.enums import ReliabilityDomain, ReadinessDecayClass


def test_readiness_decay_contributors():
    # Stale evidence
    records = ReadinessDecayEngine.evaluate_stale_evidence(
        ReliabilityDomain.MARKET_TRUTH, 10.0, 5.0
    )
    assert len(records) == 1
    assert records[0].decay_class == ReadinessDecayClass.STALE_EVIDENCE
    assert records[0].severity_score > 0

    # Unresolved debt
    records_debt = ReadinessDecayEngine.evaluate_unresolved_debt(
        ReliabilityDomain.MARKET_TRUTH, 2, 10.0
    )
    assert len(records_debt) == 1
    assert records_debt[0].decay_class == ReadinessDecayClass.UNRESOLVED_DEBT
