from datetime import datetime, timezone
import uuid
from typing import Dict, Any
from decimal import Decimal

from app.ledger_plane.models import EquityView
from app.ledger_plane.enums import EquityClass
from app.performance_plane.enums import PerformanceDomain, ReturnClass, WindowClass
from app.performance_plane.models import PerformanceWindow, ReturnSurface
from app.performance_plane.returns import ReturnSurfaceBuilder


class EquityViewBuilder:
    @staticmethod
    def build(
        account_scope: str,
        equity_class: EquityClass,
        total_value: float,
        currency: str,
        metadata: Dict[str, Any] = None,
    ) -> EquityView:
        return EquityView(
            id=str(uuid.uuid4()),
            account_scope=account_scope,
            equity_class=equity_class,
            total_value=total_value,
            currency=currency,
            timestamp=datetime.now(timezone.utc),
            metadata=metadata or {},
        )

    @staticmethod
    def export_performance_surface(
        view: EquityView, start_time: datetime, end_time: datetime = None
    ) -> ReturnSurface:
        window = PerformanceWindow(
            window_class=WindowClass.DAILY,
            start_time=start_time,
            end_time=end_time,
            is_complete=end_time is not None,
        )
        return ReturnSurfaceBuilder.build_pnl_linked(
            domain=PerformanceDomain.PORTFOLIO,
            target_id=view.account_scope,
            window=window,
            realized_pnl=Decimal(str(view.total_value)),
            currency=view.currency,
            caveats=[
                "Equity-linked return base. Realized vs equity view differences may apply."
            ],
        )
