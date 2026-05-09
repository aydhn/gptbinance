import json
import os
from typing import List, Optional
from app.research_plane.models import ResearchItem, ResearchArtifactManifest
from app.research_plane.exceptions import ResearchStorageError
from pydantic import ValidationError


class ResearchStorage:
    def __init__(self, storage_path: str = "data/research_registry"):
        self.storage_path = storage_path
        os.makedirs(self.storage_path, exist_ok=True)
        self.items_path = os.path.join(self.storage_path, "items")
        self.manifests_path = os.path.join(self.storage_path, "manifests")
        os.makedirs(self.items_path, exist_ok=True)
        os.makedirs(self.manifests_path, exist_ok=True)

    def _get_item_path(self, research_id: str) -> str:
        return os.path.join(self.items_path, f"{research_id}.json")

    def save_item(self, item: ResearchItem) -> None:
        try:
            with open(self._get_item_path(item.research_id), "w") as f:
                f.write(item.model_dump_json(indent=2))
        except Exception as e:
            raise ResearchStorageError(f"Failed to save research item: {e}")

    def load_item(self, research_id: str) -> Optional[ResearchItem]:
        path = self._get_item_path(research_id)
        if not os.path.exists(path):
            return None
        try:
            with open(path, "r") as f:
                data = json.load(f)
                return ResearchItem.model_validate(data)
        except ValidationError as e:
            raise ResearchStorageError(f"Validation error loading research item: {e}")
        except Exception as e:
            raise ResearchStorageError(f"Failed to load research item: {e}")

    def list_items(self) -> List[ResearchItem]:
        items = []
        for filename in os.listdir(self.items_path):
            if filename.endswith(".json"):
                research_id = filename[:-5]
                item = self.load_item(research_id)
                if item:
                    items.append(item)
        return items

    def save_manifest(self, manifest: ResearchArtifactManifest) -> None:
        path = os.path.join(self.manifests_path, f"{manifest.manifest_id}.json")
        try:
            with open(path, "w") as f:
                f.write(manifest.model_dump_json(indent=2))
        except Exception as e:
            raise ResearchStorageError(f"Failed to save manifest: {e}")
