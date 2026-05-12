import pytest

from app.reliability_plane.enums import (ReliabilityServiceClass, SLIClass,
                                         SLOClass)
from app.reliability_plane.exceptions import InvalidReliabilityDefinition
from app.reliability_plane.models import (ReliabilityService, SliDefinition,
                                          SloDefinition)
from app.reliability_plane.registry import CanonicalReliabilityRegistry


def test_slo_requires_existing_sli():
    registry = CanonicalReliabilityRegistry()
    service = ReliabilityService(
        service_id="exec-1", service_class=ReliabilityServiceClass.EXECUTION
    )
    registry.register_service(service)

    slo = SloDefinition(
        slo_id="slo-1",
        slo_class=SLOClass.HARD,
        sli_id="unknown-sli",
        target_value=99.9,
        window_seconds=3600,
    )
    with pytest.raises(InvalidReliabilityDefinition):
        registry.register_slo(slo)
