import pytest

from app.reliability_plane.enums import ReliabilityServiceClass
from app.reliability_plane.exceptions import InvalidReliabilityDefinition
from app.reliability_plane.models import ReliabilityService
from app.reliability_plane.registry import CanonicalReliabilityRegistry


def test_registry_requires_service_id():
    registry = CanonicalReliabilityRegistry()
    with pytest.raises(InvalidReliabilityDefinition):
        registry.register_service(
            ReliabilityService(
                service_id="", service_class=ReliabilityServiceClass.EXECUTION
            )
        )


def test_registry_registers_service():
    registry = CanonicalReliabilityRegistry()
    service = ReliabilityService(
        service_id="exec-1", service_class=ReliabilityServiceClass.EXECUTION
    )
    registry.register_service(service)

    assert registry.get_service("exec-1") is not None
    assert len(registry.list_services()) == 1
