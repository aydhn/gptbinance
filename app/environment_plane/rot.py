from app.environment_plane.models import EnvironmentRotRecord

def record_rot(rot_description: str, severity: str) -> EnvironmentRotRecord:
    return EnvironmentRotRecord(rot_description=rot_description, severity=severity)
