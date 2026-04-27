import pytest
import pandas as pd
from datetime import datetime, timezone, timedelta
from app.data.data_service import MarketDataService, BaseMarketDataProvider
from app.data.models import MarketDataFrame, Timeframe, DataVendor
from app.storage.local_store import LocalMarketDataStore
from app.config.models import AppConfig
from app.core.paths import PATHS
import shutil


class DummyProvider(BaseMarketDataProvider):
    def __init__(self):
        self.fetch_count = 0

    @property
    def vendor(self) -> DataVendor:
        return DataVendor.MOCK

    def fetch_ohlcv(self, symbol: str, timeframe: Timeframe) -> MarketDataFrame:
        self.fetch_count += 1
        dates = pd.date_range(start="2023-01-01", periods=3, freq="D")
        data = {
            "open": [1.0, 2.0, 3.0],
            "high": [1.1, 2.1, 3.1],
            "low": [0.9, 1.9, 2.9],
            "close": [1.05, 2.05, 3.05],
            "volume": [10, 20, 30],
        }
        df = pd.DataFrame(data, index=dates)
        df.index.name = "timestamp"
        return MarketDataFrame(df=df)


@pytest.fixture
def store(tmp_path):
    original_storage = PATHS.storage
    PATHS.storage = tmp_path / "storage"
    PATHS.storage.mkdir(parents=True, exist_ok=True)

    settings = AppConfig()
    store = LocalMarketDataStore(settings=settings)

    yield store

    PATHS.storage = original_storage
    if PATHS.storage.exists() and str(PATHS.storage) != str(original_storage):
        shutil.rmtree(PATHS.storage, ignore_errors=True)


def test_data_service_caching_logic(store):
    provider = DummyProvider()
    service = MarketDataService(provider=provider, store=store, prefer_local=True)

    df1 = service.get_ohlcv("CACHE1", Timeframe.D1)
    assert provider.fetch_count == 1
    assert store.exists("CACHE1", DataVendor.MOCK, Timeframe.D1)

    df2 = service.get_ohlcv("CACHE1", Timeframe.D1)
    assert provider.fetch_count == 1

    df3 = service.get_ohlcv("CACHE1", Timeframe.D1, refresh=True)
    assert provider.fetch_count == 2

    df4 = service.get_ohlcv("NOSAVE", Timeframe.D1, save=False)
    assert provider.fetch_count == 3
    assert not store.exists("NOSAVE", DataVendor.MOCK, Timeframe.D1)


def test_data_service_provider_fallback():
    provider = DummyProvider()
    service = MarketDataService(provider=provider, store=None)

    df1 = service.get_ohlcv("FALLBACK", Timeframe.D1)
    assert provider.fetch_count == 1

    df2 = service.get_ohlcv("FALLBACK", Timeframe.D1)
    assert provider.fetch_count == 2
