import pytest
from app.liability_plane.repository import LiabilityRepository
from app.liability_plane.models import LiabilityObject, LiabilityClass
from app.liability_plane.caps import CapManager
from app.liability_plane.enums import LiabilityCapClass

def test_cap_manager():
    repo = LiabilityRepository()
    obj = LiabilityObject(liability_id="L-104", liability_class=LiabilityClass.CONTRACT_BREACH_LIABILITY, owner="legal", scope="global", causation_posture="open", exposure_posture="open")
    repo.register_and_save(obj)

    manager = CapManager(repo)
    cap = manager.add_cap("L-104", LiabilityCapClass.CONTRACT_CAP, 50000.0, "USD", [])

    assert cap.amount == 50000.0
    assert len(repo.get_liability_record("L-104").caps) == 1
