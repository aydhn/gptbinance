from app.risk_plane.responses import ResponseIntentEngine
from app.risk_plane.models import RiskBreachRecord, RiskLimitRef, RiskStateRef
from app.risk_plane.enums import BreachClass, ResponseClass, LimitClass, RiskDomain


def test_response_intent_generation():
    engine = ResponseIntentEngine()
    breach = RiskBreachRecord(
        breach_id="b1",
        limit_ref=RiskLimitRef(
            limit_id="l1", limit_class=LimitClass.HARD, owner_domain="D"
        ),
        state_ref=RiskStateRef(state_id="s1", domain=RiskDomain.ACCOUNT, target_id="T"),
        breach_class=BreachClass.EMERGENCY,
        breached_value=2000.0,
        timestamp="2024-01-01T00:00:00Z",
        repeated_family=False,
        blast_radius="GLOBAL",
        proof_notes=[],
    )

    intents = engine.generate_intents([breach])
    assert len(intents) == 1
    assert intents[0].response_class == ResponseClass.EMERGENCY_DELEVERAGE_INTENT
