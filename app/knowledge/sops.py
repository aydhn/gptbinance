from typing import List, Optional
from app.knowledge.models import SopDocument
from app.knowledge.catalog import catalog_registry
from app.knowledge.enums import KnowledgeItemType


class SopRegistry:
    def register(self, sop: SopDocument) -> None:
        catalog_registry.register(sop)

    def get_sop(self, item_id: str) -> Optional[SopDocument]:
        item = catalog_registry.get(item_id)
        if item and item.item_type == KnowledgeItemType.SOP:
            return item  # type: ignore
        return None

    def list_sops(self) -> List[SopDocument]:
        return [item for item in catalog_registry.list_by_type(KnowledgeItemType.SOP)]  # type: ignore


sop_registry = SopRegistry()
