from app.incident_plane.quality import IncidentQualityReport

def test_incident_quality():
    report = IncidentQualityReport(incident_id="INC-001", is_high_quality=False)
    assert report.is_high_quality is False
