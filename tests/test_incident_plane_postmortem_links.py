from app.incident_plane.postmortem_links import PostmortemLink

def test_postmortem_requirement_classes():
    link = PostmortemLink(incident_id="INC-001", postmortem_id="PM-001", is_mandatory=True)
    assert link.is_mandatory is True
