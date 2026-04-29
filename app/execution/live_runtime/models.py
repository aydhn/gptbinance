from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from datetime import datetime
from app.execution.live_runtime.enums import (
    LiveRolloutMode,
    LiveSessionStatus,
    LiveRuntimeVerdict,
    FlattenMode,
    RollbackSeverity,
    CapitalCapType,
    LiveAuditEventType,
    SessionArmingStatus,
    LiveSafetyStatus,
)


class LiveSymbolAllowance(BaseModel):
    symbol: str
    max_notional_usd: float
    max_orders: int


class LiveCapitalCaps(BaseModel):
    max_session_notional_usd: float
    max_daily_loss_usd: float
    max_live_exposure_usd: float
    max_new_orders_per_session: int
    allowlist: List[LiveSymbolAllowance] = Field(default_factory=list)


class LiveSessionConfig(BaseModel):
    rollout_mode: LiveRolloutMode
    capital_caps: LiveCapitalCaps
    duration_seconds: int = 3600
    require_telegram_notify: bool = True


class LiveStartGateReport(BaseModel):
    passed: bool
    reasons: List[str] = Field(default_factory=list)
    blockers: List[str] = Field(default_factory=list)
    warnings: List[str] = Field(default_factory=list)
    recommended_actions: List[str] = Field(default_factory=list)
    effective_rollout_mode: LiveRolloutMode


class LiveSessionState(BaseModel):
    status: LiveSessionStatus = LiveSessionStatus.INITIALIZING
    arming_status: SessionArmingStatus = SessionArmingStatus.DISARMED
    safety_status: LiveSafetyStatus = LiveSafetyStatus.HEALTHY
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None


class LiveRun(BaseModel):
    run_id: str
    config: LiveSessionConfig
    state: LiveSessionState = Field(default_factory=LiveSessionState)
    created_at: datetime = Field(default_factory=datetime.utcnow)


class LivePosition(BaseModel):
    symbol: str
    qty: float = 0.0
    avg_entry_price: float = 0.0
    realized_pnl: float = 0.0
    unrealized_pnl: float = 0.0


class LivePositionBook(BaseModel):
    positions: Dict[str, LivePosition] = Field(default_factory=dict)
    last_updated: datetime = Field(default_factory=datetime.utcnow)


class LiveFillRecord(BaseModel):
    fill_id: str
    order_id: str
    client_order_id: str
    symbol: str
    side: str
    qty: float
    price: float
    fee: float
    fee_asset: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class LiveBalanceSnapshot(BaseModel):
    asset: str
    free: float
    locked: float


class LiveAccountSnapshot(BaseModel):
    run_id: str
    balances: List[LiveBalanceSnapshot] = Field(default_factory=list)
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class LivePnlSnapshot(BaseModel):
    symbol: str
    realized_pnl: float
    unrealized_pnl: float


class LiveEquitySnapshot(BaseModel):
    run_id: str
    total_equity_usd: float
    max_drawdown_pct: float
    pnl_by_symbol: List[LivePnlSnapshot] = Field(default_factory=list)
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class LiveRuntimeDecision(BaseModel):
    verdict: LiveRuntimeVerdict
    reason: str
    cap_type: Optional[CapitalCapType] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class LiveRolloutPlan(BaseModel):
    mode: LiveRolloutMode
    caps: LiveCapitalCaps


class LiveRollbackPlan(BaseModel):
    run_id: str
    severity: RollbackSeverity
    reason: str
    disarm_mainnet: bool = True
    trigger_flatten: bool = False


class LiveFlattenRequest(BaseModel):
    run_id: str
    mode: FlattenMode
    reason: str


class LiveFlattenResult(BaseModel):
    run_id: str
    success: bool
    orders_cancelled: int
    positions_closed: int
    errors: List[str] = Field(default_factory=list)
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class LiveAuditRecord(BaseModel):
    run_id: str
    event_type: LiveAuditEventType
    details: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class LiveSessionSummary(BaseModel):
    run_id: str
    start_time: Optional[datetime]
    end_time: Optional[datetime]
    total_orders: int = 0
    total_fills: int = 0
    final_equity: float = 0.0
    max_drawdown_pct: float = 0.0
    vetoes: int = 0


class LiveAfterActionSummary(BaseModel):
    run_id: str
    summary: LiveSessionSummary
    key_events: List[LiveAuditRecord] = Field(default_factory=list)
    generated_at: datetime = Field(default_factory=datetime.utcnow)


class LiveArtifactManifest(BaseModel):
    run_id: str
    has_account_snapshot: bool = False
    has_pnl_snapshot: bool = False
    has_audit_trail: bool = False
    has_after_action: bool = False
