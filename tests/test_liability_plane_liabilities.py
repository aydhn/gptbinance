import pytest
from app.liability_plane.repository import LiabilityRepository
from app.liability_plane.models import LiabilityObject, LiabilityClass, LiabilityState

def test_liability_lifecycle():
    repo = LiabilityRepository()
    obj = LiabilityObject(
        liability_id="L-101",
        liability_class=LiabilityClass.CONTRACT_BREACH_LIABILITY,
        owner="legal",
        scope="partner-x",
        causation_posture="resolved",
        exposure_posture="open"
    )
    record = repo.register_and_save(obj)
    assert record.liability.state == LiabilityState.ACTIVE

    record.liability.state = LiabilityState.SETTLED
    repo.storage.save(record)

    fetched = repo.get_liability_record("L-101")
    assert fetched.liability.state == LiabilityState.SETTLED
