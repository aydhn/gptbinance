import time
from typing import Dict, Tuple
from .models import CarryCostSnapshot, FundingSnapshot, BorrowSnapshot
from .enums import FundingDirection, BorrowState
from app.products.enums import ProductType

class CarryCostAccounting:
    def __init__(self):
        self._accrued_funding: Dict[str, float] = {} # symbol -> amount
        self._accrued_interest: Dict[str, float] = {} # asset -> amount

    def add_funding_charge(self, symbol: str, amount: float):
        self._accrued_funding[symbol] = self._accrued_funding.get(symbol, 0.0) + amount

    def add_borrow_interest(self, asset: str, amount: float):
        self._accrued_interest[asset] = self._accrued_interest.get(asset, 0.0) + amount

    def get_carry_cost_snapshot(self, product_type: ProductType, symbol: str) -> CarryCostSnapshot:
        base_asset = symbol.replace("USDT", "") # Very naive, just for structure
        quote_asset = "USDT"

        funding_total = self._accrued_funding.get(symbol, 0.0)
        borrow_total = self._accrued_interest.get(base_asset, 0.0) + self._accrued_interest.get(quote_asset, 0.0)

        fs = None
        if product_type in (ProductType.FUTURES_USDM, ProductType.FUTURES_COINM):
            fs = FundingSnapshot(
                symbol=symbol,
                funding_rate=0.0, # Placeholder
                next_funding_time=int(time.time()) + 28800,
                direction=FundingDirection.PAY if funding_total > 0 else FundingDirection.RECEIVE,
                estimated_cost=funding_total
            )

        bs = None
        if product_type == ProductType.MARGIN:
             bs = BorrowSnapshot(
                asset=base_asset,
                borrowed_amount=0.0, # Placeholder
                interest_rate=0.0,
                state=BorrowState.HEALTHY
            )

        return CarryCostSnapshot(
            product_type=product_type,
            symbol=symbol,
            total_accrued_cost=funding_total + borrow_total,
            funding_snapshot=fs,
            borrow_snapshot=bs
        )
