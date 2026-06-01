import pytest
from app.drift_plane.scars import ScarManager
from app.drift_plane.enums import ScarClass

def test_scar_reactivation_creation():
    manager = ScarManager()
    manager.add_scar("reactivation-1", ScarClass.VISIBLE)

    scar = manager.get_scar("reactivation-1")
    assert scar is not None
    assert scar.scar_id == "reactivation-1"
    assert scar.class_type == ScarClass.VISIBLE
