
from typing import Dict, Optional
from app.waterfall_plane.models import WaterfallObject

class CanonicalWaterfallRegistry:
    def __init__(self):
        self._waterfalls: Dict[str, WaterfallObject] = {}

    def register_waterfall(self, waterfall: WaterfallObject) -> None:
        self._waterfalls[waterfall.waterfall_id] = waterfall

    def get_waterfall(self, waterfall_id: str) -> Optional[WaterfallObject]:
        return self._waterfalls.get(waterfall_id)

    def list_waterfalls(self) -> list[WaterfallObject]:
        return list(self._waterfalls.values())
