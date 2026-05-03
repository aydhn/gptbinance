from typing import List, Optional
from app.knowledge.storage import KnowledgeStorage
from app.knowledge.models import (
    KnowledgeItem,
    Runbook,
    SopDocument,
    Playbook,
    LessonLearned,
    QuizResult,
    OperatorReadinessRecord,
)
from app.knowledge.enums import KnowledgeItemType
from app.knowledge.catalog import catalog_registry


class KnowledgeRepository:
    def __init__(self, storage: KnowledgeStorage):
        self.storage = storage

    def load_catalog(self):
        items = self.storage.get_items()
        for data in items:
            t = data.get("item_type")
            if t == KnowledgeItemType.RUNBOOK.value:
                catalog_registry.register(Runbook(**data))
            elif t == KnowledgeItemType.SOP.value:
                catalog_registry.register(SopDocument(**data))
            elif t == KnowledgeItemType.PLAYBOOK.value:
                catalog_registry.register(Playbook(**data))
            elif t == KnowledgeItemType.LESSON_LEARNED.value:
                catalog_registry.register(LessonLearned(**data))
            else:
                catalog_registry.register(KnowledgeItem(**data))

    def save_item(self, item: KnowledgeItem):
        self.storage.save_item(item)
        catalog_registry.register(item)


storage = KnowledgeStorage()
knowledge_repo = KnowledgeRepository(storage)
