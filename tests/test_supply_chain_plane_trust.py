import pytest
from app.supply_chain_plane.models import ComponentRef
from app.supply_chain_plane.enums import TrustVerdict
from app.supply_chain_plane.trust import TrustVerdictEngine


def test_trust_verdict_engine():
    engine = TrustVerdictEngine()
    ref = ComponentRef(component_id="comp-1")
    verdict = engine.evaluate_trust(ref)

    assert verdict.verdict == TrustVerdict.TRUSTED
    assert "origin_clarity" in verdict.breakdown
