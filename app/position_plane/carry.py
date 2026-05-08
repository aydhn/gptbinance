from decimal import Decimal
import uuid

from app.position_plane.models import CarryAttributionRecord


class CarryCalculator:
    @staticmethod
    def attribute_carry(
        symbol: str, amount: Decimal, description: str
    ) -> CarryAttributionRecord:
        return CarryAttributionRecord(
            record_id=str(uuid.uuid4()),
            symbol=symbol,
            amount=-abs(amount),  # Carry costs are expenses
            currency="QUOTE",
            description=description,
        )
