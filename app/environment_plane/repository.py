from app.environment_plane.storage import EnvironmentStorage
from app.environment_plane.models import EnvironmentObject
from typing import List

class EnvironmentRepository:
    def __init__(self, storage: EnvironmentStorage):
        self.storage = storage

    def save_environment(self, env: EnvironmentObject) -> None:
        self.storage.save(env)

    def get_environment(self, environment_id: str) -> EnvironmentObject:
        return self.storage.load(environment_id)

    def list_environments(self) -> List[EnvironmentObject]:
        return self.storage.load_all()
