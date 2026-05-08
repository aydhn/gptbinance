from typing import List
from app.performance_plane.models import DragComponent
from app.performance_plane.enums import DragClass


class DragSurfaceAnalyzer:
    @staticmethod
    def summarize_drags(drags: List[DragComponent]) -> dict:
        summary = {drag_class.value: 0 for drag_class in DragClass}

        for drag in drags:
            if drag.drag_class.value in summary:
                # Note: we assume all currency is identical or handled separately.
                summary[drag.drag_class.value] += float(drag.impact_value)

        return summary
