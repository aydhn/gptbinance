from typing import Dict
from datetime import datetime, timezone
from app.experiments.models import BaselineReference
from app.experiments.exceptions import MissingBaselineError


class BaselineRegistry:
    def __init__(self):
        self._baselines: Dict[str, BaselineReference] = {}

    def register(self, baseline: BaselineReference) -> str:
        self._baselines[baseline.baseline_id] = baseline
        return baseline.baseline_id

    def get(self, baseline_id: str) -> BaselineReference:
        if baseline_id not in self._baselines:
            raise MissingBaselineError(f"Baseline {baseline_id} not found")
        return self._baselines[baseline_id]

    def check_freshness(self, baseline_id: str, max_age_days: int = 30) -> bool:
        baseline = self.get(baseline_id)
        age = (datetime.now(timezone.utc) - baseline.frozen_at).days
        return age <= max_age_days
