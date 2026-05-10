from app.incident_plane.divergence import IncidentDivergenceReport

def test_incident_divergence():
    report = IncidentDivergenceReport(incident_id="INC-001", has_divergence=True)
    assert report.has_divergence is True
