from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime

from app.backtest.walkforward.enums import (
    WalkForwardMode,
    WindowScheme,
    SelectionPolicy,
    PromotionVerdict,
    SegmentStatus,
    AggregateVerdict,
    GateSeverity,
)
from app.strategies.models import StrategySpec
from app.backtest.models import BacktestResult


class WalkForwardConfig(BaseModel):
    symbol: str
    interval: str
    start_ts: int
    end_ts: int
    feature_set: str
    strategy_set: str
    mode: WalkForwardMode = WalkForwardMode.STANDARD
    window_scheme: WindowScheme = WindowScheme.ROLLING
    is_bars: int = Field(..., gt=0)
    oos_bars: int = Field(..., gt=0)
    step_bars: int = Field(..., gt=0)
    selection_policy: SelectionPolicy = SelectionPolicy.BALANCED
    min_trades_is: int = 5
    min_trades_oos: int = 2


class WalkForwardWindow(BaseModel):
    segment_index: int
    is_start: int
    is_end: int
    oos_start: int
    oos_end: int
    is_length: int
    oos_length: int
    is_valid: bool = True
    reason: Optional[str] = None


class WalkForwardPlan(BaseModel):
    config: WalkForwardConfig
    windows: List[WalkForwardWindow]


class FrozenStrategyBundle(BaseModel):
    spec: StrategySpec
    metadata: Dict[str, Any] = Field(default_factory=dict)
    frozen_at: str


class CandidateSelectionResult(BaseModel):
    selected_candidate: Optional[FrozenStrategyBundle]
    selection_rationale: str
    verdict: PromotionVerdict
    alternatives: List[Dict[str, Any]] = Field(default_factory=dict)


class WindowDiagnostic(BaseModel):
    is_expectancy: float
    oos_expectancy: float
    expectancy_decay: float
    is_trade_count: int
    oos_trade_count: int
    oos_max_drawdown: float
    warnings: List[str] = Field(default_factory=list)


class WalkForwardSegmentResult(BaseModel):
    segment_index: int
    window: WalkForwardWindow
    status: SegmentStatus
    selection: Optional[CandidateSelectionResult] = None
    oos_result: Optional[BacktestResult] = None
    diagnostics: Optional[WindowDiagnostic] = None
    error_message: Optional[str] = None


class WindowPerformanceSummary(BaseModel):
    segment_index: int
    status: str
    oos_trades: int
    oos_total_return: float
    oos_expectancy: float
    oos_max_drawdown: float


class OOSAggregateCurve(BaseModel):
    timestamps: List[int]
    equity: List[float]


class WalkForwardAggregateResult(BaseModel):
    total_segments: int
    completed_segments: int
    total_oos_trades: int
    aggregate_oos_return: float
    aggregate_oos_expectancy: float
    aggregate_oos_max_drawdown: float
    segment_summaries: List[WindowPerformanceSummary]


class PromotionGateResult(BaseModel):
    verdict: AggregateVerdict
    checks: List[Dict[str, Any]]
    summary: str


class WalkForwardArtifactManifest(BaseModel):
    run_id: str
    config: WalkForwardConfig
    plan: WalkForwardPlan
    aggregate_result: WalkForwardAggregateResult
    gates: PromotionGateResult
    created_at: str


class WalkForwardSummary(BaseModel):
    run_id: str
    symbol: str
    interval: str
    windows: int
    completed: int
    oos_return: float
    oos_expectancy: float
    oos_max_dd: float
    verdict: AggregateVerdict


class WalkForwardRun(BaseModel):
    run_id: str
    config: WalkForwardConfig
    plan: WalkForwardPlan
    segments: List[WalkForwardSegmentResult]
    aggregate: Optional[WalkForwardAggregateResult] = None
    gates: Optional[PromotionGateResult] = None
    created_at: str
