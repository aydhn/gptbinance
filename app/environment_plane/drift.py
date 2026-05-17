from app.environment_plane.models import DriftRecord

def record_drift(severity: str, description: str) -> DriftRecord:
    return DriftRecord(severity=severity, description=description)
