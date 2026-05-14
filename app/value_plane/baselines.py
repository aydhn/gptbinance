from typing import Dict, List, Optional
from app.value_plane.models import BaselineRecord
from app.value_plane.exceptions import InvalidBaselineOrCounterfactual

class BaselineRegistry:
    def __init__(self):
        self._baselines: Dict[str, BaselineRecord] = {}

    def register(self, baseline: BaselineRecord):
        if not baseline.description:
            raise InvalidBaselineOrCounterfactual("Baseline must have a description")
        self._baselines[baseline.baseline_id] = baseline

    def get(self, baseline_id: str) -> Optional[BaselineRecord]:
        return self._baselines.get(baseline_id)

    def list_all(self) -> List[BaselineRecord]:
        return list(self._baselines.values())

baseline_registry = BaselineRegistry()
