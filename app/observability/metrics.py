from typing import Dict, List, Optional
from app.observability.models import MetricDefinition, MetricSample
from app.observability.exceptions import InvalidMetricDefinition
from app.observability.enums import MetricType, MetricUnit, ComponentType
from datetime import datetime, timezone


class MetricRegistry:
    def __init__(self):
        self._definitions: Dict[str, MetricDefinition] = {}
        self._samples: List[MetricSample] = []

    def register(self, definition: MetricDefinition) -> None:
        if definition.name in self._definitions:
            raise InvalidMetricDefinition(
                f"Metric {definition.name} already registered"
            )
        self._definitions[definition.name] = definition

    def get_definition(self, name: str) -> Optional[MetricDefinition]:
        return self._definitions.get(name)

    def list_definitions(self) -> List[MetricDefinition]:
        return list(self._definitions.values())

    def record(
        self,
        name: str,
        value: float,
        tags: Optional[Dict[str, str]] = None,
        run_id: Optional[str] = None,
    ) -> None:
        if name not in self._definitions:
            raise InvalidMetricDefinition(f"Metric {name} not registered")

        sample = MetricSample(
            metric_name=name,
            value=value,
            timestamp=datetime.now(timezone.utc),
            tags=tags or {},
            run_id=run_id,
        )
        self._samples.append(sample)

    def get_samples(self, name: Optional[str] = None) -> List[MetricSample]:
        if name:
            return [s for s in self._samples if s.metric_name == name]
        return self._samples.copy()

    def clear_samples(self) -> None:
        self._samples.clear()


registry = MetricRegistry()
