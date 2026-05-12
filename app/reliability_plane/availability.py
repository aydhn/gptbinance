from typing import Optional

from .enums import ReliabilityObjectiveClass, SLIClass
from .models import SliDefinition, SloDefinition


class AvailabilityAnalyzer:
    def __init__(self, registry):
        self._registry = registry

    def analyze(self, service_id: str) -> dict:
        slis = [
            s
            for s in self._registry.list_slis()
            if s.service_id == service_id and s.sli_class == SLIClass.SUCCESS_RATE
        ]
        if not slis:
            return {"status": "unknown", "reason": "No availability SLI found"}

        # In a real implementation, this would query observability plane for actual success rates
        return {"status": "ok", "tracked_slis": len(slis)}
