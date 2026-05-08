from app.execution_plane.models import SlicePlan
from typing import Optional

class SlicingEngine:
    @staticmethod
    def generate_plan(total_qty: float, min_notional: float, price: float) -> Optional[SlicePlan]:
        # Very simple slicing logic: slice into 3 if total is large enough.
        min_qty_required = min_notional / (price or 1.0)

        if total_qty > min_qty_required * 5:
            return SlicePlan(
                total_qty=total_qty,
                slice_count=3,
                min_viable_slice=min_qty_required,
                time_spacing_ms=5000,
                rationale="Qty is > 5x min notional, slicing into 3 parts.",
                lineage_ref="simple_slice_v1"
            )
        return None
