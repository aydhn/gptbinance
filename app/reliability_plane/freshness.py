from typing import Optional

from .enums import SLIClass
from .models import SliDefinition


class FreshnessAnalyzer:
    def __init__(self, registry):
        self._registry = registry

    def analyze(self, service_id: str) -> dict:
        slis = [
            s
            for s in self._registry.list_slis()
            if s.service_id == service_id and s.sli_class == SLIClass.FRESHNESS_LAG
        ]
        if not slis:
            return {"status": "unknown", "reason": "No freshness SLI found"}

        return {"status": "ok", "tracked_slis": len(slis)}
