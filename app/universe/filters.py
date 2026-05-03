import logging
from decimal import Decimal, ROUND_DOWN, ROUND_UP
from typing import Tuple, Optional
from app.universe.models import ExchangeFilterSet
from app.universe.exceptions import ExchangeFilterError

logger = logging.getLogger(__name__)

class FilterEvaluator:
    @staticmethod
    def validate_price(price: float, filters: ExchangeFilterSet) -> bool:
        if not filters.tick_size:
            return False

        p = Decimal(str(price))
        ts = Decimal(str(filters.tick_size.tick_size))
        min_p = Decimal(str(filters.tick_size.min_price))
        max_p = Decimal(str(filters.tick_size.max_price))

        if p < min_p or p > max_p:
            return False

        # Check if (price - min_price) % tick_size == 0
        rem = (p - min_p) % ts
        # Handle floating point inaccuracies in Decimal modulus
        return rem == 0 or rem == ts

    @staticmethod
    def validate_qty(qty: float, filters: ExchangeFilterSet) -> bool:
        if not filters.step_size:
            return False

        q = Decimal(str(qty))
        ss = Decimal(str(filters.step_size.step_size))
        min_q = Decimal(str(filters.step_size.min_qty))
        max_q = Decimal(str(filters.step_size.max_qty))

        if q < min_q or q > max_q:
            return False

        rem = (q - min_q) % ss
        return rem == 0 or rem == ss

    @staticmethod
    def validate_notional(price: float, qty: float, filters: ExchangeFilterSet) -> bool:
        if not filters.min_notional:
            return True # Notional filter is not always present

        notional = price * qty
        return notional >= filters.min_notional.min_notional

    @staticmethod
    def round_price_down(price: float, filters: ExchangeFilterSet) -> Optional[float]:
        if not filters.tick_size:
            return None

        p = Decimal(str(price))
        ts = Decimal(str(filters.tick_size.tick_size))
        min_p = Decimal(str(filters.tick_size.min_price))

        intervals = (p - min_p) // ts
        rounded = min_p + (intervals * ts)
        return float(rounded)

    @staticmethod
    def round_qty_down(qty: float, filters: ExchangeFilterSet) -> Optional[float]:
        if not filters.step_size:
            return None

        q = Decimal(str(qty))
        ss = Decimal(str(filters.step_size.step_size))
        min_q = Decimal(str(filters.step_size.min_qty))

        intervals = (q - min_q) // ss
        rounded = min_q + (intervals * ss)
        return float(rounded)
