import pytest
from app.ledger_plane.trust import TrustVerdictEngine
from app.ledger_plane.enums import TrustVerdict

def test_trust_verdict_creation():
    verdict = TrustVerdictEngine.evaluate(
        verdict=TrustVerdict.CAUTION,
        reasons=["Missing latest funding post"]
    )
    assert verdict.verdict == TrustVerdict.CAUTION
    assert len(verdict.reasons) == 1
    assert "Missing" in verdict.reasons[0]
