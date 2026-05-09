from typing import List, Optional
from app.experiment_plane.models import ExperimentDefinition
from app.experiment_plane.storage import ExperimentStorage


class ExperimentRepository:
    def __init__(self, storage: ExperimentStorage):
        self._storage = storage

    def save(self, experiment: ExperimentDefinition) -> None:
        self._storage.save(experiment)

    def get(self, experiment_id: str) -> Optional[ExperimentDefinition]:
        return self._storage.load(experiment_id)

    def list_all(self) -> List[ExperimentDefinition]:
        return self._storage.load_all()
