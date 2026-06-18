import pytest
from app.netting_plane.objects import NettingObjectManager
from app.netting_plane.enums import NettingClass, MutualityClass, CloseoutClass

def test_object_creation():
    mgr = NettingObjectManager()
    data = {
        "netting_id": "obj-1",
        "class_name": NettingClass.WATERFALL_DISTRIBUTION_NETTING,
        "owner": "finance",
        "scope": "regional",
        "mutuality_posture": MutualityClass.PARTIAL_MUTUALITY,
        "closeout_posture": CloseoutClass.PARTIAL_CLOSEOUT
    }
    obj = mgr.create_object(data)
    assert obj.netting_id == "obj-1"
    assert mgr.get_object("obj-1").owner == "finance"
