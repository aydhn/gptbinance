import pytest
from pathlib import Path
from app.config.models import AppConfig
from app.storage.paths import (
    get_ohlcv_file_path,
    get_data_dir,
    get_market_data_dir,
    get_metadata_dir,
    get_ohlcv_dir,
    InvalidSymbolError,
)


def test_get_ohlcv_file_path_normalizes_symbol():
    path = get_ohlcv_file_path("asels.is", "yfinance", "1d")
    assert path.name == "ASELS.csv"


def test_get_ohlcv_file_path_invalid_symbol():
    with pytest.raises(InvalidSymbolError):
        get_ohlcv_file_path("", "yfinance", "1d")

    with pytest.raises(InvalidSymbolError):
        get_ohlcv_file_path(None, "yfinance", "1d")


def test_get_ohlcv_file_path_expected_structure():
    settings = AppConfig()
    path = get_ohlcv_file_path("THYAO", "mock", "1h", settings=settings)

    expected_dir = get_ohlcv_dir("mock", "1h", settings)
    assert path == expected_dir / "THYAO.csv"
    assert path.parent.name == "1h"
    assert path.parent.parent.name == "mock"


def test_get_ohlcv_file_path_custom_extension():
    path = get_ohlcv_file_path("ASELS", "yfinance", "1d", extension="parquet")
    assert path.name == "ASELS.parquet"

    path = get_ohlcv_file_path("ASELS", "yfinance", "1d", extension=".parquet")
    assert path.name == "ASELS.parquet"
