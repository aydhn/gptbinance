import json
from typing import Dict, Any
from app.observability.models import (
    SystemHealthSnapshot,
    ObservabilitySummary,
    TelemetryDigest,
)
from app.observability.enums import ComponentType


class ObservabilityReporter:
    @staticmethod
    def format_system_health(snapshot: SystemHealthSnapshot) -> str:
        report = {
            "severity": snapshot.severity.value,
            "timestamp": snapshot.timestamp.isoformat(),
            "summary": snapshot.summary,
            "components": {},
        }
        for comp, comp_snap in snapshot.components.items():
            report["components"][comp.value] = {
                "severity": comp_snap.severity.value,
                "explanation": comp_snap.explanation,
            }
        return json.dumps(report, indent=2)

    @staticmethod
    def format_metrics_summary(metrics: list) -> str:
        # Simplified placeholder
        return json.dumps({"status": "OK", "count": len(metrics)}, indent=2)

    @staticmethod
    def format_alerts_summary(alerts: list) -> str:
        res = []
        for a in alerts:
            res.append(
                {
                    "alert_id": a.alert_id,
                    "severity": a.severity.value,
                    "component": a.component.value,
                    "state": a.state.value,
                    "occurrences": a.occurrence_count,
                }
            )
        return json.dumps(res, indent=2)

    @staticmethod
    def format_digest(digest: TelemetryDigest) -> str:
        return json.dumps(
            digest.dict(exclude={"start_time", "end_time", "generated_at"}),
            indent=2,
            default=str,
        )
