import pytest
from app.governance.triggers import TriggerEvaluator
from app.governance.enums import RefreshTriggerType
from datetime import datetime, timezone, timedelta


def test_time_based_trigger():
    evaluator = TriggerEvaluator()
    assert evaluator.evaluate_time_based(None, 24) == True

    recent = datetime.now(timezone.utc) - timedelta(hours=1)
    assert evaluator.evaluate_time_based(recent, 24) == False

    old = datetime.now(timezone.utc) - timedelta(hours=25)
    assert evaluator.evaluate_time_based(old, 24) == True


def test_create_trigger():
    evaluator = TriggerEvaluator()
    t = evaluator.create_trigger(RefreshTriggerType.MANUAL, "test")
    assert t.trigger_type == RefreshTriggerType.MANUAL
    assert t.source == "test"
