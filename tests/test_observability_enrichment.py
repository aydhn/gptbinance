import pytest
from app.observability.enrichment import IncidentEnricher
from app.observability.models import AlertEvent
from app.observability.enums import ComponentType, AlertSeverity, AlertState
from datetime import datetime, timezone


@pytest.fixture
def enricher():
    return IncidentEnricher()


def test_incident_enrichment(enricher):
    now = datetime.now(timezone.utc)
    alert = AlertEvent(
        alert_id="A1",
        rule_id="R1",
        component=ComponentType.DATA_STREAM,
        severity=AlertSeverity.ERROR,
        state=AlertState.OPEN,
        first_seen=now,
        last_seen=now,
        occurrence_count=1,
        evidence={"lag": 5000},
    )

    hint = enricher.enrich_alert(alert)
    assert hint.alert_id == "A1"
    assert hint.suggested_runbook is not None
    assert hint.suggested_runbook.ref_id == "RB-STREAM-001"
    assert "lag" in hint.context
