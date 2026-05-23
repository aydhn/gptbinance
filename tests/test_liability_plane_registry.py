import pytest
from app.liability_plane.registry import CanonicalLiabilityRegistry
from app.liability_plane.models import LiabilityObject, LiabilityClass, LiabilityState
from app.liability_plane.exceptions import InvalidLiabilityObjectError

def test_registry_registration():
    registry = CanonicalLiabilityRegistry()
    obj = LiabilityObject(
        liability_id="L-100",
        liability_class=LiabilityClass.INCIDENT_LIABILITY,
        owner="team-alpha",
        scope="production",
        causation_posture="unresolved",
        exposure_posture="open"
    )
    registry.register_liability(obj)

    fetched = registry.get_liability("L-100")
    assert fetched.liability_class == LiabilityClass.INCIDENT_LIABILITY

    with pytest.raises(InvalidLiabilityObjectError):
        registry.register_liability(obj)

    with pytest.raises(InvalidLiabilityObjectError):
        registry.get_liability("non_existent")
