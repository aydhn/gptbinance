from typing import Optional, List, Dict, Union
from abc import ABC, abstractmethod
from app.data.models import MarketDataFrame, Timeframe, DataVendor
from app.storage.local_store import LocalMarketDataStore


class BaseMarketDataProvider(ABC):
    @property
    @abstractmethod
    def vendor(self) -> DataVendor:
        pass

    @abstractmethod
    def fetch_ohlcv(self, symbol: str, timeframe: Timeframe) -> MarketDataFrame:
        pass


class MarketDataService:
    def __init__(
        self,
        provider: BaseMarketDataProvider,
        universe=None,
        store: Optional[LocalMarketDataStore] = None,
        prefer_local: bool = True,
    ):
        self.provider = provider
        self.universe = universe
        self.store = store
        self.prefer_local = prefer_local

    def get_ohlcv(
        self,
        symbol: str,
        timeframe: Union[Timeframe, str],
        refresh: bool = False,
        save: bool = True,
    ) -> MarketDataFrame:
        tf = Timeframe(timeframe) if isinstance(timeframe, str) else timeframe

        if self.store and self.prefer_local and not refresh:
            if self.store.exists(symbol, self.provider.vendor, tf):
                return self.store.read_ohlcv(symbol, self.provider.vendor, tf)

        data = self.provider.fetch_ohlcv(symbol, tf)

        if self.store and save:
            self.store.write_ohlcv(symbol, self.provider.vendor, tf, data)

        return data

    def get_many_ohlcv(
        self,
        symbols: List[str],
        timeframe: Union[Timeframe, str],
        refresh: bool = False,
        save: bool = True,
    ) -> Dict[str, MarketDataFrame]:
        results = {}
        for symbol in symbols:
            try:
                results[symbol] = self.get_ohlcv(symbol, timeframe, refresh, save)
            except Exception as e:
                raise RuntimeError(f"Failed to get data for symbol {symbol}: {e}")
        return results

    def provider_status(self) -> dict:
        return {
            "provider": self.provider.vendor.value,
            "has_store": self.store is not None,
            "prefer_local": self.prefer_local,
            "data_dir": (
                str(self.store.base_dir)
                if self.store and self.store.base_dir
                else "default"
            ),
        }
