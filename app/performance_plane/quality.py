from typing import List
from app.performance_plane.models import ReturnSurface, AttributionTree


class PerformanceQualityChecker:
    @staticmethod
    def check_quality(surface: ReturnSurface, tree: AttributionTree) -> List[str]:
        warnings = []
        if not surface.window.is_complete:
            warnings.append("Incomplete performance window.")

        if tree.residual_value != 0:
            # We use a threshold to prevent floating point noise flags
            if abs(float(tree.residual_value)) > 0.01 * abs(float(surface.value)):
                warnings.append(
                    f"High unexplained residual value: {tree.residual_value}"
                )

        return warnings
