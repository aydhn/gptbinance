import pytest
from app.settlement_plane.trust import SettlementTrustEngine
from app.settlement_plane.models import SettlementRecord
from app.settlement_plane.enums import SettlementClass, TrustVerdict

def test_settlement_trust_engine():
    engine = SettlementTrustEngine()

    # Missing release refs
    record1 = SettlementRecord(
        id="S1",
        settlement_class=SettlementClass.DISPUTE_RESOLUTION,
        owner="test",
        scope_refs=["s1"],
        release_refs=[],
        performance_refs=[]
    )
    verdict1 = engine.evaluate(record1)
    assert verdict1.verdict == TrustVerdict.REVIEW_REQUIRED

    # Valid
    record2 = SettlementRecord(
        id="S2",
        settlement_class=SettlementClass.DISPUTE_RESOLUTION,
        owner="test",
        scope_refs=["s1"],
        release_refs=["r1"],
        performance_refs=[]
    )
    verdict2 = engine.evaluate(record2)
    assert verdict2.verdict == TrustVerdict.TRUSTED
