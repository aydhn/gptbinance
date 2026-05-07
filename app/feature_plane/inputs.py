from typing import Dict, Optional, List
from app.feature_plane.models import FeatureInputSurface
from app.feature_plane.exceptions import FeaturePlaneError


class InputSurfaceRegistry:
    def __init__(self):
        self._surfaces: Dict[str, FeatureInputSurface] = {}

    def register(self, surface: FeatureInputSurface) -> None:
        if surface.source_id in self._surfaces:
            raise FeaturePlaneError(f"Input Surface {surface.source_id} already exists")
        self._surfaces[surface.source_id] = surface

    def get(self, source_id: str) -> Optional[FeatureInputSurface]:
        return self._surfaces.get(source_id)
