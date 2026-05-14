import pytest
from app.value_plane.models import RealizedImpactRecord, EvidenceLink
from app.value_plane.realized import realized_impact_registry
from app.value_plane.enums import ImpactClass
from app.value_plane.exceptions import ValuePlaneError

def test_realized_impact_with_baseline():
    record = RealizedImpactRecord(
        realized_impact_id="ri_1",
        impact_class=ImpactClass.REALIZED_SHORT_TERM,
        value=100.0,
        horizon="Q1",
        evidence_linkage=[],
        baseline_ref="base_1"
    )
    realized_impact_registry.register(record)
    assert realized_impact_registry.get("ri_1") is not None

def test_realized_impact_without_baseline():
    with pytest.raises(ValuePlaneError):
        record = RealizedImpactRecord(
            realized_impact_id="ri_2",
            impact_class=ImpactClass.REALIZED_SHORT_TERM,
            value=100.0,
            horizon="Q1",
            evidence_linkage=[],
            baseline_ref=""
        )
        realized_impact_registry.register(record)
