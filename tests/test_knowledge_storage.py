import pytest
import os
from datetime import datetime, timezone
from app.knowledge.models import KnowledgeItem, KnowledgeOwner
from app.knowledge.enums import KnowledgeItemType, DocumentStatus
from app.knowledge.storage import KnowledgeStorage


def test_storage():
    storage = KnowledgeStorage(db_path=":memory:")
    item = KnowledgeItem(
        item_id="KI-001",
        item_type=KnowledgeItemType.SOP,
        title="Test",
        description="Desc",
        owner=KnowledgeOwner(owner_id="u1", team="ops"),
        status=DocumentStatus.PUBLISHED,
        last_reviewed_at=datetime.now(timezone.utc),
    )
    storage.save_item(item)
    items = storage.get_items()
    assert len(items) == 1
    assert items[0]["item_id"] == "KI-001"
