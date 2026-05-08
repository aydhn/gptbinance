from typing import Dict, Optional, Any
from app.model_plane.exceptions import ModelPlaneError
from pydantic import BaseModel


class ModelInputDescriptor(BaseModel):
    input_id: str
    feature_manifest_id: str
    config_threshold_refs: Optional[Dict[str, str]] = None
    market_truth_trust_refs: Optional[Dict[str, str]] = None
    freshness_ms: Optional[int] = None
    is_stale: bool = False


class ModelInputRegistry:
    def __init__(self):
        self._inputs: Dict[str, ModelInputDescriptor] = {}

    def register_input(self, descriptor: ModelInputDescriptor) -> None:
        if not descriptor.input_id:
            raise ModelPlaneError("Input ID is required.")
        self._inputs[descriptor.input_id] = descriptor

    def get_input(self, input_id: str) -> Optional[ModelInputDescriptor]:
        return self._inputs.get(input_id)

    def validate_freshness(self, input_id: str, max_age_ms: int) -> bool:
        descriptor = self.get_input(input_id)
        if not descriptor:
            return False
        if descriptor.freshness_ms is None:
            return False

        is_fresh = descriptor.freshness_ms <= max_age_ms
        descriptor.is_stale = not is_fresh
        return is_fresh
