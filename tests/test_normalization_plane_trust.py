import pytest
from app.normalization_plane.trust import TrustVerdictEngine
from app.normalization_plane.models import NormalizationRecord, ReentryGateRecord, ResidualScarRecord, LimitLiftRecord
from app.normalization_plane.enums import NormalizationClass, ReentryGateStatus, ResidualScarClass, LimitLiftClass, NormalizationTrustVerdict

def test_trust_verdict_engine_blocked_by_hidden_scar():
    record = NormalizationRecord(
        normalization_id="NORM-001",
        normalization_class=NormalizationClass.POST_RESOLUTION,
        owner="SYSTEM",
        domain="Trading",
        reentry_gate=ReentryGateRecord(gate_id="G1", status=ReentryGateStatus.CLEARED, notes="Safe"),
        residual_scars=[ResidualScarRecord(scar_id="S1", scar_class=ResidualScarClass.HIDDEN, description="Hidden scar", domain="Trading", is_hidden=True)]
    )
    engine = TrustVerdictEngine()
    report = engine.evaluate(record)
    assert report.verdict == NormalizationTrustVerdict.BLOCKED
    assert "Hidden residual scar detected." in report.blockers

def test_trust_verdict_engine_caution_not_cleared_gate():
    record = NormalizationRecord(
        normalization_id="NORM-002",
        normalization_class=NormalizationClass.CUSTOMER_SAFE_REOPEN,
        owner="SYSTEM",
        domain="Trading",
        reentry_gate=ReentryGateRecord(gate_id="G2", status=ReentryGateStatus.PROVISIONAL, notes="Provisional"),
        residual_scars=[]
    )
    engine = TrustVerdictEngine()
    report = engine.evaluate(record)
    assert report.verdict == NormalizationTrustVerdict.CAUTION
    assert "Re-entry gate is not cleared." in report.cautions

def test_trust_verdict_engine_trusted():
    record = NormalizationRecord(
        normalization_id="NORM-003",
        normalization_class=NormalizationClass.SECURITY_HARDENING,
        owner="SYSTEM",
        domain="Core",
        reentry_gate=ReentryGateRecord(gate_id="G3", status=ReentryGateStatus.CLEARED, notes="Cleared"),
        residual_scars=[]
    )
    engine = TrustVerdictEngine()
    report = engine.evaluate(record)
    assert report.verdict == NormalizationTrustVerdict.TRUSTED
