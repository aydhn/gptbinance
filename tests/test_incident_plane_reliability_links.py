from app.incident_plane.reliability_links import ReliabilityLink

def test_reliability_linkage():
    link = ReliabilityLink(incident_id="INC-001", slo_breach_id="SLO-001")
    assert link.incident_id == "INC-001"
    assert link.slo_breach_id == "SLO-001"
