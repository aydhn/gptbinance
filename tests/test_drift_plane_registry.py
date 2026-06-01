import pytest
from app.drift_plane.registry import CanonicalDriftRegistry
from app.drift_plane.enums import DriftClass

def test_drift_registry_registration():
    registry = CanonicalDriftRegistry()
    registry.register_drift("drift-1", DriftClass.POST_NORMALIZATION_DRIFT)

    drift = registry.get_drift("drift-1")
    assert drift is not None
    assert drift["class_type"] == DriftClass.POST_NORMALIZATION_DRIFT
    assert drift["mandatory"] is True
    assert drift["marker"] == "production-grade"

def test_drift_registry_list():
    registry = CanonicalDriftRegistry()
    registry.register_drift("drift-1", DriftClass.POST_NORMALIZATION_DRIFT)
    registry.register_drift("drift-2", DriftClass.POST_RECAPITALIZATION_DRIFT, is_mandatory=False)

    drifts = registry.list_drifts()
    assert len(drifts) == 2
    assert "drift-1" in drifts
    assert drifts["drift-2"]["marker"] == "advisory"
