from typing import List, Optional
from app.knowledge.models import Playbook
from app.knowledge.catalog import catalog_registry
from app.knowledge.enums import KnowledgeItemType


class PlaybookRegistry:
    def register(self, playbook: Playbook) -> None:
        catalog_registry.register(playbook)

    def get_playbook(self, item_id: str) -> Optional[Playbook]:
        item = catalog_registry.get(item_id)
        if item and item.item_type == KnowledgeItemType.PLAYBOOK:
            return item  # type: ignore
        return None

    def list_playbooks(self) -> List[Playbook]:
        return [item for item in catalog_registry.list_by_type(KnowledgeItemType.PLAYBOOK)]  # type: ignore


playbook_registry = PlaybookRegistry()
