from typing import Dict, Optional
from app.supply_chain_plane.models import ContainerArtifactRecord


class ContainerArtifactRegistry:
    def __init__(self):
        self._containers: Dict[str, ContainerArtifactRecord] = {}

    def register_container(self, container: ContainerArtifactRecord) -> None:
        self._containers[container.container_id] = container

    def get_container(self, container_id: str) -> Optional[ContainerArtifactRecord]:
        return self._containers.get(container_id)
