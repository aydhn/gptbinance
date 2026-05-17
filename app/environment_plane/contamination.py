from app.environment_plane.models import EnvironmentContaminationRecord
from app.environment_plane.enums import ContaminationClass

def record_contamination(contamination_class: ContaminationClass, severity: str, blast_radius: str) -> EnvironmentContaminationRecord:
    return EnvironmentContaminationRecord(contamination_class=contamination_class, severity=severity, blast_radius=blast_radius)
