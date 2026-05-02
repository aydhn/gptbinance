from typing import Dict, Any, Optional, List
from datetime import datetime, timezone
from app.observability.models import TelemetryEvent
from app.observability.enums import ComponentType, AlertSeverity


class TelemetryIngester:
    def __init__(self):
        self._events: List[TelemetryEvent] = []

    def capture_event(
        self,
        event_type: str,
        component: ComponentType,
        details: Optional[Dict[str, Any]] = None,
        severity: AlertSeverity = AlertSeverity.INFO,
        run_id: Optional[str] = None,
    ) -> None:
        """Captures a structured telemetry event."""

        # High cardinality guard: sanitize details if needed. For now, simple dict dump.
        sanitized_details = details or {}

        event = TelemetryEvent(
            event_type=event_type,
            component=component,
            timestamp=datetime.now(timezone.utc),
            details=sanitized_details,
            severity=severity,
            run_id=run_id,
        )
        self._events.append(event)

    def get_events(self) -> List[TelemetryEvent]:
        return self._events.copy()

    def clear_events(self) -> None:
        self._events.clear()


ingester = TelemetryIngester()
