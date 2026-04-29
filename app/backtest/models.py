from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field
from datetime import datetime
from app.backtest.enums import (
    BacktestMode,
    OrderSide,
    FillAssumption,
    PositionSide,
    TradeStatus,
    CostModelType,
    SlippageModelType,
    SignalHandlingMode,
    ExposureMode,
)


class CostModelConfig(BaseModel):
    model_type: CostModelType = CostModelType.FIXED_BPS
    maker_fee_bps: float = 0.0
    taker_fee_bps: float = 0.04  # Binance VIP 0 USDT-M taker is 0.04% by default, or 0.1% Spot. Using 0.04%


class SlippageModelConfig(BaseModel):
    model_type: SlippageModelType = SlippageModelType.FIXED_BPS
    slippage_bps: float = 0.05  # 0.05% slippage


class ExecutionAssumption(BaseModel):
    fill_assumption: FillAssumption = FillAssumption.NEXT_BAR_OPEN
    cost_config: CostModelConfig = Field(default_factory=CostModelConfig)
    slippage_config: SlippageModelConfig = Field(default_factory=SlippageModelConfig)


class BacktestConfig(BaseModel):
    symbol: str
    interval: str
    start_time: datetime
    end_time: datetime
    strategy_set: str = "default"
    feature_set: str = "default"
    initial_capital: float = 10000.0
    mode: BacktestMode = BacktestMode.STANDARD
    execution: ExecutionAssumption = Field(default_factory=ExecutionAssumption)
    signal_mode: SignalHandlingMode = SignalHandlingMode.IGNORE_IF_IN_POSITION
    exposure_mode: ExposureMode = ExposureMode.SINGLE_POSITION
    allow_long: bool = True
    allow_short: bool = True


from typing import Optional
from uuid import UUID


class BacktestRun(BaseModel):
    run_id: str
    config: BacktestConfig
    started_at: datetime
    completed_at: Optional[datetime] = None


class SimulatedOrderIntent(BaseModel):
    risk_rejection_rationale: str = ""
    is_risk_approved: bool = False
    timestamp: datetime
    symbol: str
    side: OrderSide
    quantity: float
    is_reduce_only: bool = False
    intent_source: str  # Strategy name
    rationale: str = ""


class FillModelDecision(BaseModel):
    accepted: bool
    fill_price: float = 0.0
    fill_quantity: float = 0.0
    fill_timestamp: Optional[datetime] = None
    fee_paid: float = 0.0
    slippage_applied: float = 0.0
    reason: str = ""


class SimulatedFill(BaseModel):
    fill_id: str
    timestamp: datetime
    intent: SimulatedOrderIntent
    decision: FillModelDecision
    realized_pnl: float = 0.0  # Associated PnL if it closes part of position


class PositionState(BaseModel):
    symbol: str
    side: PositionSide = PositionSide.FLAT
    quantity: float = 0.0
    entry_price: float = 0.0
    realized_pnl: float = 0.0
    unrealized_pnl: float = 0.0
    open_timestamp: Optional[datetime] = None
    last_update_timestamp: Optional[datetime] = None


class TradeRecord(BaseModel):
    trade_id: str
    symbol: str
    side: PositionSide
    entry_timestamp: datetime
    exit_timestamp: Optional[datetime] = None
    entry_price: float
    exit_price: float = 0.0
    quantity: float
    status: TradeStatus = TradeStatus.OPEN
    realized_pnl: float = 0.0
    total_fees: float = 0.0
    total_slippage: float = 0.0
    strategy_source: str = ""


class EquitySnapshot(BaseModel):
    timestamp: datetime
    cash: float
    equity: float
    unrealized_pnl: float
    drawdown_pct: float
    high_water_mark: float


class DrawdownSnapshot(BaseModel):
    max_drawdown_pct: float = 0.0
    max_drawdown_value: float = 0.0
    current_drawdown_pct: float = 0.0


class PerformanceSummary(BaseModel):
    run_id: str
    total_return_pct: float = 0.0
    total_trades: int = 0
    winning_trades: int = 0
    losing_trades: int = 0
    hit_rate: float = 0.0
    average_win: float = 0.0
    average_loss: float = 0.0
    expectancy: float = 0.0
    profit_factor: float = 0.0
    max_drawdown_pct: float = 0.0
    exposure_ratio: float = 0.0
    total_fees_paid: float = 0.0
    final_equity: float = 0.0
    initial_capital: float = 0.0


class BacktestResult(BaseModel):
    run: BacktestRun
    summary: PerformanceSummary


class BacktestArtifactManifest(BaseModel):
    run_id: str
    timestamp: datetime
    config_path: str
    trade_log_path: str
    equity_curve_path: str
    summary_path: str


class BacktestStepContext(BaseModel):
    timestamp: datetime
    bar_open: float
    bar_high: float
    bar_low: float
    bar_close: float
    bar_volume: float
    features: Dict[str, Any] = Field(default_factory=dict)
