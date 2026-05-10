import pytest
from app.release_plane.activation_links import ActivationLinkManager
from app.release_plane.exceptions import ReleasePlaneError

def test_activation_link():
    manager = ActivationLinkManager()
    link = manager.link_activation("live_full", "rel-1", ["canary_report"])
    assert link.release_ref.release_id == "rel-1"

def test_release_less_activation_rejection():
    manager = ActivationLinkManager()
    with pytest.raises(ReleasePlaneError):
         manager.link_activation("live_full", "", [])
