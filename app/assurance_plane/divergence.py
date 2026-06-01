from app.assurance_plane.models import AssuranceDivergenceReport

def create_divergence_report(report_id: str, assurance_id: str, severity: str, details: str) -> AssuranceDivergenceReport:
    return AssuranceDivergenceReport(
        report_id=report_id,
        assurance_id=assurance_id,
        severity=severity,
        details=details
    )
