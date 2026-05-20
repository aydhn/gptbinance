import pytest
from app.provenance_plane.trust import trust_evaluator
from app.provenance_plane.registry import registry
from app.provenance_plane.enums import TrustVerdictEnum

def test_trust_verdict_trusted():
    registry.register("trust-1", {"provenance_id": "trust-1", "custody_gap": False, "attribution": {"primary": "x"}})
    assert trust_evaluator.evaluate_trust("trust-1") == TrustVerdictEnum.TRUSTED

def test_trust_verdict_caution():
    registry.register("trust-2", {"provenance_id": "trust-2", "custody_gap": True, "attribution": {"primary": "y"}})
    assert trust_evaluator.evaluate_trust("trust-2") == TrustVerdictEnum.CAUTION

def test_trust_verdict_blocked():
    assert trust_evaluator.evaluate_trust("unknown-id") == TrustVerdictEnum.BLOCKED
