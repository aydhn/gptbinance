from pydantic import BaseModel, Field, ConfigDict
from typing import List, Dict, Optional, Any
from app.connectors.binance.enums import SymbolStatus, MarketType


class ServerTimeSnapshot(BaseModel):
    server_time: int
    local_time: int
    latency_ms: int
    drift_ms: int


class SymbolFilter(BaseModel):
    model_config = ConfigDict(extra="allow")
    filterType: str


class SymbolMetadata(BaseModel):
    symbol: str
    status: SymbolStatus
    base_asset: str
    quote_asset: str
    market_type: MarketType = Field(default=MarketType.SPOT)
    is_spot_trading_allowed: bool
    is_margin_trading_allowed: bool

    # Precision fields
    base_asset_precision: int
    quote_asset_precision: int
    base_commission_precision: int
    quote_commission_precision: int

    # Derived from filters
    filters: List[SymbolFilter] = Field(default_factory=list)

    @property
    def is_tradable(self) -> bool:
        return self.status == SymbolStatus.TRADING and self.is_spot_trading_allowed


class RateLimit(BaseModel):
    rateLimitType: str
    interval: str
    intervalNum: int
    limit: int


class ExchangeInfoSnapshot(BaseModel):
    server_time: int
    rate_limits: List[RateLimit] = Field(default_factory=list)
    symbols: List[SymbolMetadata] = Field(default_factory=list)


class ConnectorHealthResult(BaseModel):
    is_healthy: bool
    config_ready: bool = False
    client_created: bool = False
    server_time_ok: bool = False
    exchange_info_ok: bool = False
    latency_status: str = "UNKNOWN"
    overall_status: str = "UNKNOWN"
    errors: List[str] = Field(default_factory=list)
