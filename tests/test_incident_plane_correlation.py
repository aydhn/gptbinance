from app.incident_plane.correlation import IncidentCorrelationEngine

def test_correlated_family_grouping():
    report = IncidentCorrelationEngine.correlate(["INC-001", "INC-003"], "shared_dependency")
    assert report.family_id == "FAM-001"
    assert report.relation_type == "shared_dependency"
