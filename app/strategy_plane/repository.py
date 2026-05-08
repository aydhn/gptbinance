from typing import List, Optional
from app.strategy_plane.storage import StrategyPlaneStorage
from app.strategy_plane.models import (
    StrategyManifest,
    StrategyLifecycleRecord,
    StrategyDefinition,
    StrategyHypothesis,
    StrategyThesis,
)
from app.strategy_plane.enums import LifecycleState


class StrategyPlaneRepository:
    def __init__(self, storage: StrategyPlaneStorage):
        self.storage = storage

    def get_latest_trusted_strategy(
        self, strategy_id: str
    ) -> Optional[StrategyManifest]:
        return self.storage.manifests.get(strategy_id)

    def get_lifecycle_history(self, strategy_id: str) -> List[StrategyLifecycleRecord]:
        return self.storage.lifecycle_records.get(strategy_id, [])

    def get_definition(self, strategy_id: str) -> Optional[StrategyDefinition]:
        return self.storage.definitions.get(strategy_id)

    def get_hypothesis(self, hypothesis_id: str) -> Optional[StrategyHypothesis]:
        return self.storage.hypotheses.get(hypothesis_id)

    def get_thesis(self, thesis_id: str) -> Optional[StrategyThesis]:
        return self.storage.theses.get(thesis_id)
