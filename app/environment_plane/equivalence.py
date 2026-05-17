from app.environment_plane.models import EnvironmentEquivalenceReport
from app.environment_plane.enums import EquivalenceVerdict

def evaluate_equivalence(verdict: EquivalenceVerdict, proof_notes: str) -> EnvironmentEquivalenceReport:
    return EnvironmentEquivalenceReport(verdict=verdict, proof_notes=proof_notes)
