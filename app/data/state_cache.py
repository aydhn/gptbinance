import logging
from typing import Dict, Any, Optional
from threading import Lock

from app.data.live_stream_models import KlineUpdateEvent, TickerEvent, BookTickerEvent

logger = logging.getLogger(__name__)


class StateCache:
    """
    Holds the latest known state for quick synchronous access.
    """

    def __init__(self):
        self._lock = Lock()
        # symbol -> {interval -> KlineUpdateEvent}
        self._klines: Dict[str, Dict[str, KlineUpdateEvent]] = {}
        # symbol -> TickerEvent
        self._tickers: Dict[str, TickerEvent] = {}
        # symbol -> BookTickerEvent
        self._book_tickers: Dict[str, BookTickerEvent] = {}

    def update_kline(self, event: KlineUpdateEvent) -> None:
        with self._lock:
            if event.symbol not in self._klines:
                self._klines[event.symbol] = {}
            self._klines[event.symbol][event.interval] = event

    def update_ticker(self, event: TickerEvent) -> None:
        with self._lock:
            self._tickers[event.symbol] = event

    def update_book_ticker(self, event: BookTickerEvent) -> None:
        with self._lock:
            self._book_tickers[event.symbol] = event

    def get_latest_kline(
        self, symbol: str, interval: str
    ) -> Optional[KlineUpdateEvent]:
        with self._lock:
            return self._klines.get(symbol, {}).get(interval)

    def get_latest_ticker(self, symbol: str) -> Optional[TickerEvent]:
        with self._lock:
            return self._tickers.get(symbol)

    def get_latest_book_ticker(self, symbol: str) -> Optional[BookTickerEvent]:
        with self._lock:
            return self._book_tickers.get(symbol)

    def get_snapshot(self) -> Dict[str, Any]:
        with self._lock:
            return {
                "klines": {
                    sym: {inv: k.model_dump() for inv, k in intervals.items()}
                    for sym, intervals in self._klines.items()
                },
                "tickers": {sym: t.model_dump() for sym, t in self._tickers.items()},
                "book_tickers": {
                    sym: b.model_dump() for sym, b in self._book_tickers.items()
                },
            }
