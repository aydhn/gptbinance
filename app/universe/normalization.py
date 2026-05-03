from typing import Dict, Any, Optional
from datetime import datetime, timezone
import logging
from app.universe.base import MetadataNormalizer
from app.universe.models import (
    ProductInstrument,
    InstrumentRef,
    InstrumentMetadata,
    ExchangeFilterSet,
    TickSizeRule,
    StepSizeRule,
    MinNotionalRule
)
from app.universe.enums import InstrumentType, InstrumentStatus, MetadataFreshness
from app.universe.exceptions import SymbolNormalizationError

logger = logging.getLogger(__name__)

class BinanceMetadataNormalizer(MetadataNormalizer):
    def get_canonical_symbol(self, symbol: str, product_type: InstrumentType) -> str:
        if not symbol:
            raise SymbolNormalizationError("Symbol cannot be empty")
        return symbol.upper().replace("-", "").replace("/", "")

    def normalize(self, raw_data: Dict[str, Any]) -> ProductInstrument:
        try:
            symbol = raw_data.get("symbol", "")
            if not symbol:
                raise SymbolNormalizationError("Missing symbol in raw data")

            # Determine product type (simplified logic for Binance)
            is_spot = raw_data.get("isSpotTradingAllowed", False)
            is_margin = raw_data.get("isMarginTradingAllowed", False)

            # Simple heuristic, real implementation might need more robust checks
            if "contractType" in raw_data:
                product_type = InstrumentType.FUTURES
            elif is_margin:
                product_type = InstrumentType.MARGIN
            elif is_spot:
                product_type = InstrumentType.SPOT
            else:
                product_type = InstrumentType.UNKNOWN

            canonical_symbol = self.get_canonical_symbol(symbol, product_type)

            ref = InstrumentRef(
                symbol=symbol,
                product_type=product_type,
                canonical_symbol=canonical_symbol
            )

            # Map status
            raw_status = raw_data.get("status", "UNKNOWN").upper()
            status_map = {
                "TRADING": InstrumentStatus.TRADING,
                "HALT": InstrumentStatus.HALTED,
                "BREAK": InstrumentStatus.BREAK,
                "POST_TRADING": InstrumentStatus.POST_TRADING,
                "PRE_TRADING": InstrumentStatus.PRE_TRADING,
                "SETTLING": InstrumentStatus.MAINTENANCE
            }
            status = status_map.get(raw_status, InstrumentStatus.UNKNOWN)

            # Parse filters
            filters = ExchangeFilterSet(raw_filters=raw_data.get("filters", []))
            for f in raw_data.get("filters", []):
                f_type = f.get("filterType")
                if f_type == "PRICE_FILTER":
                    filters.tick_size = TickSizeRule(
                        tick_size=float(f.get("tickSize", 0)),
                        min_price=float(f.get("minPrice", 0)),
                        max_price=float(f.get("maxPrice", 0))
                    )
                elif f_type == "LOT_SIZE":
                    filters.step_size = StepSizeRule(
                        step_size=float(f.get("stepSize", 0)),
                        min_qty=float(f.get("minQty", 0)),
                        max_qty=float(f.get("maxQty", 0))
                    )
                elif f_type == "NOTIONAL":
                    filters.min_notional = MinNotionalRule(
                        min_notional=float(f.get("minNotional", 0)),
                        apply_to_market=f.get("applyToMarket", False),
                        avg_price_mins=int(f.get("avgPriceMins", 0))
                    )

            # Parse metadata
            metadata = InstrumentMetadata(
                base_asset=raw_data.get("baseAsset", ""),
                quote_asset=raw_data.get("quoteAsset", "")
            )

            return ProductInstrument(
                ref=ref,
                status=status,
                filters=filters,
                metadata=metadata,
                freshness=MetadataFreshness.FRESH,
                last_update=datetime.now(timezone.utc),
                raw_data=raw_data
            )
        except Exception as e:
            logger.error(f"Error normalizing metadata for {raw_data.get('symbol')}: {e}")
            raise SymbolNormalizationError(f"Failed to normalize: {e}")
