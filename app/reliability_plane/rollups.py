from datetime import datetime
from typing import Dict, List, Optional

from .models import ReliabilityRollup


class RollupManager:
    def __init__(self):
        self._rollups: Dict[str, List[ReliabilityRollup]] = {}

    def record_rollup(self, rollup: ReliabilityRollup) -> None:
        if rollup.scope_id not in self._rollups:
            self._rollups[rollup.scope_id] = []
        self._rollups[rollup.scope_id].append(rollup)

    def get_latest_rollup(self, scope_id: str) -> Optional[ReliabilityRollup]:
        rollups = self._rollups.get(scope_id, [])
        if not rollups:
            return None
        return sorted(rollups, key=lambda r: r.timestamp)[-1]
