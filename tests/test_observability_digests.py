import pytest
from app.observability.digests import DigestBuilder
from app.observability.models import AlertEvent, SloEvaluation
from app.observability.enums import (
    DigestScope,
    ComponentType,
    AlertSeverity,
    AlertState,
    SloStatus,
)
from datetime import datetime, timezone, timedelta


@pytest.fixture
def builder():
    return DigestBuilder()


def test_digest_building(builder):
    now = datetime.now(timezone.utc)
    alerts = [
        AlertEvent(
            alert_id="A1",
            rule_id="R1",
            component=ComponentType.DATA_STREAM,
            severity=AlertSeverity.CRITICAL,
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
    ]

    slos = [
        SloEvaluation(
            slo_id="SLO-1",
            status=SloStatus.BREACH,
            current_sli_value=85.0,
            timestamp=now,
            explanation="Failed",
        )
    ]

    digest = builder.build_digest(DigestScope.DAILY, alerts, slos)

    assert digest.scope == DigestScope.DAILY
    assert "A1" in digest.top_alerts
    assert "A2" in digest.top_alerts
    assert "1 SLO breaches" in digest.slo_summary
