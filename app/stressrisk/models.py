from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime
from app.stressrisk.enums import (
    ScenarioType,
    ShockType,
    LossSeverity,
    BudgetVerdict,
    StressOverlayVerdict,
    VulnerabilityType,
    StressSource,
    ScenarioConfidence,
)


class ShockVector(BaseModel):
    shock_type: ShockType
    value_multiplier: float = 1.0
    absolute_addition: float = 0.0
    metadata: Dict[str, Any] = Field(default_factory=dict)


class StressScenario(BaseModel):
    scenario_id: str
    name: str
    scenario_type: ScenarioType
    source: StressSource
    confidence: ScenarioConfidence
    shocks: List[ShockVector]
    applicable_profiles: List[str]
    description: str
    expected_weak_points: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class StressScenarioSet(BaseModel):
    set_id: str
    scenarios: List[StressScenario]
    description: str


class ShockedInstrumentState(BaseModel):
    symbol: str
    base_price: float
    shocked_price: float
    base_liquidity: float
    shocked_liquidity: float
    base_spread: float
    shocked_spread: float


class ScenarioLossEstimate(BaseModel):
    scenario_id: str
    symbol: str
    base_exposure: float
    estimated_loss: float
    loss_severity: LossSeverity
    cost_burden: float
    execution_deterioration_cost: float
    metadata: Dict[str, Any] = Field(default_factory=dict)


class PortfolioStressSnapshot(BaseModel):
    run_id: str
    timestamp: datetime
    total_base_value: float
    total_estimated_loss: float
    overall_severity: LossSeverity
    scenario_losses: List[ScenarioLossEstimate]
    reserve_cash_sensitivity: float


class TailLossBudget(BaseModel):
    profile: str
    max_daily_stress_loss: float
    max_scenario_loss: float
    max_concentration_loss: float


class StressBudgetResult(BaseModel):
    profile: str
    verdict: BudgetVerdict
    utilized_daily_budget_pct: float
    utilized_scenario_budget_pct: float
    reasons: List[str]


class VulnerabilityBreakdown(BaseModel):
    vulnerability_type: VulnerabilityType
    severity: LossSeverity
    description: str
    affected_symbols: List[str]
    contribution_pct: float


class CorrelationStressSnapshot(BaseModel):
    average_correlation_jump: float
    diversification_erosion_pct: float
    highly_correlated_clusters: List[List[str]]


class LiquidityStressSnapshot(BaseModel):
    average_spread_widening_pct: float
    average_turnover_drop_pct: float
    illiquid_symbols_warning: List[str]


class FundingStressSnapshot(BaseModel):
    total_funding_burden_jump: float
    borrow_cost_jump: float
    liquidation_proximity_tightening: float


class StressOverlayDecision(BaseModel):
    run_id: str
    profile: str
    verdict: StressOverlayVerdict
    reasons: List[str]
    evidence_refs: List[str]
    metadata: Dict[str, Any] = Field(default_factory=dict)


class StressFinding(BaseModel):
    finding_id: str
    severity: LossSeverity
    description: str


class StressRecommendation(BaseModel):
    action: str
    reason: str


class StressRun(BaseModel):
    run_id: str
    timestamp: datetime
    scenario_set_id: str
    profile: str
    portfolio_snapshot: PortfolioStressSnapshot
    budget_result: StressBudgetResult
    vulnerabilities: List[VulnerabilityBreakdown]
    correlation_snapshot: CorrelationStressSnapshot
    liquidity_snapshot: LiquidityStressSnapshot
    funding_snapshot: Optional[FundingStressSnapshot] = None
    overlay_decision: StressOverlayDecision
    findings: List[StressFinding]
    recommendations: List[StressRecommendation]


class TailRiskReport(BaseModel):
    run_id: str
    timestamp: datetime
    profile: str
    worst_scenario_loss: float
    worst_scenario_id: str
    budget_verdict: BudgetVerdict
    overlay_verdict: StressOverlayVerdict
    top_vulnerabilities: List[str]


class StressRiskAuditRecord(BaseModel):
    record_id: str
    timestamp: datetime
    run_id: str
    event_type: str
    details: Dict[str, Any]


class StressRiskArtifactManifest(BaseModel):
    manifest_id: str
    run_id: str
    artifacts: List[str]
