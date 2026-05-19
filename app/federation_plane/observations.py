from typing import Dict, List, Optional
from app.federation_plane.models import FederationObservationRecord
from app.federation_plane.exceptions import FederationPlaneError


class ObservationManager:
    def __init__(self):
        self._observations: Dict[str, FederationObservationRecord] = {}

    def register(self, record: FederationObservationRecord):
        if not record.observation_id:
            raise FederationPlaneError("No one-off federation comfort allowed.")
        self._observations[record.observation_id] = record

    def get_observation(
        self, observation_id: str
    ) -> Optional[FederationObservationRecord]:
        return self._observations.get(observation_id)

    def list_observations(self) -> List[FederationObservationRecord]:
        return list(self._observations.values())
