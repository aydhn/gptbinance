import pytest
from app.enforcement_plane.models import EnforcementObject, TriggerRecord, ScopeBoundRecord
from app.enforcement_plane.enums import EnforcementClass, ReversibilityClass, AppealClass, DueProcessClass
from app.enforcement_plane.registry import CanonicalEnforcementRegistry
from app.enforcement_plane.trust import TrustedEnforcementVerdictEngine
from app.enforcement_plane.enums import TrustVerdictClass
from datetime import datetime

def test_enforcement_registry_integrity():
    registry = CanonicalEnforcementRegistry()

    trigger = TriggerRecord(trigger_id="TRG-1", basis="POLICY_BREACH", evidence_ref="EV-1", is_authoritative=True)
    scope = ScopeBoundRecord(actor_scope="User1", beneficiary_impact="LOW")

    enforcement = EnforcementObject(
        enforcement_id="ENF-1",
        enforcement_class=EnforcementClass.BLOCK,
        owner="Admin",
        trigger=trigger,
        scope=scope,
        reversibility=ReversibilityClass.FULLY_REVERSIBLE,
        due_process=DueProcessClass.PRE_REVIEWED,
        appeal_posture=AppealClass.APPEALABLE
    )

    registry.register(enforcement)

    retrieved = registry.get("ENF-1")
    assert retrieved is not None
    assert retrieved.enforcement_class == EnforcementClass.BLOCK

def test_indefinite_hold_detection():
    trigger = TriggerRecord(trigger_id="TRG-2", basis="RISK", evidence_ref="EV-2", is_authoritative=True)
    scope = ScopeBoundRecord(actor_scope="System", beneficiary_impact="HIGH")

    enforcement = EnforcementObject(
        enforcement_id="ENF-2",
        enforcement_class=EnforcementClass.HOLD,
        owner="Admin",
        trigger=trigger,
        scope=scope,
        reversibility=ReversibilityClass.FULLY_REVERSIBLE,
        due_process=DueProcessClass.POST_REVIEW_REQUIRED,
        appeal_posture=AppealClass.APPEALABLE
    )

    engine = TrustedEnforcementVerdictEngine()
    verdict = engine.evaluate(enforcement)

    assert verdict.verdict == TrustVerdictClass.BLOCKED
    assert any("Indefinite Hold Detected" in b for b in verdict.blockers)

def test_due_process_bypass_detection():
    trigger = TriggerRecord(trigger_id="TRG-3", basis="OBLIGATION_MISS", evidence_ref="EV-3", is_authoritative=True)
    scope = ScopeBoundRecord(actor_scope="User2", beneficiary_impact="MEDIUM")

    enforcement = EnforcementObject(
        enforcement_id="ENF-3",
        enforcement_class=EnforcementClass.SANCTION,
        owner="System",
        trigger=trigger,
        scope=scope,
        reversibility=ReversibilityClass.IRREVERSIBLE,
        due_process=DueProcessClass.EMERGENCY_BYPASS,
        appeal_posture=AppealClass.DUE_PROCESS_BYPASSED,
        expiry_at=datetime.now()
    )

    engine = TrustedEnforcementVerdictEngine()
    verdict = engine.evaluate(enforcement)

    assert verdict.verdict == TrustVerdictClass.DEGRADED
    assert any("Due Process Bypass" in w for w in verdict.debt_warnings)

def test_weak_evidence_caution():
    trigger = TriggerRecord(trigger_id="TRG-4", basis="SUSPICION", evidence_ref="EV-4", is_authoritative=False)
    scope = ScopeBoundRecord(actor_scope="User3", beneficiary_impact="LOW")

    enforcement = EnforcementObject(
        enforcement_id="ENF-4",
        enforcement_class=EnforcementClass.INTERVENTION,
        owner="System",
        trigger=trigger,
        scope=scope,
        reversibility=ReversibilityClass.FULLY_REVERSIBLE,
        due_process=DueProcessClass.PRE_REVIEWED,
        appeal_posture=AppealClass.APPEALABLE,
        expiry_at=datetime.now()
    )

    engine = TrustedEnforcementVerdictEngine()
    verdict = engine.evaluate(enforcement)

    assert verdict.verdict == TrustVerdictClass.CAUTION
    assert verdict.factors["trigger_basis"] == "Weak Evidence"
