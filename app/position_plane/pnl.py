
from typing import List

from app.position_plane.models import (
    PositionPnLBreakdown,
    RealizedPnLRecord,
    UnrealizedPnLRecord,
    FeeAttributionRecord,
    FundingAttributionRecord,
    CarryAttributionRecord,
)


class PnLOrchestrator:
    @staticmethod
    def generate_breakdown(
        symbol: str,
        realized_records: List[RealizedPnLRecord],
        unrealized_records: List[UnrealizedPnLRecord],
        fee_records: List[FeeAttributionRecord],
        funding_records: List[FundingAttributionRecord],
        carry_records: List[CarryAttributionRecord],
    ) -> PositionPnLBreakdown:
        total_realized = sum(r.amount for r in realized_records)
        total_unrealized = sum(r.amount for r in unrealized_records)
        total_fees = sum(r.amount for r in fee_records)
        total_funding = sum(r.amount for r in funding_records)
        total_carry = sum(r.amount for r in carry_records)

        return PositionPnLBreakdown(
            symbol=symbol,
            realized_pnl=total_realized,
            unrealized_pnl=total_unrealized,
            total_fees=total_fees,
            total_funding=total_funding,
            total_carry=total_carry,
            currency="QUOTE",
        )
