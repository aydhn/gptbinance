import pytest
from app.clearing_plane.individual import IndividualManager
from app.clearing_plane.exceptions import InvalidSegregationPostureError

def test_individual_segregation_clean():
    manager = IndividualManager()
    manager.register("rec_1", {"beneficiary_verified": True, "fellow_customer_risk": False})
    res = manager.evaluate("rec_1")
    assert res["status"] == "individual_segregation_clean"

def test_individual_theater_raises_error():
    manager = IndividualManager()
    manager.register("rec_2", {"beneficiary_verified": True, "fellow_customer_risk": True})
    with pytest.raises(InvalidSegregationPostureError):
        manager.evaluate("rec_2")
