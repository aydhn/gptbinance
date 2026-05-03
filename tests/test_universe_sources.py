import requests
import pytest
from unittest.mock import patch, MagicMock
from app.universe.sources import BinanceSpotSourceAdapter
from datetime import datetime, timezone

def test_binance_spot_source_adapter_success():
    adapter = BinanceSpotSourceAdapter()

    with patch("requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = {"symbols": [{"symbol": "BTCUSDT"}]}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        symbols = adapter.fetch_instruments()

        assert len(symbols) == 1
        assert symbols[0]["symbol"] == "BTCUSDT"
        assert adapter.get_source_freshness() > datetime.min.replace(tzinfo=timezone.utc)

def test_binance_spot_source_adapter_failure():
    adapter = BinanceSpotSourceAdapter()

    with patch("requests.get") as mock_get:
        mock_get.side_effect = requests.RequestException("Network error")

        symbols = adapter.fetch_instruments()

        assert len(symbols) == 0
        assert adapter.get_source_freshness() == datetime.min.replace(tzinfo=timezone.utc)
