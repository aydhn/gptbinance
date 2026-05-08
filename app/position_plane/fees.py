from decimal import Decimal
import uuid

from app.position_plane.models import FeeAttributionRecord
from app.position_plane.enums import PnlComponent


class FeeCalculator:
    @staticmethod
    def attribute_fee(
        symbol: str, amount: Decimal, is_maker: bool, fill_id: str
    ) -> FeeAttributionRecord:
        fee_type = PnlComponent.MAKER_FEE if is_maker else PnlComponent.TAKER_FEE
        return FeeAttributionRecord(
            record_id=str(uuid.uuid4()),
            symbol=symbol,
            amount=-abs(amount),  # Fees are always an expense
            currency="QUOTE",
            fee_type=fee_type,
            source_fill_id=fill_id,
        )
