from typing import Dict, Any, List
from decimal import Decimal
from datetime import datetime, timezone

from app.performance_plane.enums import PerformanceDomain, ReturnClass, WindowClass
from app.performance_plane.models import PerformanceWindow, ReturnSurface
from app.performance_plane.returns import ReturnSurfaceBuilder


class PnlCalculator:
    # Exports realized/unrealized/funding/fee/carry attribution using ledger cashflow surfaces.
    # Distinguishes authoritative PNL from ledger-posted cashflow and strengthens PNL-to-ledger lineage.

    @staticmethod
    def export_to_performance_surface(
        target_id: str,
        domain: PerformanceDomain,
        realized_pnl: Decimal,
        currency: str,
        start_time: datetime,
        end_time: datetime = None,
    ) -> ReturnSurface:
        window = PerformanceWindow(
            window_class=WindowClass.TRADE_LIFECYCLE,
            start_time=start_time,
            end_time=end_time,
            is_complete=end_time is not None,
        )
        return ReturnSurfaceBuilder.build_pnl_linked(
            domain=domain,
            target_id=target_id,
            window=window,
            realized_pnl=realized_pnl,
            currency=currency,
        )
