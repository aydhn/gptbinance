import pytest
from datetime import datetime, timezone
from app.knowledge.models import KnowledgeItem, KnowledgeOwner
from app.knowledge.enums import KnowledgeItemType, DocumentStatus
from app.knowledge.search import KnowledgeSearchEngine
from app.knowledge.catalog import KnowledgeCatalogRegistry
import app.knowledge.search
import app.knowledge.freshness


@pytest.fixture(autouse=True)
def clean_catalog(monkeypatch):
    registry = KnowledgeCatalogRegistry()
    monkeypatch.setattr(app.knowledge.search, "catalog_registry", registry)

    # Mock freshness engine
    class MockFreshness:
        def evaluate(self, item):
            from app.knowledge.enums import FreshnessSeverity
            from app.knowledge.models import FreshnessReport

            return FreshnessReport(
                item_id=item.item_id,
                severity=FreshnessSeverity.HEALTHY,
                last_reviewed_at=datetime.now(),
                days_since_review=0,
            )

    monkeypatch.setattr(app.knowledge.search, "freshness_engine", MockFreshness())
    return registry


def test_knowledge_search(clean_catalog):
    item = KnowledgeItem(
        item_id="KI-001",
        item_type=KnowledgeItemType.SOP,
        title="Test Incident",
        description="Desc",
        owner=KnowledgeOwner(owner_id="u1", team="ops"),
        status=DocumentStatus.PUBLISHED,
        last_reviewed_at=datetime.now(timezone.utc),
    )
    clean_catalog.register(item)

    engine = KnowledgeSearchEngine()
    results = engine.search("incident")
    assert len(results) == 1
    assert results[0].score > 0
