import pytest
from app.adaptation_plane.models import AdaptationRecord
from app.adaptation_plane.enums import AdaptationClass
from app.adaptation_plane.registry import RegistryManager
from app.adaptation_plane.objects import ObjectsManager
from app.adaptation_plane.exceptions import InvalidAdaptationObject

def test_object_lifecycle():
    registry = RegistryManager()
    objects = ObjectsManager(registry)

    record = AdaptationRecord(
        adaptation_id="ADAPT-003",
        class_type=AdaptationClass.BENEFICIARY_HARM_REDUCTION,
        owner="product_team",
        scope="local",
        status="draft" # will be forced to proposed
    )

    objects.create_object(record)
    assert registry.get_adaptation("ADAPT-003").status == "proposed"

    objects.transition_status("ADAPT-003", "deployed")
    assert registry.get_adaptation("ADAPT-003").status == "deployed"

    with pytest.raises(InvalidAdaptationObject):
        objects.transition_status("ADAPT-003", "invalid_status")
