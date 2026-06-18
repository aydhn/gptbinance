import pytest
from app.clearing_plane.defaults import DefaultsManager
from app.clearing_plane.exceptions import InvalidDefaultWaterfallError

def test_default_declared_cleanly():
    manager = DefaultsManager()
    manager.register("rec_1", {"formally_declared": True, "hedge_plan_ready": True})
    res = manager.evaluate("rec_1")
    assert res["status"] == "default_declared_cleanly"

def test_opaque_default_raises_error():
    manager = DefaultsManager()
    manager.register("rec_2", {"formally_declared": True, "hedge_plan_ready": False})
    with pytest.raises(InvalidDefaultWaterfallError):
        manager.evaluate("rec_2")
