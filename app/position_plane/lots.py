from decimal import Decimal
from typing import Dict, Any, Tuple
from datetime import datetime, timezone
import uuid

from app.position_plane.models import PositionLot
from app.position_plane.enums import ProductClass, Side
from app.position_plane.exceptions import InvalidPositionLotError


class LotManager:
    @staticmethod
    def create_lot_from_fill(fill: Dict[str, Any], sleeve_id: str) -> PositionLot:
        try:
            return PositionLot(
                id=str(uuid.uuid4()),
                symbol=fill["symbol"],
                product_class=ProductClass(fill.get("product_class", "spot_pair")),
                side=Side(fill["side"]),
                quantity=Decimal(str(fill["quantity"])),
                remaining_quantity=Decimal(str(fill["quantity"])),
                entry_price=Decimal(str(fill["price"])),
                created_at=datetime.now(timezone.utc),
                source_fill_id=fill.get("fill_id", str(uuid.uuid4())),
                sleeve_id=sleeve_id,
            )
        except KeyError as e:
            raise InvalidPositionLotError(f"Missing required field in fill: {e}")

    @staticmethod
    def consume_lot(lot: PositionLot, amount: Decimal) -> Tuple[PositionLot, Decimal]:
        """Consumes a specified amount from a lot. Returns updated lot and remaining amount."""
        if lot.is_closed:
            return lot, amount

        if amount <= lot.remaining_quantity:
            lot.remaining_quantity -= amount
            if lot.remaining_quantity == Decimal("0"):
                lot.is_closed = True
            return lot, Decimal("0")
        else:
            remaining = amount - lot.remaining_quantity
            lot.remaining_quantity = Decimal("0")
            lot.is_closed = True
            return lot, remaining
