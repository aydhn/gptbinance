import pytest
from app.value_plane.models import ValueObjective
from app.value_plane.objectives import objective_registry
from app.value_plane.enums import ObjectiveClass
from app.value_plane.exceptions import InvalidObjectiveDefinition

def test_objective_registration():
    obj = ValueObjective(
        objective_id="obj_1",
        objective_class=ObjectiveClass.GROWTH,
        description="Increase revenue",
        measurable_success_criteria="> 10% YoY"
    )
    objective_registry.register(obj)
    assert objective_registry.get("obj_1") is not None

def test_invalid_objective_registration():
    with pytest.raises(InvalidObjectiveDefinition):
        obj = ValueObjective(
            objective_id="obj_1",
            objective_class=ObjectiveClass.GROWTH,
            description="Increase revenue",
            measurable_success_criteria=""
        )
        objective_registry.register(obj)
