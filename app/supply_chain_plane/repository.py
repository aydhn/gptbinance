from typing import List, Optional, Dict
from app.supply_chain_plane.models import ComponentDefinition, ComponentRef
from app.supply_chain_plane.storage import SupplyChainStorage


class SupplyChainRepository:
    def __init__(self, storage: SupplyChainStorage):
        self.storage = storage

    def save_component(self, component: ComponentDefinition) -> None:
        self.storage.save("components", component.component_id, component)

    def get_component(self, component_id: str) -> Optional[Dict]:
        return self.storage.load("components", component_id)
