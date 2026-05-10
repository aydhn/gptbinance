from app.incident_plane.equivalence import IncidentEquivalenceReport

def test_incident_equivalence():
    report = IncidentEquivalenceReport(incident_id="INC-001", is_equivalent_across_envs=True, notes="Matches exactly")
    assert report.is_equivalent_across_envs is True
