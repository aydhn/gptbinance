import pytest
from app.liability_plane.repository import LiabilityRepository
from app.liability_plane.models import LiabilityObject, LiabilityClass
from app.liability_plane.causation import CausationManager
from app.liability_plane.enums import CausationClass

def test_causation_manager():
    repo = LiabilityRepository()
    obj = LiabilityObject(liability_id="L-103", liability_class=LiabilityClass.INCIDENT_LIABILITY, owner="ops", scope="net", causation_posture="open", exposure_posture="open")
    repo.register_and_save(obj)

    manager = CausationManager(repo)
    cause = manager.add_causation("L-103", CausationClass.DIRECT, "sys-agent", "Triggered failover incorrectly", [])

    assert cause.causation_class == CausationClass.DIRECT
    assert len(repo.get_liability_record("L-103").causation) == 1
