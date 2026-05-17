import pytest
from datetime import datetime, timezone
from app.change_plane.trust import ChangeTrustEngine
from app.change_plane.models import ChangeObject, ChangeRequestRecord, ImpactAssessmentRecord, ApprovalChainRecord, ChangeWindowRecord, ChangeVerificationRecord, RollbackPlanRecord
from app.change_plane.enums import ChangeClass, RequestClass, ApprovalClass, WindowClass, VerificationClass, ChangeTrustVerdict, RollbackClass

def build_trusted_change():
    req = ChangeRequestRecord(
        request_id="r1", change_id="c1", request_class=RequestClass.RUNTIME,
        initiating_reason="r", target_surfaces=["s"], expected_benefit="b", expected_downside="d",
        requester_metadata={}, requested_at=datetime.now(timezone.utc)
    )
    imp = ImpactAssessmentRecord(
        change_id="c1", system_impact="l", customer_business_impact="l",
        reliability_security_compliance_impact="l", capacity_cost_impact="l", residual_impact_notes="n"
    )
    appr = ApprovalChainRecord(
        change_id="c1", approval_class=ApprovalClass.NORMAL_APPROVAL, approvers=["user1"],
        approved_at=datetime.now(timezone.utc), conflict_notes=[]
    )
    win = ChangeWindowRecord(
        window_id="w1", change_id="c1", window_class=WindowClass.NORMAL,
        start_time=datetime.now(timezone.utc), end_time=datetime.now(timezone.utc), constraints=[]
    )
    rb = RollbackPlanRecord(
        change_id="c1", rollback_class=RollbackClass.TESTED_READY,
        feasibility="High", prerequisites=[], tested_posture="Verified", caveats=[]
    )
    verf = ChangeVerificationRecord(
        verification_id="v1", change_id="c1", verification_class=VerificationClass.POST_CHANGE,
        sufficiency_notes="ok", verified_at=datetime.now(timezone.utc)
    )
    return ChangeObject(
        change_id="c1", name="n", owner="o", change_class=ChangeClass.NORMAL, target_surface="s",
        request=req, impact=imp, approval=appr, window=win, rollback=rb, verification=verf
    )

def test_trust_engine_trusted():
    change = build_trusted_change()
    engine = ChangeTrustEngine()
    verdict = engine.evaluate(change)
    assert verdict.verdict == ChangeTrustVerdict.TRUSTED

def test_trust_engine_blocked_missing_approval():
    change = build_trusted_change()
    change.approval = None
    engine = ChangeTrustEngine()
    verdict = engine.evaluate(change)
    assert verdict.verdict == ChangeTrustVerdict.BLOCKED

def test_trust_engine_caution_unverified():
    change = build_trusted_change()
    change.verification.verification_class = VerificationClass.UNVERIFIED
    engine = ChangeTrustEngine()
    verdict = engine.evaluate(change)
    assert verdict.verdict == ChangeTrustVerdict.CAUTION
