import pytest
from app.observability.telemetry import TelemetryIngester
from app.observability.enums import ComponentType, AlertSeverity


@pytest.fixture
def ingester():
    return TelemetryIngester()


def test_telemetry_capture(ingester):
    ingester.capture_event(
        event_type="test_event",
        component=ComponentType.EXECUTION,
        details={"order_id": "123"},
        severity=AlertSeverity.WARNING,
    )

    events = ingester.get_events()
    assert len(events) == 1
    assert events[0].event_type == "test_event"
    assert events[0].component == ComponentType.EXECUTION
    assert events[0].details["order_id"] == "123"
    assert events[0].severity == AlertSeverity.WARNING
