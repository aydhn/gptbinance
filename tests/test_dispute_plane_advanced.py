import pytest
from app.dispute_plane.models import *
from app.dispute_plane.enums import *
from app.dispute_plane.exceptions import *
from app.dispute_plane.registry import CanonicalDisputeRegistry
from app.dispute_plane.trust import TrustedDisputeVerdictEngine
from app.dispute_plane.complaints import ComplaintManager
from app.dispute_plane.debt import DebtTracker
from app.policy_kernel.invariants import verify_dispute_invariants
from app.enforcement_plane.dispute_integration import check_dispute_posture as check_enforcement_dispute
from app.rights_plane.dispute_integration import check_dispute_posture as check_rights_dispute
from app.liability_plane.dispute_integration import check_dispute_posture as check_liability_dispute
from app.authority_plane.dispute_integration import check_dispute_posture as check_authority_dispute
from app.precedent_plane.dispute_integration import check_dispute_posture as check_precedent_dispute
from app.jurisdiction_plane.dispute_integration import check_dispute_posture as check_jurisdiction_dispute
from app.finality_plane.dispute_integration import check_dispute_posture as check_finality_dispute
from app.commitment_plane.dispute_integration import check_dispute_posture as check_commitment_dispute
from app.remedy_plane.dispute_integration import check_dispute_posture as check_remedy_dispute
from app.representation_plane.dispute_integration import check_dispute_posture as check_representation_dispute
from app.interpretation_plane.dispute_integration import check_dispute_posture as check_interpretation_dispute
from app.adversarial_plane.dispute_integration import check_dispute_posture as check_adversarial_dispute
from app.tradeoff_plane.dispute_integration import check_dispute_posture as check_tradeoff_dispute
from app.epistemic_plane.dispute_integration import check_dispute_posture as check_epistemic_dispute
from app.semantic_plane.dispute_integration import check_dispute_posture as check_semantic_dispute
from app.temporal_plane.dispute_integration import check_dispute_posture as check_temporal_dispute
from app.provenance_plane.dispute_integration import check_dispute_posture as check_provenance_dispute
from app.autonomy_plane.dispute_integration import check_dispute_posture as check_autonomy_dispute
from app.federation_plane.dispute_integration import check_dispute_posture as check_federation_dispute
from app.constitution_plane.dispute_integration import check_dispute_posture as check_constitution_dispute
from app.contract_plane.dispute_integration import check_dispute_posture as check_contract_dispute
from app.compliance_plane.dispute_integration import check_dispute_posture as check_compliance_dispute
from app.security_plane.dispute_integration import check_dispute_posture as check_security_dispute
from app.incident_plane.dispute_integration import check_dispute_posture as check_incident_dispute
from app.release_plane.dispute_integration import check_dispute_posture as check_release_dispute
from app.migration_plane.dispute_integration import check_dispute_posture as check_migration_dispute
from app.policy_plane.dispute_integration import check_dispute_posture as check_policy_dispute
from app.scenario_plane.dispute_integration import check_dispute_posture as check_scenario_dispute
from app.state_plane.dispute_integration import check_dispute_posture as check_state_dispute

def test_registry_integration():
    registry = CanonicalDisputeRegistry()
    d = DisputeRecord(dispute_id="D-REG-1", dispute_class=DisputeClass.RIGHTS_CLAIM, owner="sys", scope="live")
    registry.register(d)
    assert registry.get("D-REG-1") == d
    assert len(registry.all()) == 1

def test_no_dismissal_theater():
    d = DisputeRecord(dispute_id="D-DT-1", dispute_class=DisputeClass.COMPLIANCE_FINDING, owner="sys", scope="live")
    d.dismissals.append(DismissalRecord(dismissal_id="DIS-1", reason="strategic", with_prejudice=True))
    v = TrustedDisputeVerdictEngine.evaluate(d)
    assert any("Dismissal Theater Risk" in c for c in v.cautions)

def test_debt_tracker():
    d = DisputeRecord(dispute_id="D-DEBT-1", dispute_class=DisputeClass.CONTRACT_BREACH, owner="sys", scope="live")
    d.issues.append(IssueRecord(issue_id="I-1", issue_class=IssueClass.MERITS, description="desc", resolved=False))
    tracker = DebtTracker()
    debt = tracker.calculate_debt(d)
    assert debt == 100

def test_policy_invariants():
    invariants = verify_dispute_invariants()
    assert len(invariants) == 4
    assert "no trusted high-risk action" in invariants[0]

def test_integrations():
    assert "Explicit caution" in check_enforcement_dispute()
    assert "Explicit caution" in check_rights_dispute()
    assert "Explicit caution" in check_liability_dispute()
    assert "Explicit caution" in check_authority_dispute()
    assert "Explicit caution" in check_precedent_dispute()
    assert "Explicit caution" in check_jurisdiction_dispute()
    assert "Explicit caution" in check_finality_dispute()
    assert "Explicit caution" in check_commitment_dispute()
    assert "Explicit caution" in check_remedy_dispute()
    assert "Explicit caution" in check_representation_dispute()
    assert "Explicit caution" in check_interpretation_dispute()
    assert "Explicit caution" in check_adversarial_dispute()
    assert "Explicit caution" in check_tradeoff_dispute()
    assert "Explicit caution" in check_epistemic_dispute()
    assert "Explicit caution" in check_semantic_dispute()
    assert "Explicit caution" in check_temporal_dispute()
    assert "Explicit caution" in check_provenance_dispute()
    assert "Explicit caution" in check_autonomy_dispute()
    assert "Explicit caution" in check_federation_dispute()
    assert "Explicit caution" in check_constitution_dispute()
    assert "Explicit caution" in check_contract_dispute()
    assert "Explicit caution" in check_compliance_dispute()
    assert "Explicit caution" in check_security_dispute()
    assert "Explicit caution" in check_incident_dispute()
    assert "Explicit caution" in check_release_dispute()
    assert "Explicit caution" in check_migration_dispute()
    assert "Explicit caution" in check_policy_dispute()
    assert "Explicit caution" in check_scenario_dispute()
    assert "Explicit caution" in check_state_dispute()
