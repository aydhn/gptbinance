import json
import os
from pathlib import Path
from typing import Dict, Any, TypeVar, Type
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


class ModelPlaneStorage:
    def __init__(self, base_path: str = "data/model_plane"):
        self.base_path = Path(base_path)
        self.base_path.mkdir(parents=True, exist_ok=True)

    def _get_path(self, collection: str, item_id: str) -> Path:
        collection_path = self.base_path / collection
        collection_path.mkdir(exist_ok=True)
        return collection_path / f"{item_id}.json"

    def save(self, collection: str, item_id: str, data: BaseModel) -> None:
        path = self._get_path(collection, item_id)
        with open(path, "w") as f:
            f.write(data.model_dump_json(indent=2))

    def load(self, collection: str, item_id: str, model_class: Type[T]) -> T:
        path = self._get_path(collection, item_id)
        if not path.exists():
            raise FileNotFoundError(f"Item {item_id} not found in {collection}")
        with open(path, "r") as f:
            data = json.load(f)
        return model_class.model_validate(data)
