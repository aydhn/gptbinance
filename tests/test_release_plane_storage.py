import pytest
from app.release_plane.storage import ReleasePlaneStorage
from app.release_plane.repository import ReleasePlaneRepository

class MockRelease:
    def __init__(self, release_id):
        self.release_id = release_id

def test_storage_and_repository():
    storage = ReleasePlaneStorage()
    repo = ReleasePlaneRepository(storage)

    rel1 = MockRelease("rel-1")
    repo.save_release(rel1)

    fetched = repo.get_release("rel-1")
    assert fetched is not None
    assert fetched.release_id == "rel-1"

    latest = repo.get_latest_trusted_release()
    assert latest.release_id == "rel-1"
