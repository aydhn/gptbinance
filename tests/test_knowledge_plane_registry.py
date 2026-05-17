import pytest
from app.knowledge_plane.registry import CanonicalKnowledgeRegistry
from app.knowledge_plane.models import KnowledgeObject
from app.knowledge_plane.exceptions import InvalidKnowledgeObject

def test_registry_registration():
    registry = CanonicalKnowledgeRegistry()
    obj = KnowledgeObject(knowledge_id="runbook-123", owner="team-a", knowledge_class="runbook", authoritative=True, scope=["live"])
    registry.register(obj)

    assert registry.get("runbook-123") is not None
    assert registry.get("runbook-123").owner == "team-a"

def test_registry_invalid_registration():
    registry = CanonicalKnowledgeRegistry()
    with pytest.raises(InvalidKnowledgeObject):
        obj = KnowledgeObject(knowledge_id="", owner="team-a", knowledge_class="runbook", authoritative=True, scope=[])
        registry.register(obj)
