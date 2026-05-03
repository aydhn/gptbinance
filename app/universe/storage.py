import json
from pathlib import Path
from typing import List, Dict, Any
from app.core.paths import PATHS
from app.universe.models import ProductInstrument

class UniverseStorage:
    def __init__(self):
        self.base_dir = PATHS.storage / "universe"
        self.base_dir.mkdir(parents=True, exist_ok=True)

    def save_registry_snapshot(self, instruments: List[ProductInstrument], name: str = "latest"):
        path = self.base_dir / f"registry_{name}.json"
        data = [inst.model_dump(mode='json') for inst in instruments]
        with open(path, 'w') as f:
            json.dump(data, f, indent=2)

    def load_registry_snapshot(self, name: str = "latest") -> List[ProductInstrument]:
        path = self.base_dir / f"registry_{name}.json"
        if not path.exists():
            return []

        with open(path, 'r') as f:
            data = json.load(f)

        return [ProductInstrument.model_validate(d) for d in data]

    # Additional storage methods for snapshots, diffs, etc. would go here
    # Kept concise for the implementation
