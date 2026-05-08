from app.risk_plane.breaches import CanonicalBreachClassifier
from app.risk_plane.models import RiskState, RiskLimitDefinition
from app.risk_plane.enums import LimitClass, RiskDomain, BreachClass


def test_breach_classification():
    classifier = CanonicalBreachClassifier()
    limit = RiskLimitDefinition(
        limit_id="l1",
        limit_class=LimitClass.HARD,
        owner_domain="D",
        domain=RiskDomain.ACCOUNT,
        target_id="T",
        value=1000.0,
        description="D",
    )
    state = RiskState(
        state_id="s1",
        domain=RiskDomain.ACCOUNT,
        target_id="T",
        timestamp="2024-01-01T00:00:00Z",
        authoritative=True,
        source_position_refs=[],
        source_ledger_refs=[],
        source_market_truth_refs=[],
        completeness_summary="",
    )

    # No breach
    assert classifier.classify(state, limit, 900.0) is None

    # Breach
    breach = classifier.classify(state, limit, 1100.0)
    assert breach is not None
    assert breach.breach_class == BreachClass.HARD
    assert breach.breached_value == 1100.0
