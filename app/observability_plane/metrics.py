from typing import Dict, List, Optional
from .models import MetricDefinition
from .exceptions import InvalidTelemetryDefinitionError

class MetricRegistry:
    def __init__(self):
        self._metrics: Dict[str, MetricDefinition] = {}

    def register_metric(self, metric: MetricDefinition) -> None:
        if not metric.unit:
            raise InvalidTelemetryDefinitionError("Metric must specify a unit.")
        self._metrics[metric.telemetry_id] = metric

    def get_metric(self, telemetry_id: str) -> Optional[MetricDefinition]:
        return self._metrics.get(telemetry_id)

    def list_metrics(self) -> List[MetricDefinition]:
        return list(self._metrics.values())
