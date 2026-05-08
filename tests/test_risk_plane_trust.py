from app.risk_plane.trust import TrustedRiskVerdictEngine
from app.risk_plane.models import (
    RiskState,
    RiskBreachRecord,
    RiskLimitRef,
    RiskStateRef,
)
from app.risk_plane.enums import TrustVerdict, RiskDomain, BreachClass, LimitClass


def test_trust_evaluation():
    engine = TrustedRiskVerdictEngine()
    state = RiskState(
        state_id="s1",
        domain=RiskDomain.ACCOUNT,
        target_id="T",
        timestamp="2024-01-01T00:00:00Z",
        authoritative=False,
        source_position_refs=[],
        source_ledger_refs=[],
        source_market_truth_refs=[],
        completeness_summary="",
    )

    # Non authoritative -> DEGRADED
    verdict1 = engine.evaluate([state], [])
    assert verdict1.verdict == TrustVerdict.DEGRADED

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

    # Emergency breach -> BLOCKED
    verdict2 = engine.evaluate([state], [breach])
    assert verdict2.verdict == TrustVerdict.BLOCKED
