import pytest
from app.drift_plane.thresholds import ThresholdManager
from app.drift_plane.enums import BreachClass

def test_threshold_breach_creation():
    manager = ThresholdManager()
    manager.add_breach("breach-1", BreachClass.MATERIAL, "threshold-1")

    breach = manager.get_breach("breach-1")
    assert breach is not None
    assert breach.breach_id == "breach-1"
    assert breach.class_type == BreachClass.MATERIAL
    assert breach.threshold_id == "threshold-1"
