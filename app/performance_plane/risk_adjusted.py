from decimal import Decimal

from app.performance_plane.models import ReturnSurface


class RiskAdjustedEvaluator:
    @staticmethod
    def evaluate_drawdown_adjusted(
        surface: ReturnSurface, max_drawdown: Decimal
    ) -> dict:
        result = float(surface.value)
        caveats = list(surface.caveats)

        if max_drawdown > 0:
            result = float(surface.value) / float(max_drawdown)
        else:
            caveats.append(
                "No drawdown recorded, risk-adjusted calculation meaningless."
            )

        return {
            "surface_id": surface.surface_id,
            "return_on_max_drawdown": result,
            "caveats": caveats,
        }
