from typing import List, Optional
from app.semantic_plane.models import MetricRecord

class MetricManager:
    def __init__(self, registry):
        self.registry = registry

    def register_metric(self, metric: MetricRecord):
        self.registry.register_metric(metric)

    def get_metrics_without_measure_basis(self) -> List[MetricRecord]:
        return [m for m in self.registry.metrics.values() if m.measure_definition is None]
