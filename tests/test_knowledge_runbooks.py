import pytest
from datetime import datetime, timezone
from app.knowledge.models import Runbook, KnowledgeOwner
from app.knowledge.enums import DocumentStatus
from app.knowledge.runbooks import RunbookRegistry
from app.knowledge.catalog import KnowledgeCatalogRegistry
import app.knowledge.runbooks


# Patch catalog_registry for tests
@pytest.fixture(autouse=True)
def clean_catalog(monkeypatch):
    registry = KnowledgeCatalogRegistry()
    monkeypatch.setattr(app.knowledge.runbooks, "catalog_registry", registry)
    return registry


def test_runbook_registration():
    r_reg = RunbookRegistry()
    rb = Runbook(
        item_id="RB-001",
        title="Test RB",
        description="Desc",
        owner=KnowledgeOwner(owner_id="u1", team="ops"),
        status=DocumentStatus.PUBLISHED,
        last_reviewed_at=datetime.now(timezone.utc),
        investigation_steps=["Check logs"],
    )
    r_reg.register(rb)
    assert r_reg.get_runbook("RB-001") == rb
    assert len(r_reg.list_runbooks()) == 1
