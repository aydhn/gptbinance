from typing import List, Dict, Optional
from app.knowledge.models import TrainingModule


class TrainingRegistry:
    def __init__(self):
        self._modules: Dict[str, TrainingModule] = {}

    def register(self, module: TrainingModule) -> None:
        self._modules[module.module_id] = module

    def get_module(self, module_id: str) -> Optional[TrainingModule]:
        return self._modules.get(module_id)

    def list_modules(self) -> List[TrainingModule]:
        return list(self._modules.values())


training_registry = TrainingRegistry()
