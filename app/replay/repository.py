import logging
from typing import Optional

from app.replay.models import ReplayConfig, DecisionReplayResult
from app.replay.engine import DefaultReplayEngine
from app.replay.storage import DummyReplayStorage

logger = logging.getLogger(__name__)


class ReplayRepository:
    def __init__(self):
        self.engine = DefaultReplayEngine()
        self.storage = DummyReplayStorage()

    def run_and_save(self, config: ReplayConfig) -> DecisionReplayResult:
        result = self.engine.run_replay(config)
        self.storage.save_run(result)
        return result

    def get_run(self, run_id: str) -> Optional[DecisionReplayResult]:
        return self.storage.get_run(run_id)


replay_repository = ReplayRepository()
