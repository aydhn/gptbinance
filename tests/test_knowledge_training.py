import pytest
from app.knowledge.models import TrainingModule
from app.knowledge.enums import KnowledgeScope
from app.knowledge.training import TrainingRegistry


def test_training_registry():
    t_reg = TrainingRegistry()
    tm = TrainingModule(
        module_id="MOD-001",
        title="Base Ops",
        description="Desc",
        scope=KnowledgeScope.GLOBAL,
    )
    t_reg.register(tm)
    assert t_reg.get_module("MOD-001") == tm
