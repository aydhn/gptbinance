from typing import Dict, List, Optional
from app.resolution_plane.base import ResolutionRegistryBase
from app.resolution_plane.models import ResolutionObject
from app.resolution_plane.exceptions import InvalidResolutionObjectError

class CanonicalResolutionRegistry(ResolutionRegistryBase):
    def __init__(self):
        self._resolutions: Dict[str, ResolutionObject] = {}

    def register_resolution(self, resolution: ResolutionObject) -> None:
        if not resolution.resolution_id:
            raise InvalidResolutionObjectError("Resolution ID must be provided")
        if resolution.resolution_id in self._resolutions:
            raise InvalidResolutionObjectError(f"Resolution {resolution.resolution_id} is already registered")
        self._resolutions[resolution.resolution_id] = resolution

    def get_resolution(self, resolution_id: str) -> Optional[ResolutionObject]:
        return self._resolutions.get(resolution_id)

    def list_resolutions(self) -> List[ResolutionObject]:
        return list(self._resolutions.values())
