import pytest
from app.liability_plane.repository import LiabilityRepository
from app.liability_plane.models import LiabilityObject, LiabilityClass
from app.liability_plane.responsibility import ResponsibilityManager
from app.liability_plane.enums import ResponsibilityClass

def test_responsibility_manager():
    repo = LiabilityRepository()
    obj = LiabilityObject(liability_id="L-102", liability_class=LiabilityClass.INCIDENT_LIABILITY, owner="ops", scope="db", causation_posture="open", exposure_posture="open")
    repo.register_and_save(obj)

    manager = ResponsibilityManager(repo)
    resp = manager.add_responsibility("L-102", ResponsibilityClass.PRIMARY, "admin-1", "Primary config change", [])

    assert resp.responsibility_class == ResponsibilityClass.PRIMARY
    assert len(repo.get_liability_record("L-102").responsibility) == 1
