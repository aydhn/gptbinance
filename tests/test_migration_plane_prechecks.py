import pytest
from app.migration_plane.prechecks import PrecheckManager
from app.migration_plane.enums import PrecheckClass

def test_execute_prechecks_passed():
    manager = PrecheckManager()
    result = manager.execute_prechecks("mig_001", ["check1", "check2"])
    assert result.status == PrecheckClass.PASSED
    assert len(result.blockers) == 0

def test_execute_prechecks_failed_no_checks():
    manager = PrecheckManager()
    result = manager.execute_prechecks("mig_001", [])
    assert result.status == PrecheckClass.FAILED
    assert len(result.blockers) > 0
