from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime
from app.risk.enums import (
    RiskVerdict,
    VetoSeverity,
    ThrottleType,
    SizingMode,
    ExposureScope,
    KillSwitchType,
    DrawdownState,
    RegimeRiskMode,
    ApprovalStatus,
)


class RiskPolicy(BaseModel):
    name: str
    description: str = ""
    scope: ExposureScope
    target: Optional[str] = None  # specific symbol or strategy, if applicable
    max_notional: Optional[float] = None
    max_fraction: Optional[float] = None
    is_hard_limit: bool = True


class RiskConfig(BaseModel):
    policies: List[RiskPolicy] = Field(default_factory=list)
    max_account_drawdown_pct: float = 20.0
    caution_drawdown_pct: float = 10.0
    reduce_drawdown_pct: float = 15.0
    max_concurrent_intents: int = 5
    default_sizing_mode: SizingMode = SizingMode.FIXED_FRACTION
    default_risk_fraction: float = 0.02
    min_position_notional: float = 10.0


class DrawdownStateModel(BaseModel):
    current_state: DrawdownState = DrawdownState.NORMAL
    peak_equity: float = 0.0
    current_equity: float = 0.0
    drawdown_pct: float = 0.0
    last_updated: datetime


class ExposureSnapshot(BaseModel):
    timestamp: datetime
    symbol_exposures: Dict[str, float] = Field(default_factory=dict)
    strategy_exposures: Dict[str, float] = Field(default_factory=dict)
    total_long_exposure: float = 0.0
    total_short_exposure: float = 0.0
    total_gross_exposure: float = 0.0
    total_equity: float = 0.0


class RiskContext(BaseModel):
    timestamp: datetime
    drawdown_state: DrawdownStateModel
    exposure_snapshot: ExposureSnapshot
    regime_mode: RegimeRiskMode = RegimeRiskMode.NORMAL
    volatility_multiplier: float = 1.0


# Forward reference placeholder for SimulatedOrderIntent,
# since it's from backtest models which risk shouldn't necessarily depend on strictly,
# but we need it for intent passing. Let's use a proxy or import it.
from app.backtest.models import SimulatedOrderIntent


class RiskEvaluationRequest(BaseModel):
    intent: SimulatedOrderIntent
    context: RiskContext
    available_capital: float


class RiskRejectionReason(BaseModel):
    source: str
    severity: VetoSeverity
    rationale: str


class PositionSizingResult(BaseModel):
    requested_size: float
    approved_size: float
    notional_value: float
    sizing_mode: SizingMode
    scaling_factors_applied: Dict[str, float] = Field(default_factory=dict)


class RiskDecision(BaseModel):
    verdict: RiskVerdict
    approved_intent: Optional[SimulatedOrderIntent] = None
    sizing: Optional[PositionSizingResult] = None
    rejection_reasons: List[RiskRejectionReason] = Field(default_factory=list)
    throttle_applied: ThrottleType = ThrottleType.NONE
    rationale: str = ""


class KillSwitchState(BaseModel):
    is_active: bool = False
    active_triggers: List[KillSwitchType] = Field(default_factory=list)
    last_triggered_at: Optional[datetime] = None
    rationale: str = ""


class RiskApprovalBundle(BaseModel):
    timestamp: datetime
    request_id: str
    decision: RiskDecision
    kill_switch_state: KillSwitchState


class RiskAuditRecord(BaseModel):
    timestamp: datetime
    run_id: str
    symbol: str
    intent_source: str
    side: str
    verdict: str
    requested_size: float
    approved_size: float
    rationale: str
    rejection_reasons: List[Dict[str, str]] = Field(default_factory=list)
