import pytest
from app.change_plane.registry import CanonicalChangeRegistry
from app.change_plane.models import ChangeObject
from app.change_plane.enums import ChangeClass
from app.change_plane.exceptions import InvalidChangeObjectError

def test_change_registry_registration():
    registry = CanonicalChangeRegistry()
    change = ChangeObject(
        change_id="chg_test_1",
        name="Test Change",
        owner="Test Owner",
        change_class=ChangeClass.STANDARD,
        target_surface="test_surface"
    )
    registry.register(change)
    retrieved = registry.get_change("chg_test_1")
    assert retrieved is not None
    assert retrieved.change_id == "chg_test_1"

def test_change_registry_requires_id():
    registry = CanonicalChangeRegistry()
    change = ChangeObject(
        change_id="",
        name="Invalid Change",
        owner="Test Owner",
        change_class=ChangeClass.STANDARD,
        target_surface="test_surface"
    )
    with pytest.raises(InvalidChangeObjectError):
        registry.register(change)
