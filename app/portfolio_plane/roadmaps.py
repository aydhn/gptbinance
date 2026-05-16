from typing import Dict, Optional
from app.portfolio_plane.models import RoadmapItem
from app.portfolio_plane.exceptions import PortfolioStorageError

class RoadmapManager:
    def __init__(self):
        self._items: Dict[str, RoadmapItem] = {}

    def register(self, item: RoadmapItem):
        if item.roadmap_item_id in self._items:
            raise PortfolioStorageError(f"Roadmap Item {item.roadmap_item_id} already exists")
        if item.is_committed and not item.integrity_notes:
            raise ValueError("Committed roadmap items must have integrity notes")
        self._items[item.roadmap_item_id] = item

    def get(self, item_id: str) -> Optional[RoadmapItem]:
        return self._items.get(item_id)

    def get_all(self) -> Dict[str, RoadmapItem]:
        return self._items.copy()
