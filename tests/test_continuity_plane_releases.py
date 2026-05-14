import pytest
from app.continuity_plane.releases import ContinuityReleaseLinkage

def test_release_linkage():
    linkage = ContinuityReleaseLinkage()
    assert linkage is not None
