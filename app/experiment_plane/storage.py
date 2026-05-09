from typing import List, Optional
from app.experiment_plane.models import ExperimentDefinition


class ExperimentStorage:
    def __init__(self, storage_dir: str = ".experiments"):
        self.storage_dir = storage_dir

    def save(self, experiment: ExperimentDefinition) -> None:
        pass

    def load(self, experiment_id: str) -> Optional[ExperimentDefinition]:
        return None

    def load_all(self) -> List[ExperimentDefinition]:
        return []
