import pytest
from app.drift_plane.baselines import BaselineManager
from app.drift_plane.models import BaselineScopeRecord
from app.drift_plane.enums import BaselineClass

def test_baseline_creation():
    manager = BaselineManager()
    scope = BaselineScopeRecord(included_domains=["domain1"])
    manager.set_baseline("baseline-1", BaselineClass.APPROVED, "owner-1", scope)

    baseline = manager.get_baseline("baseline-1")
    assert baseline is not None
    assert baseline.baseline_id == "baseline-1"
    assert baseline.class_type == BaselineClass.APPROVED
    assert baseline.owner == "owner-1"
    assert "domain1" in baseline.scope.included_domains
