import pytest
from app.continuity_plane.repository import ContinuityRepository

def test_continuity_repository():
    repo = ContinuityRepository()
    assert repo is not None
