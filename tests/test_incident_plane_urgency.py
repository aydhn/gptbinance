from app.incident_plane.urgency import IncidentUrgencyEngine
from app.incident_plane.enums import IncidentUrgency

def test_urgency_classification():
    urgency = IncidentUrgencyEngine.determine_urgency("high", 0)
    assert urgency == IncidentUrgency.IMMEDIATE
