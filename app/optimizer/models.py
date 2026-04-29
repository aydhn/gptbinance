from pydantic import BaseModel, Field, root_validator
from typing import List, Dict, Any, Optional, Union
from app.optimizer.enums import (
    SearchMode,
    ParameterType,
    ObjectiveComponent,
    RankingVerdict,
    PruningVerdict,
    GuardSeverity,
    OptimizerStatus,
)
from app.backtest.models import PerformanceSummary


class ParameterSpec(BaseModel):
    name: str
    param_type: ParameterType
    bounds: Optional[List[float]] = None
    step: Optional[float] = None
    whitelist: Optional[List[Union[int, float, str]]] = None
    default_value: Union[int, float, str]
    description: Optional[str] = None

    @root_validator(pre=True, allow_reuse=True)
    def validate_spec(cls, values):
        return values


class ConstraintSpec(BaseModel):
    param1: str
    operator: str
    param2: str


class SearchSpace(BaseModel):
    name: str
    strategy_family: str
    parameters: List[ParameterSpec]
    constraints: List[ConstraintSpec] = Field(default_factory=list)


class OptimizerConfig(BaseModel):
    symbol: str
    interval: str
    start_ts: int
    end_ts: int
    feature_set: str
    strategy_family: str
    space_name: str
    max_trials: int = 40
    search_mode: SearchMode = SearchMode.GRID


class ParameterCandidate(BaseModel):
    candidate_id: str
    values: Dict[str, Union[int, float, str]]


class TrialConfig(BaseModel):
    trial_id: str
    run_id: str
    candidate: ParameterCandidate


class ObjectiveScore(BaseModel):
    total_score: float
    component_scores: Dict[str, float]
    penalties: Dict[str, float]
    rationale: str


class GuardWarning(BaseModel):
    severity: GuardSeverity
    code: str
    message: str
    recommended_handling: str
    metric: Optional[str] = None
    value: Optional[Any] = None


class OptimizationGuardReport(BaseModel):
    trial_id: str
    warnings: List[GuardWarning]
    passed_all: bool
    pruning_verdict: PruningVerdict


class TrialMetrics(BaseModel):
    expectancy: float
    profit_factor: float
    max_drawdown_pct: float
    total_trades: int
    hit_rate: float
    benchmark_relative_strength: float = 0.0


class TrialLineage(BaseModel):
    run_id: str
    trial_id: str
    candidate_id: str
    space_name: str
    generated_at: str


class TrialResult(BaseModel):
    trial_id: str
    config: TrialConfig
    backtest_summary: Optional[PerformanceSummary] = None
    validation_summary: Optional[Any] = None
    metrics: Optional[TrialMetrics] = None
    objective: Optional[ObjectiveScore] = None
    guard_report: Optional[OptimizationGuardReport] = None
    lineage: TrialLineage
    error_message: Optional[str] = None


class TrialRankingRow(BaseModel):
    trial_id: str
    rank: int
    candidate_values: Dict[str, Any]
    total_score: float
    expectancy: float
    total_trades: int
    max_drawdown_pct: float
    guard_severity: str
    verdict: RankingVerdict


class OptimizerSummary(BaseModel):
    run_id: str
    symbol: str
    interval: str
    strategy_family: str
    total_trials: int
    successful_trials: int
    failed_trials: int
    pruned_trials: int
    status: OptimizerStatus
    best_expectancy: Optional[float] = None
    created_at: str


class OptimizerSelectionResult(BaseModel):
    top_candidates: List[TrialRankingRow]
    run_id: str


class TrialArtifactManifest(BaseModel):
    run_id: str
    trial_id: str
    config: TrialConfig
    result: TrialResult
    created_at: str


class OptimizerRun(BaseModel):
    run_id: str
    config: OptimizerConfig
    space: SearchSpace
    status: OptimizerStatus
    trials: List[TrialResult] = Field(default_factory=list)
    ranking: List[TrialRankingRow] = Field(default_factory=list)
    summary: Optional[OptimizerSummary] = None
    created_at: str
    completed_at: Optional[str] = None
