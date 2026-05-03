import logging
from typing import Optional, Dict, List

from app.replay.models import DecisionReplayResult

logger = logging.getLogger(__name__)


class DummyReplayStorage:
    def __init__(self):
        self._runs: Dict[str, DecisionReplayResult] = {}

    def save_run(self, result: DecisionReplayResult) -> None:
        self._runs[result.run_id] = result
        logger.info(f"Saved replay run {result.run_id}")

    def get_run(self, run_id: str) -> Optional[DecisionReplayResult]:
        return self._runs.get(run_id)

    def list_runs(self) -> List[str]:
        return list(self._runs.keys())
