import pytest
from app.dispute_plane.models import *
from app.dispute_plane.enums import *
from app.dispute_plane.exceptions import *
from app.dispute_plane.registry import dispute_registry
from app.dispute_plane.trust import TrustedDisputeVerdictEngine
from app.dispute_plane.complaints import ComplaintManager

def test_dispute_registry():
    d = DisputeRecord(dispute_id="D-100", dispute_class=DisputeClass.RIGHTS_CLAIM, owner="sys", scope="live")
    dispute_registry.register(d)
    assert dispute_registry.get("D-100") == d

def test_no_issue_burial():
    d = DisputeRecord(dispute_id="D-101", dispute_class=DisputeClass.CONTRACT_BREACH, owner="sys", scope="live")
    d.issues.append(IssueRecord(issue_id="I-1", issue_class=IssueClass.MERITS, description="Breach of section 4", resolved=False))
    d.disposition_posture = DispositionClass.RESOLVED_ON_MERITS

    with pytest.raises(DisputeBurialViolation):
        TrustedDisputeVerdictEngine.evaluate(d)

def test_no_off_record_adjudication():
    d = DisputeRecord(dispute_id="D-102", dispute_class=DisputeClass.COMPLIANCE_FINDING, owner="sys", scope="live")
    d.rulings.append(RulingRecord(ruling_id="R-1", ruling_class=RulingClass.MERITS, rationale="Secret reason", on_record=False))

    with pytest.raises(OffRecordAdjudicationViolation):
        TrustedDisputeVerdictEngine.evaluate(d)

def test_no_complaint_shortcut():
    d = DisputeRecord(dispute_id="D-103", dispute_class=DisputeClass.RIGHTS_CLAIM, owner="sys", scope="live")
    d.disposition_posture = DispositionClass.RESOLVED_ON_MERITS
    c = ComplaintRecord(complaint_id="C-1", complaint_class=ComplaintClass.FORMAL, description="Test", is_admitted=False)

    cm = ComplaintManager()
    with pytest.raises(InvalidComplaintError):
        cm.process(d, c)

def test_trust_verdict_caution():
    d = DisputeRecord(dispute_id="D-104", dispute_class=DisputeClass.ENFORCEMENT_APPEAL, owner="sys", scope="live")
    d.appeals.append(AppealRecord(appeal_id="A-1", appeal_class=AppealClass.PENDING, stays_enforcement=True))

    v = TrustedDisputeVerdictEngine.evaluate(d)
    assert v.verdict == DisputeTrustVerdict.CAUTION
    assert "Appeal Starvation Risk" in v.cautions[0]
