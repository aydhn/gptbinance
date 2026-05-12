from typing import Dict, List, Optional
from .models import TelemetryNormalizationRecord
from .exceptions import ObservabilityPlaneError

class NormalizationRegistry:
    def __init__(self):
        self._rules: Dict[str, TelemetryNormalizationRecord] = {}

    def register_normalization(self, record: TelemetryNormalizationRecord) -> None:
        if record.semantic_rewrite:
            raise ObservabilityPlaneError("Hidden semantic rewrite during normalization is prohibited.")
        self._rules[record.normalization_id] = record

    def get_normalization(self, normalization_id: str) -> Optional[TelemetryNormalizationRecord]:
        return self._rules.get(normalization_id)

    def list_normalization(self) -> List[TelemetryNormalizationRecord]:
        return list(self._rules.values())
