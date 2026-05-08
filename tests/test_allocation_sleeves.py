from app.allocation.sleeves import SleeveRegistry
from app.allocation.models import SleeveDefinition
from app.allocation.enums import SleeveClass


def test_sleeve_registry():
    registry = SleeveRegistry()
    sleeves = registry.list_all()
    assert len(sleeves) >= 2

    primary = registry.get_sleeve("primary_alpha_01")
    assert primary.sleeve_class == SleeveClass.PRIMARY_ALPHA
