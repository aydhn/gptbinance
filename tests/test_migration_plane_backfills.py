import pytest
from app.migration_plane.backfills import BackfillManager

def test_execute_backfill():
    manager = BackfillManager()
    result = manager.execute_backfill("mig_001", True)
    assert result.is_successful is True
    assert result.is_required is True
