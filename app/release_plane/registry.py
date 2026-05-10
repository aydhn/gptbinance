from typing import Dict, List, Optional
from app.release_plane.models import ReleaseDefinition
from app.release_plane.base import CanonicalReleaseRegistryBase
from app.release_plane.exceptions import InvalidReleaseDefinition

class CanonicalReleaseRegistry(CanonicalReleaseRegistryBase):
    def __init__(self):
        self._releases: Dict[str, ReleaseDefinition] = {}

    def register(self, release_def: ReleaseDefinition) -> None:
        if not release_def.release_id:
            raise InvalidReleaseDefinition("Release ID cannot be empty.")
        if release_def.release_id in self._releases:
            raise InvalidReleaseDefinition(f"Release {release_def.release_id} already exists.")

        # Enforce no undocumented release ids
        if "undocumented" in release_def.release_id.lower():
             raise InvalidReleaseDefinition("Undocumented releases are strictly prohibited.")

        self._releases[release_def.release_id] = release_def

    def get(self, release_id: str) -> Optional[ReleaseDefinition]:
        return self._releases.get(release_id)

    def get_all(self) -> List[ReleaseDefinition]:
        return list(self._releases.values())

# Global registry instance
registry = CanonicalReleaseRegistry()
