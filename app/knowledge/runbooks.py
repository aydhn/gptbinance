from typing import List, Optional
from app.knowledge.models import Runbook
from app.knowledge.catalog import catalog_registry
from app.knowledge.enums import KnowledgeItemType


class RunbookRegistry:
    def register(self, runbook: Runbook) -> None:
        catalog_registry.register(runbook)

    def get_runbook(self, item_id: str) -> Optional[Runbook]:
        item = catalog_registry.get(item_id)
        if item and item.item_type == KnowledgeItemType.RUNBOOK:
            return item  # type: ignore
        return None

    def list_runbooks(self) -> List[Runbook]:
        return [item for item in catalog_registry.list_by_type(KnowledgeItemType.RUNBOOK)]  # type: ignore


runbook_registry = RunbookRegistry()
