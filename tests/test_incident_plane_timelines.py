from app.incident_plane.timelines import IncidentTimelineEngine

def test_append_only_timeline():
    # Example test checking gap validation logic
    gaps = IncidentTimelineEngine.check_gaps([])
    assert gaps == []
