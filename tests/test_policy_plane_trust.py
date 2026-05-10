import pytest
from app.policy_plane.trust import evaluate_system_trust
from app.policy_plane.enums import TrustVerdict


def test_evaluate_system_trust():
    trust = evaluate_system_trust()
    assert trust is not None
    assert trust.verdict == TrustVerdict.TRUSTED
    assert trust.factors["coverage"] == "complete"
