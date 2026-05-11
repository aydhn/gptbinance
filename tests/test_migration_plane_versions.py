import pytest
from app.migration_plane.models import MigrationVersionPair
from app.migration_plane.versions import VersionManager
from app.migration_plane.exceptions import InvalidVersionPairError

def test_valid_version_pair():
    pair = MigrationVersionPair(source_version="v1", target_version="v2")
    assert VersionManager.validate_pair(pair) is True

def test_invalid_version_pair():
    pair = MigrationVersionPair(source_version="v1", target_version="v1")
    with pytest.raises(InvalidVersionPairError):
         VersionManager.validate_pair(pair)
