import pytest
from app.clearing_plane.omnibus import OmnibusManager
from app.clearing_plane.exceptions import InvalidSegregationPostureError

def test_omnibus_segregation_clean():
    manager = OmnibusManager()
    manager.register("rec_1", {"contains_house_funds": False, "portability_tested": True})
    res = manager.evaluate("rec_1")
    assert res["status"] == "omnibus_segregation_clean"

def test_omnibus_theater_raises_error():
    manager = OmnibusManager()
    manager.register("rec_2", {"contains_house_funds": True, "portability_tested": True})
    with pytest.raises(InvalidSegregationPostureError):
        manager.evaluate("rec_2")
