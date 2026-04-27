from decimal import Decimal, ROUND_DOWN
from typing import Optional, Dict, Any
from app.connectors.binance.models import SymbolMetadata


class SymbolRules:
    """
    Helper functions to enforce symbol constraints like minNotional, stepSize, and tickSize.
    Uses Decimal for precision safety.
    """

    @staticmethod
    def _get_filter(
        symbol_meta: SymbolMetadata, filter_type: str
    ) -> Optional[Dict[str, Any]]:
        for f in symbol_meta.filters:
            if f.filterType == filter_type:
                # Access extra fields provided by pydantic extra="allow"
                return getattr(f, "__pydantic_extra__", {}) or getattr(
                    f, "__dict__", {}
                )
        return None

    @staticmethod
    def round_price(
        price: float | str | Decimal, symbol_meta: SymbolMetadata
    ) -> Decimal:
        """
        Rounds a price down to the nearest valid tickSize.
        """
        price_dec = Decimal(str(price))

        price_filter = SymbolRules._get_filter(symbol_meta, "PRICE_FILTER")
        if not price_filter or "tickSize" not in price_filter:
            # Fallback to general precision if filter is missing
            precision = symbol_meta.quote_asset_precision
            return round(price_dec, precision)

        tick_size = Decimal(str(price_filter["tickSize"]))
        if tick_size <= 0:
            return price_dec

        # Round down to nearest tick
        quantized = (price_dec // tick_size) * tick_size

        # Remove trailing zeros for clean output
        return quantized.normalize()

    @staticmethod
    def round_quantity(
        quantity: float | str | Decimal, symbol_meta: SymbolMetadata
    ) -> Decimal:
        """
        Rounds a quantity down to the nearest valid stepSize.
        """
        qty_dec = Decimal(str(quantity))

        lot_filter = SymbolRules._get_filter(symbol_meta, "LOT_SIZE")
        if not lot_filter or "stepSize" not in lot_filter:
            # Fallback
            precision = symbol_meta.base_asset_precision
            return round(qty_dec, precision)

        step_size = Decimal(str(lot_filter["stepSize"]))
        if step_size <= 0:
            return qty_dec

        quantized = (qty_dec // step_size) * step_size
        return quantized.normalize()

    @staticmethod
    def check_min_notional(
        price: float | str | Decimal,
        quantity: float | str | Decimal,
        symbol_meta: SymbolMetadata,
    ) -> bool:
        """
        Checks if the proposed order value (price * qty) meets the MIN_NOTIONAL or NOTIONAL requirement.
        """
        price_dec = Decimal(str(price))
        qty_dec = Decimal(str(quantity))
        notional = price_dec * qty_dec

        # Check NOTIONAL filter (newer)
        notional_filter = SymbolRules._get_filter(symbol_meta, "NOTIONAL")
        if notional_filter and "minNotional" in notional_filter:
            min_notional = Decimal(str(notional_filter["minNotional"]))
            return notional >= min_notional

        # Check MIN_NOTIONAL filter (legacy)
        min_notional_filter = SymbolRules._get_filter(symbol_meta, "MIN_NOTIONAL")
        if min_notional_filter and "minNotional" in min_notional_filter:
            min_notional = Decimal(str(min_notional_filter["minNotional"]))
            return notional >= min_notional

        return True  # If no filter is present, we assume it's valid

    @staticmethod
    def is_valid_quantity(
        quantity: float | str | Decimal, symbol_meta: SymbolMetadata
    ) -> bool:
        """
        Checks if quantity is within minQty and maxQty bounds.
        """
        qty_dec = Decimal(str(quantity))
        lot_filter = SymbolRules._get_filter(symbol_meta, "LOT_SIZE")

        if not lot_filter:
            return True

        if "minQty" in lot_filter and qty_dec < Decimal(str(lot_filter["minQty"])):
            return False

        if "maxQty" in lot_filter and qty_dec > Decimal(str(lot_filter["maxQty"])):
            return False

        return True
