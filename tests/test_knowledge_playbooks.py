import pytest
from datetime import datetime, timezone
from app.knowledge.models import Playbook, KnowledgeOwner
from app.knowledge.enums import DocumentStatus
from app.knowledge.playbooks import PlaybookRegistry
from app.knowledge.catalog import KnowledgeCatalogRegistry
import app.knowledge.playbooks


@pytest.fixture(autouse=True)
def clean_catalog(monkeypatch):
    registry = KnowledgeCatalogRegistry()
    monkeypatch.setattr(app.knowledge.playbooks, "catalog_registry", registry)
    return registry


def test_playbook_registration():
    p_reg = PlaybookRegistry()
    pb = Playbook(
        item_id="PB-001",
        title="Test PB",
        description="Desc",
        owner=KnowledgeOwner(owner_id="u1", team="ops"),
        status=DocumentStatus.PUBLISHED,
        last_reviewed_at=datetime.now(timezone.utc),
        trigger_conditions=["Alert X"],
    )
    p_reg.register(pb)
    assert p_reg.get_playbook("PB-001") == pb
    assert len(p_reg.list_playbooks()) == 1
