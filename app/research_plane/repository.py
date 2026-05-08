from app.research_plane.storage import ResearchStorage
from app.research_plane.registry import CanonicalResearchRegistry
from app.research_plane.models import ResearchItem
from typing import List, Optional


class ResearchRepository:
    def __init__(self, storage_path: str = "data/research_registry"):
        self.storage = ResearchStorage(storage_path)
        self.registry = CanonicalResearchRegistry(self.storage)

    def save(self, item: ResearchItem) -> None:
        if self.storage.load_item(item.research_id):
            self.registry.update_item(item)
        else:
            self.registry.register_item(item)

    def get(self, research_id: str) -> Optional[ResearchItem]:
        return self.registry.get_item(research_id)

    def list_all(self) -> List[ResearchItem]:
        return self.registry.list_items()
