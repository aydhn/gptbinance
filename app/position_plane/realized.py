from decimal import Decimal
import uuid


from app.position_plane.models import PositionLot, RealizedPnLRecord
from app.position_plane.enums import Side


class RealizedPnLCalculator:
    @staticmethod
    def calculate_from_reduction(
        lot: PositionLot,
        consumed_qty: Decimal,
        close_price: Decimal,
        close_fill_id: str,
    ) -> RealizedPnLRecord:
        multiplier = Decimal("1") if lot.side == Side.LONG else Decimal("-1")
        pnl_amount = (close_price - lot.entry_price) * consumed_qty * multiplier

        return RealizedPnLRecord(
            record_id=str(uuid.uuid4()),
            symbol=lot.symbol,
            sleeve_id=lot.sleeve_id,
            amount=pnl_amount,
            currency="QUOTE",  # Default quote currency
            source_lot_id=lot.id,
            close_fill_id=close_fill_id,
            proof_notes=[f"Reduced lot {lot.id} by {consumed_qty} at {close_price}"],
        )
