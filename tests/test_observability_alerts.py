import pytest
from app.observability.alerts import AlertEngine
from app.observability.models import AlertRule
from app.observability.enums import ComponentType, AlertSeverity, AlertState


@pytest.fixture
def engine():
    return AlertEngine()


def test_alert_rule_evaluation(engine):
    rule = AlertRule(
        rule_id="RULE-001",
        name="High Reject Rate",
        component=ComponentType.EXECUTION,
        severity=AlertSeverity.ERROR,
        condition_type="threshold",
        threshold_value=5.0,
        description="Too many rejected orders",
    )
    engine.register_rule(rule)

    # Should not trigger
    engine.evaluate_condition("RULE-001", current_value=2.0)
    assert len(engine.get_active_alerts()) == 0

    # Should trigger
    engine.evaluate_condition("RULE-001", current_value=10.0, evidence={"rejects": 10})
    alerts = engine.get_active_alerts()
    assert len(alerts) == 1
    assert alerts[0].rule_id == "RULE-001"
    assert alerts[0].state == AlertState.OPEN
    assert alerts[0].occurrence_count == 1
    assert alerts[0].evidence["rejects"] == 10

    # Trigger again, should increment count
    engine.evaluate_condition("RULE-001", current_value=12.0)
    alerts = engine.get_active_alerts()
    assert len(alerts) == 1
    assert alerts[0].occurrence_count == 2

    # Below threshold, should clear
    engine.evaluate_condition("RULE-001", current_value=1.0)
    assert len(engine.get_active_alerts()) == 0

    # History should contain the event
    history = engine.get_alert_history()
    assert len(history) == 1
    assert history[0].state == AlertState.CLEARED
