from typing import Dict, List
from app.semantic_plane.models import ThresholdRecord
from app.semantic_plane.exceptions import InvalidThresholdSemanticsError

class ThresholdManager:
    def __init__(self, registry):
        self.registry = registry
        self.thresholds: Dict[str, ThresholdRecord] = {}

    def register_threshold(self, threshold: ThresholdRecord):
        if not threshold.semantic_id or not threshold.threshold_id:
            raise InvalidThresholdSemanticsError("Threshold must have ID and semantic_id")
        if not threshold.implication_notes:
            raise InvalidThresholdSemanticsError("Threshold must have implication_notes (no threshold without obligation)")
        self.thresholds[threshold.threshold_id] = threshold
