from app.environment_plane.models import EnvironmentReadinessReport
from app.environment_plane.enums import ReadinessClass

def evaluate_readiness(readiness_class: ReadinessClass, proof_notes: str) -> EnvironmentReadinessReport:
    return EnvironmentReadinessReport(readiness_class=readiness_class, proof_notes=proof_notes)
