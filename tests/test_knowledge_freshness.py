import pytest
from datetime import datetime, timezone, timedelta
from app.knowledge.models import KnowledgeItem, KnowledgeOwner
from app.knowledge.enums import KnowledgeItemType, DocumentStatus, FreshnessSeverity
from app.knowledge.freshness import FreshnessEngine


def test_freshness():
    engine = FreshnessEngine(review_cadence_days=30)
    item = KnowledgeItem(
        item_id="KI-001",
        item_type=KnowledgeItemType.SOP,
        title="Test",
        description="Desc",
        owner=KnowledgeOwner(owner_id="u1", team="ops"),
        status=DocumentStatus.PUBLISHED,
        last_reviewed_at=datetime.now(timezone.utc) - timedelta(days=10),
    )

    report = engine.evaluate(item)
    assert report.severity == FreshnessSeverity.HEALTHY

    item.last_reviewed_at = datetime.now(timezone.utc) - timedelta(days=40)
    report = engine.evaluate(item)
    assert report.severity == FreshnessSeverity.STALE
