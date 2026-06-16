from app.indemnity_plane.models import IndemnityDivergenceReport
def analyze_divergence(indemnity_id: str) -> IndemnityDivergenceReport:
    return IndemnityDivergenceReport(divergence_type="none", severity="low")
