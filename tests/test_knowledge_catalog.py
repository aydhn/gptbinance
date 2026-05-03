import pytest
from datetime import datetime, timezone
from app.knowledge.models import KnowledgeItem, KnowledgeOwner
from app.knowledge.enums import KnowledgeItemType, DocumentStatus
from app.knowledge.catalog import KnowledgeCatalogRegistry


def test_catalog_registration():
    registry = KnowledgeCatalogRegistry()
    item = KnowledgeItem(
        item_id="KI-001",
        item_type=KnowledgeItemType.SOP,
        title="Test",
        description="Desc",
        owner=KnowledgeOwner(owner_id="u1", team="ops"),
        status=DocumentStatus.PUBLISHED,
        last_reviewed_at=datetime.now(timezone.utc),
    )
    registry.register(item)
    assert registry.get("KI-001") == item
    assert len(registry.list_all()) == 1
    assert len(registry.list_by_type(KnowledgeItemType.SOP)) == 1
