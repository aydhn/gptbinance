from app.research_plane.models import ResearchObservation
import datetime


class ObservationIntake:
    def process_replay_observation(
        self, observation_id: str, text: str, confidence: float
    ) -> ResearchObservation:
        return ResearchObservation(
            observation_id=observation_id,
            source="replay",
            text=text,
            confidence_score=confidence,
            freshness=datetime.datetime.now(datetime.timezone.utc),
        )

    def process_runtime_anomaly(
        self, observation_id: str, text: str, confidence: float
    ) -> ResearchObservation:
        return ResearchObservation(
            observation_id=observation_id,
            source="runtime_anomaly",
            text=text,
            confidence_score=confidence,
            freshness=datetime.datetime.now(datetime.timezone.utc),
        )
