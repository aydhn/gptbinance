import logging
from typing import Dict, Any, List
from app.connectors.binance.client_factory import BinancePublicClient
from app.connectors.binance.models import (
    ExchangeInfoSnapshot,
    SymbolMetadata,
    SymbolFilter,
    RateLimit,
)
from app.connectors.binance.enums import SymbolStatus, MarketType
from app.connectors.binance.exceptions import (
    BinanceMetadataParseError,
    BinanceAPIError,
    BinanceConnectivityError,
)

logger = logging.getLogger(__name__)


class ExchangeInfoService:
    """
    Fetches, parses, and normalizes Binance exchange metadata.
    """

    def __init__(self, client: BinancePublicClient):
        self.client = client

    def get_exchange_info(self) -> ExchangeInfoSnapshot:
        """
        Fetches full exchange info and normalizes it to our domain models.
        """
        try:
            logger.info("Fetching exchange info from Binance...")
            raw_data = self.client.get("/api/v3/exchangeInfo")
            return self._parse_exchange_info(raw_data)
        except (BinanceConnectivityError, BinanceAPIError) as e:
            logger.error(f"Failed to fetch exchange info: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error in get_exchange_info: {e}")
            raise BinanceMetadataParseError(f"Unexpected error: {e}")

    def _parse_exchange_info(self, data: Dict[str, Any]) -> ExchangeInfoSnapshot:
        """
        Converts the raw API dictionary into our strictly typed Pydantic models.
        """
        try:
            server_time = data.get("serverTime", 0)

            # Parse Rate Limits
            rate_limits = []
            for limit_data in data.get("rateLimits", []):
                rate_limits.append(RateLimit(**limit_data))

            # Parse Symbols
            symbols = []
            for sym_data in data.get("symbols", []):
                try:
                    symbols.append(self._parse_symbol(sym_data))
                except Exception as e:
                    logger.warning(
                        f"Failed to parse symbol {sym_data.get('symbol', 'UNKNOWN')}: {e}"
                    )
                    # We continue to parse the rest rather than failing the whole snapshot
                    continue

            logger.info(
                f"Successfully parsed exchange info: {len(symbols)} symbols, {len(rate_limits)} rate limits."
            )
            return ExchangeInfoSnapshot(
                server_time=server_time, rate_limits=rate_limits, symbols=symbols
            )
        except Exception as e:
            raise BinanceMetadataParseError(f"Failed to parse exchange info: {e}")

    def _parse_symbol(self, sym_data: Dict[str, Any]) -> SymbolMetadata:
        """
        Extracts relevant fields from a single symbol dictionary.
        """
        # Determine status
        raw_status = sym_data.get("status", "UNKNOWN")
        try:
            status = SymbolStatus(raw_status)
        except ValueError:
            logger.warning(
                f"Unknown symbol status '{raw_status}' for {sym_data.get('symbol')}. Defaulting to UNKNOWN."
            )
            status = SymbolStatus.UNKNOWN

        # Determine permissions
        permissions = sym_data.get("permissions", [])
        is_spot = "SPOT" in permissions
        is_margin = "MARGIN" in permissions

        # Parse filters
        filters = []
        for f_data in sym_data.get("filters", []):
            filters.append(SymbolFilter(**f_data))

        return SymbolMetadata(
            symbol=sym_data["symbol"],
            status=status,
            base_asset=sym_data["baseAsset"],
            quote_asset=sym_data["quoteAsset"],
            market_type=MarketType.SPOT,  # Explicitly SPOT for this read-only phase
            is_spot_trading_allowed=is_spot,
            is_margin_trading_allowed=is_margin,
            base_asset_precision=sym_data.get("baseAssetPrecision", 8),
            quote_asset_precision=sym_data.get("quoteAssetPrecision", 8),
            base_commission_precision=sym_data.get("baseCommissionPrecision", 8),
            quote_commission_precision=sym_data.get("quoteCommissionPrecision", 8),
            filters=filters,
        )
