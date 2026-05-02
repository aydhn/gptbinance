import pytest
from app.release.storage import ReleaseStorage


def test_release_storage():
    storage = ReleaseStorage()
    assert storage is not None
