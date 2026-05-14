from typing import Dict, Optional, List
from app.supply_chain_plane.models import ComponentDefinition, ComponentRef
from app.supply_chain_plane.base import ComponentRegistryBase
from app.supply_chain_plane.exceptions import InvalidComponentDefinition


class CanonicalComponentRegistry(ComponentRegistryBase):
    def __init__(self):
        self._components: Dict[str, ComponentDefinition] = {}

    def register_component(self, component: ComponentDefinition) -> None:
        if not component.component_id:
            raise InvalidComponentDefinition("Component ID cannot be empty.")
        if not component.name:
            raise InvalidComponentDefinition("Component name cannot be empty.")
        self._components[component.component_id] = component

    def get_component(self, component_id: str) -> Optional[ComponentDefinition]:
        return self._components.get(component_id)

    def list_components(self) -> List[ComponentDefinition]:
        return list(self._components.values())
