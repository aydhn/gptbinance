import pytest
from app.migration_plane.reindex import ReindexManager

def test_execute_reindex():
    manager = ReindexManager()
    result = manager.execute_reindex("mig_001")
    assert result.is_successful is True
