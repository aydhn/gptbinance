from app.incident_plane.models import RecoveryVerificationRecord
from app.incident_plane.enums import VerificationVerdict
from datetime import datetime, timezone

class IncidentVerificationEngine:
    @staticmethod
    def verify(incident_id: str, checks_passed: bool, operator: str, proof: str) -> RecoveryVerificationRecord:
        return RecoveryVerificationRecord(
            incident_id=incident_id,
            objective_checks_passed=checks_passed,
            no_regression_checks_passed=checks_passed,
            quiet_period_met=True,
            residual_risk_assessment="Low",
            verdict=VerificationVerdict.VERIFIED if checks_passed else VerificationVerdict.FAILED,
            verified_at=datetime.now(timezone.utc),
            verified_by=operator,
            proof_notes=proof
        )
