from app.reliability.slos import SLORegistry
from app.reliability.models import SLODefinition, SLOTarget, SLOWindow
from app.reliability.enums import ReliabilityDomain, SLOClass
from app.reliability.exceptions import InvalidSLODefinition
import pytest


def test_slo_definition_validation():
    registry = SLORegistry()

    with pytest.raises(InvalidSLODefinition):
        registry.register(
            SLODefinition(
                slo_id="invalid_slo",
                domain=ReliabilityDomain.MARKET_TRUTH,
                slo_class=SLOClass.STANDARD,
                name="Test",
                description="Test",
                target=SLOTarget(target_value=-10.0, unit="ms"),
                windows=[SLOWindow(window_id="w1", duration_seconds=60)],
            )
        )

    slos = registry.list_all()
    assert len(slos) >= 3
