from typing import Dict, List, Optional
from .exceptions import ObservabilityPlaneError

class AggregationRulesRegistry:
    def __init__(self):
        self._rules: Dict[str, str] = {}

    def register_aggregation(self, telemetry_id: str, aggregation_type: str) -> None:
        if aggregation_type not in ["SUM", "AVG", "MAX", "MIN", "P99"]:
            raise ObservabilityPlaneError(f"Opaque rollup logic detected for {telemetry_id}.")
        self._rules[telemetry_id] = aggregation_type

    def get_aggregation(self, telemetry_id: str) -> Optional[str]:
        return self._rules.get(telemetry_id)

    def list_aggregations(self) -> Dict[str, str]:
        return self._rules.copy()
