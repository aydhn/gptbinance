from app.indemnity_plane.models import IndemnityEquivalenceReport, EquivalenceVerdict
def evaluate_equivalence(indemnity_id: str) -> IndemnityEquivalenceReport:
    return IndemnityEquivalenceReport(verdict=EquivalenceVerdict.EQUIVALENT)
