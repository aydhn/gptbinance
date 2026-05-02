import pytest
from app.observability.suppression import SuppressionEngine
from app.observability.enums import SuppressionAction


@pytest.fixture
def engine():
    return SuppressionEngine()


def test_suppression(engine):
    rule_id = "TEST-RULE"

    assert engine.check_suppression(rule_id) == SuppressionAction.ALLOW

    engine.suppress_rule(
        rule_id, duration_minutes=60, reason="Maintenance", created_by="ops"
    )

    assert engine.check_suppression(rule_id) == SuppressionAction.SUPPRESS
    assert len(engine.get_active_suppressions()) == 1

    # Test expiration by mocking time if needed, but here we just test the logic exists
    # If we suppress for -1 minutes it should expire immediately
    engine.suppress_rule(rule_id, duration_minutes=-1, reason="Test", created_by="ops")
    assert engine.check_suppression(rule_id) == SuppressionAction.ALLOW
