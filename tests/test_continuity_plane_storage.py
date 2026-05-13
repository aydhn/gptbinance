import pytest
from app.continuity_plane.storage import ContinuityStorage

def test_continuity_storage():
    storage = ContinuityStorage()
    assert storage is not None
