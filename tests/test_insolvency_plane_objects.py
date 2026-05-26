import pytest
from app.insolvency_plane.objects import create_insolvency_object
from app.insolvency_plane.enums import InsolvencyClass

def test_create_object():
    obj = create_insolvency_object("obj-001", InsolvencyClass.MIGRATION_LOSS_INSOLVENCY, "user1", "local")
    assert obj.id == "obj-001"
    assert obj.class_type == InsolvencyClass.MIGRATION_LOSS_INSOLVENCY
