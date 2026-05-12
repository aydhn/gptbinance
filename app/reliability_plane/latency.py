from typing import Optional

from .enums import SLIClass
from .models import SliDefinition


class LatencyAnalyzer:
    def __init__(self, registry):
        self._registry = registry

    def analyze(self, service_id: str) -> dict:
        slis = [
            s
            for s in self._registry.list_slis()
            if s.service_id == service_id and s.sli_class == SLIClass.LATENCY_PERCENTILE
        ]
        if not slis:
            return {"status": "unknown", "reason": "No latency SLI found"}

        return {"status": "ok", "tracked_slis": len(slis)}
