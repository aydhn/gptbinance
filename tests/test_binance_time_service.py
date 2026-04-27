import pytest
from unittest.mock import MagicMock, patch
from app.connectors.binance.time_service import TimeService
from app.connectors.binance.exceptions import BinanceAPIError


def test_get_server_time_success():
    mock_client = MagicMock()
    mock_client.get.return_value = {"serverTime": 1600000000000}

    with patch("time.time") as mock_time:
        # Start time: 1600000000.000 (1600000000000 ms)
        # End time:   1600000000.100 (1600000000100 ms)
        mock_time.side_effect = [1600000000.000, 1600000000.100]

        service = TimeService(mock_client)
        snapshot = service.get_server_time()

        # RTT = 100ms
        # Approx local at server = 1600000000000 + 50 = 1600000000050
        # server_time = 1600000000000
        # Drift = 1600000000050 - 1600000000000 = 50

        assert snapshot.server_time == 1600000000000
        assert snapshot.local_time == 1600000000100
        assert snapshot.latency_ms == 100
        assert snapshot.drift_ms == 50


def test_get_server_time_invalid_response():
    mock_client = MagicMock()
    mock_client.get.return_value = {"wrongKey": 123}

    service = TimeService(mock_client)
    with pytest.raises(BinanceAPIError):
        service.get_server_time()
