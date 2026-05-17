from app.environment_plane.models import EnvironmentResetRecord

def define_reset(reset_type: str, drift_notes: str) -> EnvironmentResetRecord:
    return EnvironmentResetRecord(reset_type=reset_type, drift_notes=drift_notes)
