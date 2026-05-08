from decimal import Decimal
import uuid
from typing import List

from app.performance_plane.models import ReturnSurface, PerformanceWindow
from app.performance_plane.enums import ReturnClass, PerformanceDomain


class ReturnSurfaceBuilder:
    @staticmethod
    def build_pnl_linked(
        domain: PerformanceDomain,
        target_id: str,
        window: PerformanceWindow,
        realized_pnl: Decimal,
        currency: str,
        caveats: List[str] = None,
    ) -> ReturnSurface:
        if caveats is None:
            caveats = []

        return ReturnSurface(
            surface_id=str(uuid.uuid4()),
            return_class=ReturnClass.REALIZED_PNL_LINKED,
            domain=domain,
            target_id=target_id,
            window=window,
            value=realized_pnl,
            currency=currency,
            caveats=caveats,
        )
