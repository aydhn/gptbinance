from typing import Dict, List, Optional
from app.knowledge.base import KnowledgeRegistryBase
from app.knowledge.models import KnowledgeItem, KnowledgeCatalogEntry
from app.knowledge.enums import KnowledgeItemType, DocumentStatus, FreshnessSeverity


class KnowledgeCatalogRegistry(KnowledgeRegistryBase):
    def __init__(self):
        self._items: Dict[str, KnowledgeItem] = {}
        self._items_by_type: Dict[KnowledgeItemType, List[str]] = {
            t: [] for t in KnowledgeItemType
        }

    def register(self, item: KnowledgeItem) -> None:
        self._items[item.item_id] = item
        if item.item_id not in self._items_by_type[item.item_type]:
            self._items_by_type[item.item_type].append(item.item_id)

    def get(self, item_id: str) -> Optional[KnowledgeItem]:
        return self._items.get(item_id)

    def list_all(self) -> List[KnowledgeItem]:
        return list(self._items.values())

    def list_by_type(self, item_type: KnowledgeItemType) -> List[KnowledgeItem]:
        return [self._items[i_id] for i_id in self._items_by_type[item_type]]

    def get_catalog_summary(self) -> List[KnowledgeCatalogEntry]:
        summary = []
        for item in self._items.values():
            summary.append(
                KnowledgeCatalogEntry(
                    item_id=item.item_id,
                    item_type=item.item_type,
                    status=item.status,
                    freshness_severity=FreshnessSeverity.HEALTHY,  # Will be enriched by freshness engine
                    title=item.title,
                )
            )
        return summary


catalog_registry = KnowledgeCatalogRegistry()
