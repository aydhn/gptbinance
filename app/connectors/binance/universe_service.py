from typing import List, Optional
from app.connectors.binance.models import ExchangeInfoSnapshot, SymbolMetadata
from app.connectors.binance.enums import SymbolStatus


class UniverseService:
    """
    Provides safe filtering mechanisms to extract a tradable universe of symbols
    from the full exchange info.
    """

    @staticmethod
    def get_active_usdt_pairs(
        exchange_info: ExchangeInfoSnapshot,
    ) -> List[SymbolMetadata]:
        """
        Returns only actively trading pairs that are quoted in USDT.
        This is a safe, standard baseline for the platform.
        """
        return [
            sym
            for sym in exchange_info.symbols
            if sym.is_tradable
            and sym.quote_asset == "USDT"
            and sym.status == SymbolStatus.TRADING
        ]

    @staticmethod
    def filter_universe(
        exchange_info: ExchangeInfoSnapshot,
        quote_asset: Optional[str] = None,
        require_spot: bool = True,
        require_margin: bool = False,
    ) -> List[SymbolMetadata]:
        """
        Generic filter for exploring the symbol universe.
        """
        filtered = []
        for sym in exchange_info.symbols:
            # Must be actively trading
            if not sym.is_tradable or sym.status != SymbolStatus.TRADING:
                continue

            if quote_asset and sym.quote_asset != quote_asset:
                continue

            if require_spot and not sym.is_spot_trading_allowed:
                continue

            if require_margin and not sym.is_margin_trading_allowed:
                continue

            filtered.append(sym)

        return filtered
