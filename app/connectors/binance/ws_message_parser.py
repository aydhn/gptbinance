import json
import logging
from typing import Any, Dict, Optional, Union

from app.data.live_stream_models import (
    KlineUpdateEvent,
    TickerEvent,
    BookTickerEvent,
    StreamEnvelope,
)

logger = logging.getLogger(__name__)


class BinanceWsMessageParser:
    """
    Isolates the raw websocket payload structure from the rest of the application.
    Parses JSON and returns strictly typed normalized domain events.
    """

    def parse_message(
        self, raw_message: str
    ) -> Optional[
        Union[KlineUpdateEvent, TickerEvent, BookTickerEvent, StreamEnvelope]
    ]:
        try:
            payload = json.loads(raw_message)

            # Combined streams are typically wrapped in {"stream": "...", "data": {...}}
            if "stream" in payload and "data" in payload:
                stream_name = payload["stream"]
                data = payload["data"]

                event = self._parse_data(data)
                if event:
                    return event
                # Fallback to envelope if we don't have a specific parser
                return StreamEnvelope(stream=stream_name, data=data)

            # Not a combined stream, just data
            return self._parse_data(payload)

        except json.JSONDecodeError:
            logger.error("Failed to decode JSON from websocket message.", exc_info=True)
            return None
        except Exception as e:
            logger.error(f"Unexpected error parsing message: {e}", exc_info=True)
            return None

    def _parse_data(
        self, data: Dict[str, Any]
    ) -> Optional[Union[KlineUpdateEvent, TickerEvent, BookTickerEvent]]:
        if not isinstance(data, dict):
            return None

        event_type = data.get("e")

        if event_type == "kline":
            return self._parse_kline(data)
        elif event_type == "24hrTicker":
            return self._parse_ticker(data)
        elif (
            "u" in data
            and "s" in data
            and "b" in data
            and "a" in data
            and not event_type
        ):
            # Book ticker often lacks "e" field, identified by "u" (updateId)
            return self._parse_book_ticker(data)

        # Unhandled event type
        return None

    def _parse_kline(self, data: Dict[str, Any]) -> KlineUpdateEvent:
        k = data["k"]
        return KlineUpdateEvent(
            event_type="kline",
            event_time=data["E"],
            symbol=data["s"],
            interval=k["i"],
            open_time=k["t"],
            close_time=k["T"],
            open_price=float(k["o"]),
            high_price=float(k["h"]),
            low_price=float(k["l"]),
            close_price=float(k["c"]),
            volume=float(k["v"]),
            quote_asset_volume=float(k["q"]),
            number_of_trades=k["n"],
            is_closed=k["x"],
        )

    def _parse_ticker(self, data: Dict[str, Any]) -> TickerEvent:
        return TickerEvent(
            event_type="24hrTicker",
            event_time=data["E"],
            symbol=data["s"],
            price_change=float(data["p"]),
            price_change_percent=float(data["P"]),
            weighted_avg_price=float(data["w"]),
            last_price=float(data["c"]),
            last_quantity=float(data["Q"]),
            open_price=float(data["o"]),
            high_price=float(data["h"]),
            low_price=float(data["l"]),
            volume=float(data["v"]),
            quote_volume=float(data["q"]),
            open_time=data["O"],
            close_time=data["C"],
            first_trade_id=data["F"],
            last_trade_id=data["L"],
            number_of_trades=data["n"],
        )

    def _parse_book_ticker(self, data: Dict[str, Any]) -> BookTickerEvent:
        return BookTickerEvent(
            update_id=data["u"],
            symbol=data["s"],
            best_bid_price=float(data["b"]),
            best_bid_qty=float(data["B"]),
            best_ask_price=float(data["a"]),
            best_ask_qty=float(data["A"]),
            event_time=data.get("E", 0),  # Might not be present
        )
