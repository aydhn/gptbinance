from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime
from app.analytics.enums import (
    AnalyticsScope,
    DivergenceType,
    AnomalySeverity,
    ExecutionQualityVerdict,
    JournalEventType,
    ComparisonVerdict,
    DiagnosticConfidence,
    PeriodGranularity,
)


class AnalyticsConfig(BaseModel):
    scope: AnalyticsScope = AnalyticsScope.SESSION
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None


class AnalyticsRun(BaseModel):
    run_id: str
    config: AnalyticsConfig
    started_at: datetime
    completed_at: Optional[datetime] = None
    status: str = "running"


class TradeJournalEntry(BaseModel):
    entry_id: str
    run_id: str
    timestamp: datetime
    event_type: JournalEventType
    symbol: str
    strategy_ref: Optional[str] = None
    regime_ref: Optional[str] = None
    risk_decision_ref: Optional[str] = None
    portfolio_decision_ref: Optional[str] = None
    order_ref: Optional[str] = None
    fill_ref: Optional[str] = None
    bundle_ref: Optional[str] = None
    details: Dict[str, Any] = Field(default_factory=dict)


class TradeLifecycleSummary(BaseModel):
    trade_id: str
    symbol: str
    open_time: datetime
    close_time: Optional[datetime] = None
    strategy_family: str
    regime: str
    pnl: float = 0.0
    fees: float = 0.0
    is_complete: bool = False
    journal_refs: List[str] = Field(default_factory=list)


class StrategyAttributionRow(BaseModel):
    strategy_family: str
    trade_count: int
    pnl: float
    expectancy: float
    hit_rate: float
    drawdown_contribution: float
    cost_burden: float


class RegimeAttributionRow(BaseModel):
    regime: str
    trade_count: int
    pnl: float
    suitability_score: float


class PortfolioAttributionRow(BaseModel):
    ranking_impact: float
    concentration_impact: float
    reserve_cash_opportunity_cost: float
    total_approved: int
    total_reduced: int
    total_deferred: int
    total_rejected: int


class ExecutionQualityReport(BaseModel):
    run_id: str
    verdict: ExecutionQualityVerdict
    submit_count: int
    fill_count: int
    reject_count: int
    cancel_count: int
    avg_ack_latency_ms: float
    avg_fill_latency_ms: float
    partial_fill_rate: float


class SlippageReport(BaseModel):
    run_id: str
    avg_entry_slippage_bps: float
    avg_exit_slippage_bps: float
    symbol_slippage: Dict[str, float] = Field(default_factory=dict)


class RejectAnalysisReport(BaseModel):
    reject_count: int
    reject_reasons: Dict[str, int] = Field(default_factory=dict)


class FillQualityReport(BaseModel):
    fill_count: int
    quality_score: float


class LiveVsPaperComparison(BaseModel):
    verdict: ComparisonVerdict
    pnl_diff: float
    slippage_diff_bps: float
    fill_rate_diff: float


class BacktestVsLiveComparison(BaseModel):
    verdict: ComparisonVerdict
    pnl_diff: float
    trade_count_diff: int


class RuntimeDecisionAttribution(BaseModel):
    risk_vetoes: int
    portfolio_rejections: int


class DivergenceReport(BaseModel):
    run_id: str
    type: DivergenceType
    severity: AnomalySeverity
    evidence: str
    likely_layer: str
    recommended_checks: List[str] = Field(default_factory=list)
    live_vs_paper: Optional[LiveVsPaperComparison] = None
    backtest_vs_live: Optional[BacktestVsLiveComparison] = None


class AnomalyReport(BaseModel):
    run_id: str
    anomaly_type: str
    severity: AnomalySeverity
    timestamp: datetime
    evidence: str
    affected_symbols: List[str] = Field(default_factory=list)


class RootCauseHypothesis(BaseModel):
    hypothesis_id: str
    run_id: str
    probable_causes: List[str] = Field(default_factory=list)
    confidence: DiagnosticConfidence
    evidence_refs: List[str] = Field(default_factory=list)
    recommended_actions: List[str] = Field(default_factory=list)


class SessionAnalyticsSummary(BaseModel):
    run_id: str
    total_pnl: float
    strategy_attribution: List[StrategyAttributionRow] = Field(default_factory=list)
    regime_attribution: List[RegimeAttributionRow] = Field(default_factory=list)
    portfolio_attribution: Optional[PortfolioAttributionRow] = None
    execution_quality: Optional[ExecutionQualityReport] = None
    anomalies: List[AnomalyReport] = Field(default_factory=list)
    divergence_warnings: List[DivergenceReport] = Field(default_factory=list)
    diagnostics: List[RootCauseHypothesis] = Field(default_factory=list)


class PeriodAnalyticsSummary(BaseModel):
    granularity: PeriodGranularity
    start_time: datetime
    end_time: datetime
    total_pnl: float
    session_summaries: List[SessionAnalyticsSummary] = Field(default_factory=list)


class AnalyticsArtifactManifest(BaseModel):
    artifact_id: str
    run_id: str
    timestamp: datetime
    files: List[str] = Field(default_factory=list)


class AnalyticsAuditRecord(BaseModel):
    run_id: str
    timestamp: datetime
    action: str
    details: Dict[str, Any] = Field(default_factory=dict)


from app.analytics.enums import PeriodGranularity

class SessionSummary(BaseModel):
    run_id: str
    timestamp: datetime
    net_pnl: float
    trade_count: int
    signal_count: int
    error_count: int

class PeriodicAggregation(BaseModel):
    granularity: PeriodGranularity
    start_time: datetime
    end_time: datetime
    total_pnl: float
    session_summaries: List[SessionSummary]
