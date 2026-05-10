import pytest
from app.incident_plane.status import IncidentStatusMachine
from app.incident_plane.closure import ClosureReadinessEvaluator
from app.incident_plane.enums import IncidentStatus, IncidentSeverity, IncidentUrgency, VerificationVerdict
from app.incident_plane.exceptions import InvalidStatusTransition, InvalidClosureState
from app.incident_plane.models import IncidentManifest, RecoveryVerificationRecord
from datetime import datetime, timezone

def test_status_transition_enforces_rules():
    event = IncidentStatusMachine.transition(IncidentStatus.DETECTED, IncidentStatus.TRIAGING, "Start Triage", "operator_1")
    assert event.new_status == IncidentStatus.TRIAGING

    with pytest.raises(InvalidStatusTransition):
        IncidentStatusMachine.transition(IncidentStatus.DETECTED, IncidentStatus.RESOLVED, "Quick fix", "operator_1")

def test_closure_requires_verification():
    manifest = IncidentManifest(
        incident_id="INC-001",
        family="data_integrity_incident",
        severity=IncidentSeverity.SEV2_MEDIUM,
        urgency=IncidentUrgency.TIME_BOUNDED,
        current_status=IncidentStatus.RESOLVED,
        blast_radius={"scope": "market_data"},
        primary_owner="operator_1",
        signals=[],
        triage=None,
        timeline=[],
        verification=None,
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc)
    )

    with pytest.raises(InvalidClosureState, match="lacks successful recovery verification"):
        ClosureReadinessEvaluator.assert_ready_for_closure(manifest)

    manifest.verification = RecoveryVerificationRecord(
        incident_id="INC-001",
        objective_checks_passed=True,
        no_regression_checks_passed=True,
        quiet_period_met=True,
        residual_risk_assessment="None",
        verdict=VerificationVerdict.VERIFIED,
        verified_by="operator_2",
        proof_notes="Logs checked, data flowing",
        verified_at=datetime.now(timezone.utc)
    )

    assert ClosureReadinessEvaluator.assert_ready_for_closure(manifest) is True
