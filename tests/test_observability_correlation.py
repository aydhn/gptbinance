import pytest
from app.observability.correlation import AlertCorrelator
from app.observability.models import AlertEvent
from app.observability.enums import (
    ComponentType,
    AlertSeverity,
    AlertState,
    CorrelationVerdict,
)
from datetime import datetime, timezone


@pytest.fixture
def correlator():
    return AlertCorrelator()


def test_alert_correlation(correlator):
    now = datetime.now(timezone.utc)
    alerts = [
        AlertEvent(
            alert_id="A1",
            rule_id="R1",
            component=ComponentType.EXECUTION,
            severity=AlertSeverity.ERROR,
            state=AlertState.OPEN,
            first_seen=now,
            last_seen=now,
            occurrence_count=10,
        ),
        AlertEvent(
            alert_id="A2",
            rule_id="R2",
            component=ComponentType.EXECUTION,
            severity=AlertSeverity.INFO,
            state=AlertState.OPEN,
            first_seen=now,
            last_seen=now,
            occurrence_count=1,
        ),
        AlertEvent(
            alert_id="A3",
            rule_id="R3",
            component=ComponentType.DATA_STREAM,
            severity=AlertSeverity.ERROR,
            state=AlertState.OPEN,
            first_seen=now,
            last_seen=now,
            occurrence_count=5,
        ),
    ]

    groups = correlator.correlate(alerts)

    # Should group A1 and A2 together since they are both EXECUTION
    assert len(groups) == 1
    assert groups[0].verdict == CorrelationVerdict.RELATED
    assert groups[0].primary_alert_id == "A1"  # Higher occurrence/severity
    assert "A2" in groups[0].related_alert_ids
    assert groups[0].likely_parent_issue == "Multiple issues on execution"
