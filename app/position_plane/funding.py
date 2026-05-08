from decimal import Decimal
import uuid

from app.position_plane.models import FundingAttributionRecord


class FundingCalculator:
    @staticmethod
    def attribute_funding(
        symbol: str, amount: Decimal, rate: Decimal
    ) -> FundingAttributionRecord:
        return FundingAttributionRecord(
            record_id=str(uuid.uuid4()),
            symbol=symbol,
            amount=amount,  # Can be positive or negative
            currency="QUOTE",
            funding_rate=rate,
        )
