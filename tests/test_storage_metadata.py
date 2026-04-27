import pytest
from datetime import datetime, timezone
from app.storage.metadata import StoredMarketDataMetadata, MarketDataIndex


def test_market_data_index_add_get():
    index = MarketDataIndex()
    now = datetime.now(timezone.utc)

    meta = StoredMarketDataMetadata(
        symbol="ASELS",
        vendor="yfinance",
        timeframe="1d",
        file_path="yfinance/1d/ASELS.csv",
        row_count=100,
        adjusted=True,
        created_at=now,
        updated_at=now,
    )

    index.add_or_update(meta)

    retrieved = index.get("ASELS", "yfinance", "1d")
    assert retrieved is not None
    assert retrieved.symbol == "ASELS"
    assert retrieved.row_count == 100

    retrieved2 = index.get("asels.is", "YFINANCE", "1D")
    assert retrieved2 is not None
    assert retrieved2.symbol == "ASELS"


def test_market_data_index_serialization():
    index = MarketDataIndex()
    now = datetime.now(timezone.utc)

    meta = StoredMarketDataMetadata(
        symbol="THYAO",
        vendor="mock",
        timeframe="1h",
        file_path="mock/1h/THYAO.csv",
        row_count=50,
        adjusted=False,
        created_at=now,
        updated_at=now,
    )

    index.add_or_update(meta)

    data_dict = index.to_dict()
    assert "items" in data_dict

    new_index = MarketDataIndex.from_dict(data_dict)
    retrieved = new_index.get("THYAO", "mock", "1h")
    assert retrieved is not None
    assert retrieved.symbol == "THYAO"
