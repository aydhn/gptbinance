from typing import List, Optional
from app.reliability.storage import storage
from app.reliability.models import (
    HealthScorecard,
    FreezeRecommendation,
    OperationalCadenceArtifact,
    ReliabilityTrendReport,
)


class ReliabilityRepository:
    def save_scorecard(self, scorecard: HealthScorecard):
        storage.save(f"scorecard_{scorecard.scorecard_id}", scorecard)

    def get_latest_scorecards(self) -> List[HealthScorecard]:
        # Simulated lookup
        raw = storage.list_all("scorecard_")
        return [HealthScorecard(**r) for r in raw]

    def save_freeze_recommendation(self, rec: FreezeRecommendation):
        storage.save(f"freeze_{rec.recommendation_id}", rec)

    def get_freeze_recommendations(self) -> List[FreezeRecommendation]:
        raw = storage.list_all("freeze_")
        return [FreezeRecommendation(**r) for r in raw]

    def save_cadence_artifact(self, artifact: OperationalCadenceArtifact):
        storage.save(f"cadence_{artifact.artifact_id}", artifact)

    def get_cadence_artifacts(self) -> List[OperationalCadenceArtifact]:
        raw = storage.list_all("cadence_")
        return [OperationalCadenceArtifact(**r) for r in raw]


repository = ReliabilityRepository()
