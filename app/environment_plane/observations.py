from app.environment_plane.models import EnvironmentObservationRecord

def record_observation(observation_type: str, sufficiency_notes: str) -> EnvironmentObservationRecord:
    return EnvironmentObservationRecord(observation_type=observation_type, sufficiency_notes=sufficiency_notes)
