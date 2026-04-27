import pytest
import pandas as pd
from datetime import datetime, timezone, timedelta
from app.storage.local_store import LocalMarketDataStore
from app.data.models import MarketDataFrame, Timeframe, DataVendor
from app.config.models import AppConfig
from app.core.paths import PATHS
import shutil


@pytest.fixture
def mock_df():
    dates = pd.date_range(start="2023-01-01", periods=5, freq="D")
    data = {
        "open": [10.0, 11.0, 12.0, 13.0, 14.0],
        "high": [10.5, 11.5, 12.5, 13.5, 14.5],
        "low": [9.5, 10.5, 11.5, 12.5, 13.5],
        "close": [10.2, 11.2, 12.2, 13.2, 14.2],
        "volume": [100, 110, 120, 130, 140],
    }
    df = pd.DataFrame(data, index=dates)
    df.index.name = "timestamp"
    return MarketDataFrame(df=df)


@pytest.fixture
def test_store(tmp_path):
    original_storage = PATHS.storage
    PATHS.storage = tmp_path / "storage"
    PATHS.storage.mkdir(parents=True, exist_ok=True)

    settings = AppConfig()
    store = LocalMarketDataStore(settings=settings)

    yield store

    PATHS.storage = original_storage
    if PATHS.storage.exists() and str(PATHS.storage) != str(original_storage):
        shutil.rmtree(PATHS.storage, ignore_errors=True)


def test_local_store_write_read(test_store, mock_df):
    symbol = "TEST"
    vendor = DataVendor.MOCK
    timeframe = Timeframe.D1

    meta = test_store.write_ohlcv(symbol, vendor, timeframe, mock_df)

    assert test_store.exists(symbol, vendor, timeframe)
    assert meta.row_count == 5
    assert meta.symbol == symbol
    assert meta.vendor == vendor.value

    read_df = test_store.read_ohlcv(symbol, vendor, timeframe)
    assert len(read_df.df) == 5
    assert list(read_df.df.columns) == ["open", "high", "low", "close", "volume"]
    assert read_df.df.index.name == "timestamp"


def test_local_store_delete(test_store, mock_df):
    symbol = "DELTEST"
    test_store.write_ohlcv(symbol, "mock", "1d", mock_df)

    assert test_store.exists(symbol, "mock", "1d")

    deleted = test_store.delete_ohlcv(symbol, "mock", "1d")
    assert deleted is True
    assert not test_store.exists(symbol, "mock", "1d")
    assert test_store.get_metadata(symbol, "mock", "1d") is None
