from typing import List, Optional
from app.research_plane.base import ResearchRegistryBase
from app.research_plane.models import ResearchItem
from app.research_plane.storage import ResearchStorage
from app.research_plane.exceptions import InvalidResearchItemError
import datetime


class CanonicalResearchRegistry(ResearchRegistryBase):
    def __init__(self, storage: ResearchStorage):
        self.storage = storage

    def register_item(self, item: ResearchItem) -> None:
        if not item.research_id:
            raise InvalidResearchItemError("Research ID cannot be empty.")
        if self.storage.load_item(item.research_id):
            raise InvalidResearchItemError(
                f"Research item {item.research_id} already exists."
            )

        # Enforce basic constraints
        if item.question and not item.question.falsifiable:
            raise InvalidResearchItemError("Research question must be falsifiable.")

        self.storage.save_item(item)

    def get_item(self, research_id: str) -> Optional[ResearchItem]:
        return self.storage.load_item(research_id)

    def update_item(self, item: ResearchItem) -> None:
        existing = self.storage.load_item(item.research_id)
        if not existing:
            raise InvalidResearchItemError(
                f"Research item {item.research_id} does not exist."
            )

        item.updated_at = datetime.datetime.now(datetime.timezone.utc)
        self.storage.save_item(item)

    def list_items(self) -> List[ResearchItem]:
        return self.storage.list_items()
