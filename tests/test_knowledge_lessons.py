import pytest
from datetime import datetime, timezone
from app.knowledge.models import LessonLearned, KnowledgeOwner
from app.knowledge.enums import DocumentStatus, LessonStatus
from app.knowledge.lessons import LessonRegistry
from app.knowledge.catalog import KnowledgeCatalogRegistry
import app.knowledge.lessons


@pytest.fixture(autouse=True)
def clean_catalog(monkeypatch):
    registry = KnowledgeCatalogRegistry()
    monkeypatch.setattr(app.knowledge.lessons, "catalog_registry", registry)
    return registry


def test_lesson_lifecycle():
    l_reg = LessonRegistry()
    lesson = LessonLearned(
        item_id="LL-001",
        title="Test Lesson",
        description="Desc",
        owner=KnowledgeOwner(owner_id="u1", team="ops"),
        status=DocumentStatus.PUBLISHED,
        last_reviewed_at=datetime.now(timezone.utc),
        lesson_status=LessonStatus.DRAFT,
    )
    l_reg.register(lesson)

    # Needs evidence to adopt
    assert not l_reg.transition_lesson("LL-001", LessonStatus.ADOPTED)

    lesson.source_incident_ref = "INC-123"
    assert l_reg.transition_lesson("LL-001", LessonStatus.ADOPTED)

    adopted = l_reg.get_lesson("LL-001")
    assert adopted.lesson_status == LessonStatus.ADOPTED
