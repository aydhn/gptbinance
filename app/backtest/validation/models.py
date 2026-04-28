from pydantic import BaseModel, Field
from typing import Dict, List, Optional, Any
from datetime import datetime
from uuid import UUID, uuid4

from app.backtest.validation.enums import (
    BenchmarkType,
    ComparisonVerdict,
    AblationType,
    RobustnessCheckType,
    SampleSplitType,
    HonestySeverity,
    ValidationStatus,
)
from app.backtest.models import PerformanceSummary as BacktestSummary


class BaselineStrategyDescriptor(BaseModel):
    name: str
    benchmark_type: BenchmarkType
    description: str


class BenchmarkSpec(BaseModel):
    benchmark_id: UUID = Field(default_factory=uuid4)
    run_id: UUID  # the run_id of the baseline it's comparing to
    benchmark_type: BenchmarkType
    baseline_descriptor: BaselineStrategyDescriptor


class BenchmarkResult(BaseModel):
    spec: BenchmarkSpec
    summary: BacktestSummary
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ComparisonMetricRow(BaseModel):
    metric_name: str
    strategy_value: float
    benchmark_value: float
    absolute_diff: float
    relative_diff_pct: float
    is_better: bool


class ComparisonResult(BaseModel):
    strategy_run_id: UUID
    benchmark_run_id: UUID
    metrics: List[ComparisonMetricRow]
    verdict: ComparisonVerdict
    caveat: Optional[str] = None


class AblationSpec(BaseModel):
    ablation_type: AblationType
    description: str
    toggled_features: Dict[str, bool]


class AblationResult(BaseModel):
    spec: AblationSpec
    summary: BacktestSummary
    comparison_to_base: ComparisonResult


class RobustnessCheckResult(BaseModel):
    check_type: RobustnessCheckType
    description: str
    is_fragile: bool
    details: Dict[str, Any]


class SampleWindow(BaseModel):
    start_ts: int
    end_ts: int
    split_type: SampleSplitType
    description: Optional[str] = None


class SampleSplitPlan(BaseModel):
    plan_id: UUID = Field(default_factory=uuid4)
    symbol: str
    interval: str
    windows: List[SampleWindow]


class HonestyWarning(BaseModel):
    severity: HonestySeverity
    message: str
    metric: str
    value: Any


class ResearchHonestyReport(BaseModel):
    strategy_run_id: UUID
    warnings: List[HonestyWarning]
    passed_all: bool


class ValidationArtifactManifest(BaseModel):
    benchmark_run_ids: List[UUID]
    comparison_ids: List[UUID]
    ablation_run_ids: List[UUID]
    robustness_ids: List[UUID]
    honesty_report_id: Optional[UUID] = None


class ValidationSummary(BaseModel):
    validation_id: UUID = Field(default_factory=uuid4)
    strategy_run_id: UUID
    status: ValidationStatus
    benchmarks: List[BenchmarkResult]
    comparisons: List[ComparisonResult]
    ablations: List[AblationResult]
    robustness_checks: List[RobustnessCheckResult]
    honesty_report: Optional[ResearchHonestyReport] = None
    artifact_manifest: ValidationArtifactManifest
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ValidationSuiteConfig(BaseModel):
    benchmark_types: List[BenchmarkType]
    ablation_types: List[AblationType]
    robustness_types: List[RobustnessCheckType]
    enable_honesty_guards: bool = True
