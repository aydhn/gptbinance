from app.incident_plane.closure import ClosureReadinessEvaluator
from app.incident_plane.models import IncidentManifest, RecoveryVerificationRecord
from app.incident_plane.enums import IncidentStatus, IncidentSeverity, IncidentUrgency, VerificationVerdict
from app.incident_plane.exceptions import InvalidClosureState
from datetime import datetime, timezone
import pytest

def test_closure_readiness_blockers():
    manifest = IncidentManifest(
        incident_id="INC-001",
        family="data_integrity_incident",
        severity=IncidentSeverity.SEV2_MEDIUM,
        urgency=IncidentUrgency.TIME_BOUNDED,
        current_status=IncidentStatus.RECOVERING,
        blast_radius={"scope": "market_data"},
        primary_owner="operator_1"
    )

    with pytest.raises(InvalidClosureState, match="must be in RESOLVED state"):
        ClosureReadinessEvaluator.assert_ready_for_closure(manifest)

    manifest.current_status = IncidentStatus.RESOLVED

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
