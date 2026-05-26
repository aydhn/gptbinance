import pytest
from app.insolvency_plane.repository import InsolvencyRepository
from app.insolvency_plane.models import InsolvencyObject, InsolvencyObjectRef
from app.insolvency_plane.enums import InsolvencyClass

def test_insolvency_registry_integrity():
    repo = InsolvencyRepository()
    obj = InsolvencyObject(
        id="ins-001",
        class_type=InsolvencyClass.SETTLEMENT_FAILURE_INSOLVENCY,
        owner="test-owner",
        scope="global"
    )
    repo.registry.register(obj)
    fetched = repo.registry.get("ins-001")
    assert fetched is not None
    assert fetched.class_type == InsolvencyClass.SETTLEMENT_FAILURE_INSOLVENCY
