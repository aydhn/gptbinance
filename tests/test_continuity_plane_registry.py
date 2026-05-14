import pytest
from app.continuity_plane.registry import CanonicalContinuityRegistry
from app.continuity_plane.models import ContinuityService
from app.continuity_plane.enums import ContinuityServiceClass
from app.continuity_plane.exceptions import InvalidContinuityDefinition

def test_registry_valid_service():
    registry = CanonicalContinuityRegistry()
    service = ContinuityService(
        service_id="test_service",
        service_class=ContinuityServiceClass.STATE_STORE,
        owner="test_owner",
        description="test description"
    )
    registry.register(service)
    retrieved = registry.get_service("test_service")
    assert retrieved is not None
    assert retrieved.service_id == "test_service"

def test_registry_invalid_service():
    registry = CanonicalContinuityRegistry()
    with pytest.raises(InvalidContinuityDefinition):
        service = ContinuityService(
            service_id="",
            service_class=ContinuityServiceClass.STATE_STORE,
            owner="test_owner",
            description="test description"
        )
        registry.register(service)
