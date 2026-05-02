"""Data models for paper trading runtime."""

from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field
from datetime import datetime
from .enums import (
    PaperOrderStatus,
    PaperSessionStatus,
    PaperEventType,
    FillTrigger,
    SessionStopReason,
    PnlMode,
    RuntimeDecisionStatus,
    SessionHealth,
)


class PaperSessionConfig(BaseModel):
    symbols: List[str]
    stream_types: List[str]
    duration_seconds: Optional[int] = None
    feature_set: str = "core"
    strategy_set: str = "core"
    enable_telegram: bool = False
    fill_trigger: FillTrigger = FillTrigger.NEXT_TICK
    max_slippage_pct: float = 0.001
    maker_fee_pct: float = 0.0002
    taker_fee_pct: float = 0.0006
    initial_capital: float = 10000.0


class PaperOrderIntent(BaseModel):
    intent_id: str
    symbol: str
    side: str
    qty: float
    order_type: str = "MARKET"
    price: Optional[float] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    ttl_seconds: int = 10


class PaperOrder(BaseModel):
    order_id: str
    intent_id: str
    symbol: str
    side: str
    qty: float
    status: PaperOrderStatus
    created_at: datetime
    accepted_at: Optional[datetime] = None
    filled_at: Optional[datetime] = None
    fill_price: Optional[float] = None
    rejection_reason: Optional[str] = None
    fill_assumption: Optional[str] = None
    fees: float = 0.0


class PaperOrderUpdate(BaseModel):
    order_id: str
    status: PaperOrderStatus
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    message: Optional[str] = None


class PaperFill(BaseModel):
    fill_id: str
    order_id: str
    symbol: str
    side: str
    qty: float
    price: float
    fees: float
    slippage: float
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class PaperPosition(BaseModel):
    symbol: str
    qty: float = 0.0
    avg_entry_price: float = 0.0
    realized_pnl: float = 0.0
    unrealized_pnl: float = 0.0
    side: str = "FLAT"


class PaperPositionBook(BaseModel):
    positions: Dict[str, PaperPosition] = Field(default_factory=dict)


class PaperPnlSnapshot(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    realized_pnl: float
    unrealized_pnl: float
    total_pnl: float


class PaperEquitySnapshot(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    equity: float
    drawdown_pct: float


class PaperRuntimeEvent(BaseModel):
    event_id: str
    event_type: PaperEventType
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    details: Dict[str, Any]


class SessionHealthSnapshot(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    health: SessionHealth
    uptime_seconds: float
    stream_freshness_ms: float
    feature_lag_ms: float
    error_count: int
    open_positions: int
    current_drawdown_pct: float
    last_error: Optional[str] = None


class PaperRuntimeSummary(BaseModel):
    run_id: str
    start_time: datetime
    end_time: Optional[datetime] = None
    stop_reason: Optional[SessionStopReason] = None
    total_orders: int
    total_fills: int
    final_equity: float
    max_drawdown_pct: float
    risk_veto_count: int


class PaperArtifactManifest(BaseModel):
    run_id: str
    config: PaperSessionConfig
    summary: PaperRuntimeSummary


class PaperSessionState(BaseModel):
    run_id: str
    status: PaperSessionStatus
    start_time: datetime = Field(default_factory=datetime.utcnow)
    end_time: Optional[datetime] = None
    config: PaperSessionConfig
    active_symbols: List[str]
    kill_switch_active: bool = False
    last_heartbeat: Optional[datetime] = None


class RuntimeDecisionRecord(BaseModel):
    decision_id: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    symbol: str
    status: RuntimeDecisionStatus
    reason: Optional[str] = None
    intent: Optional[PaperOrderIntent] = None


class PendingIntentQueue(BaseModel):
    intents: List[PaperOrderIntent] = Field(default_factory=list)
