from app.incident_plane.verification import IncidentVerificationEngine
from app.incident_plane.enums import VerificationVerdict

def test_verification_quiet_period():
    record = IncidentVerificationEngine.verify("INC-001", checks_passed=True, operator="op1", proof="No errors in 30 mins")
    assert record.quiet_period_met is True
    assert record.verdict == VerificationVerdict.VERIFIED
