from app.supply_chain_plane.models import ComponentDefinition
from app.supply_chain_plane.registry import CanonicalComponentRegistry


class ComponentManager:
    def __init__(self, registry: CanonicalComponentRegistry):
        self.registry = registry

    def create_component(self, component: ComponentDefinition) -> None:
        self.registry.register_component(component)

    def get_component(self, component_id: str) -> ComponentDefinition:
        comp = self.registry.get_component(component_id)
        if not comp:
            raise ValueError(f"Component not found: {component_id}")
        return comp
