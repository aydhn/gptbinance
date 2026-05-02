from typing import Dict, List, Optional
from datetime import datetime, timezone, timedelta
from app.observability.models import TelemetryDigest, AlertEvent, SloEvaluation
from app.observability.enums import DigestScope


class DigestBuilder:
    def build_digest(
        self, scope: DigestScope, alerts: List[AlertEvent], slos: List[SloEvaluation]
    ) -> TelemetryDigest:
        now = datetime.now(timezone.utc)

        if scope == DigestScope.SESSION:
            start_time = now - timedelta(hours=1)  # Mock session duration
        elif scope == DigestScope.DAILY:
            start_time = now - timedelta(days=1)
        else:
            start_time = now - timedelta(days=7)

        recent_alerts = [a for a in alerts if a.last_seen >= start_time]
        # Sort by severity and occurrence
        recent_alerts.sort(
            key=lambda a: (a.severity.value, -a.occurrence_count), reverse=True
        )
        top_alerts = [a.alert_id for a in recent_alerts[:5]]

        health_highlights = (
            f"Generated {len(recent_alerts)} alerts in the last {scope.value}."
        )

        breached_slos = [s for s in slos if s.status.value == "breach"]
        slo_summary = f"{len(breached_slos)} SLO breaches out of {len(slos)} evaluated."

        return TelemetryDigest(
            scope=scope,
            start_time=start_time,
            end_time=now,
            top_alerts=top_alerts,
            health_highlights=health_highlights,
            slo_summary=slo_summary,
        )


builder = DigestBuilder()
