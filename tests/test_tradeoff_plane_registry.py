import pytest
from app.tradeoff_plane.models import TradeoffObject, ObjectiveSetRecord
from app.tradeoff_plane.enums import TradeoffClass
from app.tradeoff_plane.registry import TradeoffRegistry
from app.tradeoff_plane.exceptions import InvalidTradeoffObjectError
from datetime import datetime

def test_tradeoff_registry_register_and_get():
    registry = TradeoffRegistry()
    obj_set = ObjectiveSetRecord(set_id="os1", objectives=[])

    obj = TradeoffObject(
        tradeoff_id="release_speed_vs_safety_tradeoff",
        tradeoff_class=TradeoffClass.AUTHORITATIVE,
        owner="release_team",
        scope="global",
        objective_set=obj_set,
        burden_posture=[]
    )

    registry.register(obj)
    retrieved = registry.get("release_speed_vs_safety_tradeoff")

    assert retrieved is not None
    assert retrieved.owner == "release_team"
    assert retrieved.tradeoff_class == TradeoffClass.AUTHORITATIVE

def test_tradeoff_registry_missing_id():
    registry = TradeoffRegistry()
    obj_set = ObjectiveSetRecord(set_id="os1", objectives=[])

    obj = TradeoffObject(
        tradeoff_id="",
        tradeoff_class=TradeoffClass.LOCAL,
        owner="team_a",
        scope="local",
        objective_set=obj_set,
        burden_posture=[]
    )

    with pytest.raises(InvalidTradeoffObjectError):
        registry.register(obj)
