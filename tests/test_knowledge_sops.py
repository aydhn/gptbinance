import pytest
from datetime import datetime, timezone
from app.knowledge.models import SopDocument, KnowledgeOwner
from app.knowledge.enums import DocumentStatus
from app.knowledge.sops import SopRegistry
from app.knowledge.catalog import KnowledgeCatalogRegistry
import app.knowledge.sops


@pytest.fixture(autouse=True)
def clean_catalog(monkeypatch):
    registry = KnowledgeCatalogRegistry()
    monkeypatch.setattr(app.knowledge.sops, "catalog_registry", registry)
    return registry


def test_sop_registration():
    s_reg = SopRegistry()
    sop = SopDocument(
        item_id="SOP-001",
        title="Test SOP",
        description="Desc",
        owner=KnowledgeOwner(owner_id="u1", team="ops"),
        status=DocumentStatus.PUBLISHED,
        last_reviewed_at=datetime.now(timezone.utc),
        steps=["Step 1"],
    )
    s_reg.register(sop)
    assert s_reg.get_sop("SOP-001") == sop
    assert len(s_reg.list_sops()) == 1
