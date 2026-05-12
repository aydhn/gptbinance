from typing import Any, Dict

from .enums import BudgetClass
from .models import ErrorBudgetPolicy, SliDefinition, SloDefinition


class QualityAnalyzer:
    def __init__(self, registry, budgets):
        self._registry = registry
        self._budgets = budgets

    def analyze_service_quality(self, service_id: str) -> Dict[str, Any]:
        warnings = []
        penalties = 0

        slis = [s for s in self._registry.list_slis() if s.service_id == service_id]
        if not slis:
            warnings.append("No SLIs defined for service")
            penalties += 10

        for sli in slis:
            if not sli.telemetry_support_refs:
                warnings.append(f"Unsupported SLI: {sli.sli_id}")
                penalties += 5

        # More checks...

        return {
            "warnings": warnings,
            "penalties": penalties,
            "quality_score": max(0, 100 - penalties),
        }
