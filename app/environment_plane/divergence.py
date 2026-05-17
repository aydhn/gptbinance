from app.environment_plane.models import EnvironmentDivergenceReport

def report_divergence(severity: str, blast_radius: str) -> EnvironmentDivergenceReport:
    return EnvironmentDivergenceReport(severity=severity, blast_radius=blast_radius)
