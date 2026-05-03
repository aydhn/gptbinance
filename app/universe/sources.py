import logging
from typing import List, Dict, Any
from datetime import datetime, timezone
import requests
from app.universe.base import InstrumentSourceAdapter

logger = logging.getLogger(__name__)

class BinanceSpotSourceAdapter(InstrumentSourceAdapter):
    """
    Fetches official exchange info from Binance Spot API.
    Strictly prohibits HTML scraping. Uses only official JSON endpoints.
    """
    def __init__(self):
        self.endpoint = "https://api.binance.com/api/v3/exchangeInfo"
        self._last_fetch_time = None

    def fetch_instruments(self) -> List[Dict[str, Any]]:
        try:
            logger.info(f"Fetching exchange info from {self.endpoint}")
            response = requests.get(self.endpoint, timeout=10)
            response.raise_for_status()
            data = response.json()

            self._last_fetch_time = datetime.now(timezone.utc)
            symbols = data.get("symbols", [])
            logger.info(f"Fetched {len(symbols)} symbols from Binance Spot")
            return symbols

        except requests.RequestException as e:
            logger.error(f"Failed to fetch exchange info: {e}")
            return []

    def get_source_freshness(self) -> datetime:
        return self._last_fetch_time or datetime.min.replace(tzinfo=timezone.utc)

class BinanceFuturesSourceAdapter(InstrumentSourceAdapter):
    def __init__(self):
        self.endpoint = "https://fapi.binance.com/fapi/v1/exchangeInfo"
        self._last_fetch_time = None

    def fetch_instruments(self) -> List[Dict[str, Any]]:
        try:
            logger.info(f"Fetching exchange info from {self.endpoint}")
            response = requests.get(self.endpoint, timeout=10)
            response.raise_for_status()
            data = response.json()

            self._last_fetch_time = datetime.now(timezone.utc)
            symbols = data.get("symbols", [])
            logger.info(f"Fetched {len(symbols)} symbols from Binance Futures")
            return symbols

        except requests.RequestException as e:
            logger.error(f"Failed to fetch exchange info: {e}")
            return []

    def get_source_freshness(self) -> datetime:
        return self._last_fetch_time or datetime.min.replace(tzinfo=timezone.utc)
