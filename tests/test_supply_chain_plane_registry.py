import pytest
from app.supply_chain_plane.models import ComponentDefinition, ComponentRef
from app.supply_chain_plane.enums import ComponentClass
from app.supply_chain_plane.registry import CanonicalComponentRegistry
from app.supply_chain_plane.exceptions import InvalidComponentDefinition


def test_registry_valid_component():
    registry = CanonicalComponentRegistry()
    comp = ComponentDefinition(
        component_id="comp-1",
        name="Test Component",
        component_class=ComponentClass.SOURCE_COMPONENT,
        owner="team-alpha",
        criticality="high",
        supported_environments=["dev", "prod"],
        lifecycle_state="active",
    )
    registry.register_component(comp)
    assert registry.get_component("comp-1") == comp


def test_registry_invalid_component():
    registry = CanonicalComponentRegistry()
    with pytest.raises(InvalidComponentDefinition):
        registry.register_component(
            ComponentDefinition(
                component_id="",
                name="Test",
                component_class=ComponentClass.SOURCE_COMPONENT,
                owner="a",
                criticality="low",
                supported_environments=[],
                lifecycle_state="active",
            )
        )
