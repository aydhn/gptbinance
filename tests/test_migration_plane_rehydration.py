import pytest
from app.migration_plane.rehydration import RehydrationManager

def test_execute_rehydration():
    manager = RehydrationManager()
    result = manager.execute_rehydration("mig_001")
    assert result.is_successful is True
