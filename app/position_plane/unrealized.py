from decimal import Decimal
import uuid
from datetime import datetime, timezone

from app.position_plane.models import PositionState, UnrealizedPnLRecord
from app.position_plane.enums import Side
from app.performance_plane.enums import TrustVerdict
from app.performance_plane.models import PerformanceTrustVerdict


class UnrealizedPnLCalculator:
    @staticmethod
    def calculate(
        state: PositionState, mark_price: Decimal, mark_source: str, confidence: float
    ) -> UnrealizedPnLRecord:
        multiplier = Decimal("1") if state.side == Side.LONG else Decimal("-1")
        pnl_amount = (
            (mark_price - state.average_entry_price) * state.quantity * multiplier
        )

        caveats = []
        if confidence < 0.9:
            caveats.append("Low confidence in mark price.")

        return UnrealizedPnLRecord(
            record_id=str(uuid.uuid4()),
            symbol=state.symbol,
            sleeve_id=state.sleeve_id,
            amount=pnl_amount,
            currency="QUOTE",
            mark_price=mark_price,
            mark_source=mark_source,
            mark_timestamp=datetime.now(timezone.utc),
            confidence=confidence,
            caveats=caveats,
        )

    @staticmethod
    def export_trust_verdict(confidence: float) -> PerformanceTrustVerdict:
        verdict = TrustVerdict.TRUSTED
        blockers = []
        if confidence < 0.5:
            verdict = TrustVerdict.DEGRADED
            blockers.append("Critically low confidence in mark price.")
        elif confidence < 0.9:
            verdict = TrustVerdict.CAUTION
            blockers.append("Low confidence in mark price.")

        return PerformanceTrustVerdict(
            verdict_id=str(uuid.uuid4()),
            manifest_id="dummy",  # Replaced dynamically
            verdict=verdict,
            blockers=blockers,
            factors={"confidence": confidence},
        )
