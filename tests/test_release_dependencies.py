import pytest
from app.release.dependencies import DependencyManager
from app.release.enums import DependencyStatus


def test_get_lock_summary():
    mgr = DependencyManager()
    summary = mgr.get_lock_summary()
    assert summary.status == DependencyStatus.SYNCED
