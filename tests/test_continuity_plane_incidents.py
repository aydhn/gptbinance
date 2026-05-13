import pytest
from app.continuity_plane.incidents import ContinuityIncidentManager
from app.continuity_plane.models import ContinuityIncidentLink

def test_incident_manager():
    manager = ContinuityIncidentManager()
    link = ContinuityIncidentLink(
        incident_id="inc_1",
        service_id="srv_1",
        link_type="recovery_trigger"
    )
    manager.record_link(link)

    links = manager.get_links_for_service("srv_1")
    assert len(links) == 1
    assert links[0].incident_id == "inc_1"
