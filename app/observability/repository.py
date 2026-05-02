from typing import List, Optional
from app.observability.storage import ObservabilityStorage
from app.observability.models import MetricSample, AlertEvent, TelemetryEvent


class ObservabilityRepository:
    def __init__(self, storage: ObservabilityStorage):
        self.storage = storage

    def save_sample(self, sample: MetricSample) -> None:
        self.storage.save_metric_sample(sample)

    def save_event(self, event: TelemetryEvent) -> None:
        self.storage.save_telemetry_event(event)

    def save_alert(self, alert: AlertEvent) -> None:
        self.storage.upsert_alert(alert)

    # Simplified querying for reporting
    def get_recent_metrics(self) -> List[MetricSample]:
        # In a real impl, fetch from sqlite
        return []

    def get_active_alerts(self) -> List[AlertEvent]:
        # In a real impl, fetch from sqlite
        return []
