import pytest
import sqlite3
import os
from datetime import datetime, timezone
from app.observability.storage import ObservabilityStorage
from app.observability.models import (
    ObservabilityConfig,
    MetricSample,
    AlertEvent,
    TelemetryEvent,
)
from app.observability.enums import ComponentType, AlertSeverity, AlertState


@pytest.fixture
def storage(tmp_path):
    config = ObservabilityConfig(storage_path=str(tmp_path), enabled=True)
    return ObservabilityStorage(config)


def test_save_metric_sample(storage):
    sample = MetricSample(metric_name="test_metric", value=1.5, tags={"env": "test"})
    storage.save_metric_sample(sample)

    with sqlite3.connect(storage.db_path) as conn:
        cursor = conn.execute("SELECT metric_name, value FROM metric_samples")
        row = cursor.fetchone()
        assert row[0] == "test_metric"
        assert row[1] == 1.5


def test_upsert_alert(storage):
    now = datetime.now(timezone.utc)
    alert = AlertEvent(
        alert_id="A1",
        rule_id="R1",
        component=ComponentType.SYSTEM,
        severity=AlertSeverity.INFO,
        state=AlertState.OPEN,
        first_seen=now,
        last_seen=now,
        occurrence_count=1,
    )
    storage.upsert_alert(alert)

    alert.occurrence_count = 2
    storage.upsert_alert(alert)

    with sqlite3.connect(storage.db_path) as conn:
        cursor = conn.execute(
            "SELECT occurrence_count FROM active_alerts WHERE alert_id='A1'"
        )
        row = cursor.fetchone()
        assert row[0] == 2
