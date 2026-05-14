import pytest
from app.value_plane.models import ValueObject, ValueObjectiveRef
from app.value_plane.registry import value_registry
from app.value_plane.enums import ValueClass
from app.value_plane.exceptions import InvalidValueObject

def test_value_registry_registration():
    vo = ValueObject(
        value_id="val_1",
        value_class=ValueClass.STRATEGY_VALUE,
        owner="strategy_team",
        scope="global",
        target_horizon="long_term",
        state="active",
        objective_ref=ValueObjectiveRef(objective_id="obj_1")
    )
    value_registry.register(vo)
    assert value_registry.get("val_1") is not None

def test_invalid_value_object():
    with pytest.raises(InvalidValueObject):
        vo = ValueObject(
            value_id="",
            value_class=ValueClass.STRATEGY_VALUE,
            owner="strategy_team",
            scope="global",
            target_horizon="long_term",
            state="active",
            objective_ref=ValueObjectiveRef(objective_id="obj_1")
        )
        value_registry.register(vo)
