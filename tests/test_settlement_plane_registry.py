import pytest
from app.settlement_plane.registry import SettlementRegistry
from app.settlement_plane.models import SettlementRecord
from app.settlement_plane.enums import SettlementClass
from app.settlement_plane.exceptions import InvalidSettlementObjectError

def test_settlement_registry():
    registry = SettlementRegistry()
    record = SettlementRecord(
        id="S1",
        settlement_class=SettlementClass.DISPUTE_RESOLUTION,
        owner="test",
        scope_refs=["s1"],
        release_refs=[],
        performance_refs=[]
    )
    registry.register(record)
    assert registry.get("S1") == record

    with pytest.raises(InvalidSettlementObjectError):
        registry.register(record)

    record_no_scope = SettlementRecord(
        id="S2",
        settlement_class=SettlementClass.DISPUTE_RESOLUTION,
        owner="test",
        scope_refs=[],
        release_refs=[],
        performance_refs=[]
    )
    with pytest.raises(InvalidSettlementObjectError):
        registry.register(record_no_scope)
