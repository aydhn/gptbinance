from datetime import datetime
from typing import Any, Dict, Optional, Literal
from pydantic import BaseModel, Field


class SubscriptionSpec(BaseModel):
    symbol: str
    stream_type: str
    interval: Optional[str] = None

    @property
    def stream_name(self) -> str:
        s = self.symbol.lower()
        if self.stream_type == "kline" and self.interval:
            return f"{s}@kline_{self.interval}"
        elif self.stream_type == "ticker":
            return f"{s}@ticker"
        elif self.stream_type == "bookTicker":
            return f"{s}@bookTicker"
        else:
            return f"{s}@{self.stream_type}"


class StreamMessageStats(BaseModel):
    total_received: int = 0
    total_parsed: int = 0
    total_errors: int = 0
    last_message_time: Optional[datetime] = None


class StreamHealthSnapshot(BaseModel):
    is_alive: bool = False
    is_stale: bool = False
    reconnect_count: int = 0
    stats: StreamMessageStats = Field(default_factory=StreamMessageStats)
    last_error: Optional[str] = None


# Event Models
class StreamEnvelope(BaseModel):
    stream: str
    data: Dict[str, Any]


class MarketDataEvent(BaseModel):
    event_type: str
    event_time: int
    symbol: str


class KlineUpdateEvent(MarketDataEvent):
    event_type: Literal["kline"] = "kline"
    interval: str
    open_time: int
    close_time: int
    open_price: float
    high_price: float
    low_price: float
    close_price: float
    volume: float
    quote_asset_volume: float
    number_of_trades: int
    is_closed: bool


class TickerEvent(MarketDataEvent):
    event_type: Literal["24hrTicker"] = "24hrTicker"
    price_change: float
    price_change_percent: float
    weighted_avg_price: float
    last_price: float
    last_quantity: float
    open_price: float
    high_price: float
    low_price: float
    volume: float
    quote_volume: float
    open_time: int
    close_time: int
    first_trade_id: int
    last_trade_id: int
    number_of_trades: int


class BookTickerEvent(BaseModel):
    # Book ticker has slightly different format (no 'E' event time usually, but updateID)
    update_id: int
    symbol: str
    best_bid_price: float
    best_bid_qty: float
    best_ask_price: float
    best_ask_qty: float
    event_time: int = 0  # Synthesized locally if not present


class HeartbeatEvent(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    source: str = "ws_client"


class ReconnectEvent(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    attempt: int
    reason: str


class StreamStatusEvent(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    status: Literal["connected", "disconnected", "degraded"]
    reason: Optional[str] = None


class StreamErrorEvent(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    error_type: str
    message: str
    raw_payload: Optional[str] = None
