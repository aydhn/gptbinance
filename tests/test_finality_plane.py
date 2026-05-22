import pytest
from app.finality_plane.registry import FinalityRegistry
from app.finality_plane.enums import FinalityClass, FinalityTrustVerdictClass
from app.finality_plane.trust import FinalityTrustEngine

def test_finality_registry():
    obj = FinalityRegistry.register_finality(
        owner="sec-ops",
        scope="incident-123",
        finality_class=FinalityClass.PROVISIONAL,
        closure_posture="observation_pending",
        reopen_posture="actor_scoped"
    )
    assert obj.finality_id.startswith("fin-")
    assert obj.owner == "sec-ops"

def test_trust_engine_blocked():
    verdict = FinalityTrustEngine.evaluate_trust(
        finality_id="fin-123",
        closure_basis_strength="strong",
        reopen_clarity="clear",
        settlement_rigor="rigorous",
        residual_duty_visibility="high",
        caveats=[],
        blockers=["open_dispute_found"]
    )
    assert verdict.verdict == FinalityTrustVerdictClass.BLOCKED

def test_trust_engine_caution():
    verdict = FinalityTrustEngine.evaluate_trust(
        finality_id="fin-456",
        closure_basis_strength="premature",
        reopen_clarity="unclear",
        settlement_rigor="weak",
        residual_duty_visibility="low",
        caveats=["might_reopen"],
        blockers=[]
    )
    assert verdict.verdict == FinalityTrustVerdictClass.CAUTION
