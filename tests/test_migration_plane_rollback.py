import pytest
from app.migration_plane.rollback import RollbackManager
from app.migration_plane.enums import RollbackClass

def test_execute_rollback():
    manager = RollbackManager()
    result = manager.execute_rollback("mig_001", RollbackClass.SUPPORTED)
    assert result.is_successful is True
    assert result.rollback_class == RollbackClass.SUPPORTED
