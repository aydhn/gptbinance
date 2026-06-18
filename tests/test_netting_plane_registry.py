import pytest
from app.netting_plane.registry import CanonicalNettingRegistry
from app.netting_plane.enums import NettingClass, MutualityClass, CloseoutClass

def test_registry_registration():
    reg = CanonicalNettingRegistry()
    data = {
        "netting_id": "net-123",
        "class_name": NettingClass.ESCROW_RELEASE_NETTING,
        "owner": "system",
        "scope": "global",
        "mutuality_posture": MutualityClass.CLEAN_MUTUALITY,
        "closeout_posture": CloseoutClass.PRUDENT_CLOSEOUT
    }
    reg.register("net-123", data)
    assert reg.get("net-123")["netting_id"] == "net-123"
    assert len(reg.list_by_class(NettingClass.ESCROW_RELEASE_NETTING)) == 1

def test_registry_not_found():
    reg = CanonicalNettingRegistry()
    assert reg.get("unknown") == {}
