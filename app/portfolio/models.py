
from app.products.enums import ProductType
from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime
from app.portfolio.enums import (
    AllocationMode,
    PortfolioVerdict,
    SleeveType,
    OpportunityStatus,
    RankingReason,
    ConcentrationSeverity,
    CorrelationRegime,
    OverlapType,
    BudgetScope,
)

# We need to import intent models from risk/execution.
# We'll use a generic forward reference or import SimulatedOrderIntent.
from app.backtest.models import SimulatedOrderIntent


class PortfolioConfig(BaseModel):
    allocation_mode: AllocationMode = AllocationMode.CONSERVATIVE
    total_budget: float = 1000.0
    reserve_cash_ratio: float = 0.20
    max_symbol_weight: float = 0.25
    max_strategy_sleeve_weight: float = 0.50
    max_correlated_cluster_weight: float = 0.40
    max_new_allocations_per_cycle: int = 5
    live_rollout_mode: str = "paper"


class CorrelationSnapshot(BaseModel):
    timestamp: datetime
    correlations: Dict[str, Dict[str, float]] = Field(default_factory=dict)
    clusters: Dict[str, List[str]] = Field(default_factory=dict)
    regime: CorrelationRegime = CorrelationRegime.NORMAL
    data_quality_stable: bool = True
    notes: str = ""


class OverlapReport(BaseModel):
    intent_id: str
    overlap_type: OverlapType = OverlapType.NONE
    overlapping_symbols: List[str] = Field(default_factory=list)
    overlap_severity_score: float = 0.0


class ConcentrationSnapshot(BaseModel):
    timestamp: datetime
    symbol_concentration: Dict[str, float] = Field(default_factory=dict)
    strategy_concentration: Dict[str, float] = Field(default_factory=dict)
    quote_concentration: Dict[str, float] = Field(default_factory=dict)
    directional_concentration: Dict[str, float] = Field(default_factory=dict)
    cluster_concentration: Dict[str, float] = Field(default_factory=dict)
    severity: ConcentrationSeverity = ConcentrationSeverity.NORMAL
    breaches: List[str] = Field(default_factory=list)


class PortfolioBudgetSnapshot(BaseModel):
    timestamp: datetime
    total_capital: float
    reserved_capital: float
    available_capital: float
    pending_allocations_notional: float


class StrategySleeve(BaseModel):
    strategy_family: str
    budget_notional: float
    used_notional: float
    is_throttled: bool = False


class SymbolSleeve(BaseModel):
    symbol: str
    budget_notional: float
    used_notional: float
    is_throttled: bool = False


class PortfolioExposureSnapshot(BaseModel):
    timestamp: datetime
    total_exposure: float
    long_exposure: float
    short_exposure: float


class PortfolioContext(BaseModel):
    timestamp: datetime
    budget: PortfolioBudgetSnapshot
    exposure: PortfolioExposureSnapshot
    correlation: CorrelationSnapshot
    concentration: ConcentrationSnapshot
    strategy_sleeves: Dict[str, StrategySleeve] = Field(default_factory=dict)
    symbol_sleeves: Dict[str, SymbolSleeve] = Field(default_factory=dict)


class PortfolioState(BaseModel):
    last_updated: datetime
    context: PortfolioContext


class PortfolioIntentBatch(BaseModel):
    timestamp: datetime
    run_id: str
    risk_approved_intents: List[Any] = Field(default_factory=list)
    # The output from risk engine that goes into portfolio engine


class OpportunityRank(BaseModel):
    intent_id: str
    score: float
    primary_reason: RankingReason = RankingReason.DEFAULT
    penalty_breakdown: Dict[str, float] = Field(default_factory=dict)
    rationale: str = ""


class PortfolioCandidate(BaseModel):
    intent: Any
    status: OpportunityStatus = OpportunityStatus.PENDING
    rank: Optional[OpportunityRank] = None
    overlap_report: Optional[OverlapReport] = None


class AllocationSlice(BaseModel):
    intent_id: str
    approved_notional: float
    requested_notional: float
    reduction_ratio: float


class PortfolioDecision(BaseModel):
    intent_id: str
    verdict: PortfolioVerdict
    original_intent: Any
    approved_intent: Optional[SimulatedOrderIntent] = None
    allocation: Optional[AllocationSlice] = None
    blocking_reasons: List[str] = Field(default_factory=list)
    rationale: str = ""


class PortfolioDecisionBatch(BaseModel):
    timestamp: datetime
    run_id: str
    decisions: List[PortfolioDecision] = Field(default_factory=list)


class AllocationRequest(BaseModel):
    candidate: PortfolioCandidate
    context: PortfolioContext


class AllocationResult(BaseModel):
    decision: PortfolioDecision


class PortfolioAuditRecord(BaseModel):
    timestamp: datetime
    run_id: str
    intent_id: str
    symbol: str
    verdict: PortfolioVerdict
    requested_notional: float
    approved_notional: float
    rationale: str


class PortfolioSummary(BaseModel):
    timestamp: datetime
    run_id: str
    total_intents_evaluated: int
    total_approved: int
    total_reduced: int
    total_deferred: int
    total_rejected: int
    total_allocated_notional: float
    concentration_severity: ConcentrationSeverity


class PortfolioArtifactManifest(BaseModel):
    timestamp: datetime
    run_id: str
    summary: PortfolioSummary
    decisions: List[PortfolioDecision] = Field(default_factory=list)

class AssetAllocation(BaseModel):
    symbol: str
    product_type: ProductType = ProductType.SPOT
    notional_exposure: float
    leveraged_exposure: float = 0.0 # Gross exposure (notional * leverage)
    target_weight: float

class PortfolioSnapshot(BaseModel):
    total_capital: float
    allocations: Dict[str, AssetAllocation] = Field(default_factory=dict)
    total_leveraged_exposure: float = 0.0
