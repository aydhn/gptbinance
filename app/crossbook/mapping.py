from typing import List
from .models import BookPositionRef, UnifiedExposureNode

class PositionMapper:
    """Maps normalized book positions to unified exposure nodes."""
    def map_positions(self, positions: List[BookPositionRef]) -> List[UnifiedExposureNode]:
        return []
