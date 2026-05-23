import pytest
from app.liability_plane.repository import LiabilityRepository
from app.liability_plane.models import LiabilityObject, LiabilityClass
from app.liability_plane.quality import QualityManager
from app.liability_plane.caps import CapManager
from app.liability_plane.enums import LiabilityCapClass

def test_quality_warnings():
    repo = LiabilityRepository()
    obj = LiabilityObject(liability_id="L-105", liability_class=LiabilityClass.INCIDENT_LIABILITY, owner="ops", scope="net", causation_posture="open", exposure_posture="open")
    repo.register_and_save(obj)

    cap_mgr = CapManager(repo)
    cap_mgr.add_cap("L-105", LiabilityCapClass.HARD_CAP, 1000.0, "USD", [])

    qual_mgr = QualityManager(repo)
    warnings = qual_mgr.check_quality("L-105")

    # Missing causation
    assert "Missing causation basis" in warnings
    # Cap without residual exposure
    assert "Cap comfort warning: Cap applied without explicit residual exposure tracking" in warnings
