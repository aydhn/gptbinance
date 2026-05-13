import pytest
from app.continuity_plane.services import ContinuityServiceRegistry
from app.continuity_plane.registry import CanonicalContinuityRegistry
from app.continuity_plane.models import ContinuityService
from app.continuity_plane.enums import ContinuityServiceClass

def test_service_registry():
    canonical = CanonicalContinuityRegistry()
    registry = ContinuityServiceRegistry(canonical)

    service = ContinuityService(
        service_id="srv_1",
        service_class=ContinuityServiceClass.CRITICAL_PATH,
        owner="admin",
        description="main"
    )
    registry.register_service(service)

    retrieved = registry.get_service("srv_1")
    assert retrieved is not None
    assert retrieved.service_id == "srv_1"

    services = registry.list_services()
    assert len(services) == 1
