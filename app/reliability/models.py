from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime, timezone
from app.reliability.enums import (
    ReliabilityDomain,
    SLOClass,
    BudgetClass,
    BurnSeverity,
    ReadinessDecayClass,
    ScorecardVerdict,
    FreezeClass,
    OperationalReviewClass,
    TrendClass,
    ReliabilityVerdict,
)


class ReliabilityTowerConfig(BaseModel):
    version: str = "1.0.0"
    enable_freeze_recommendations: bool = True


class ReliabilityDomainModel(BaseModel):
    name: ReliabilityDomain
    owner: str
    rationale: str
    evidence_requirements: List[str] = []


class SLOTarget(BaseModel):
    target_value: float
    is_upper_bound: bool = (
        True  # e.g. latency is upper bound, uptime is lower bound (False)
    )
    unit: str


class SLOWindow(BaseModel):
    window_id: str
    duration_seconds: int
    window_type: str = "rolling"


class SLODefinition(BaseModel):
    slo_id: str
    domain: ReliabilityDomain
    slo_class: SLOClass
    name: str
    description: str
    target: SLOTarget
    windows: List[SLOWindow]


class ErrorBudget(BaseModel):
    budget_id: str
    slo_id: str
    budget_class: BudgetClass
    total_budget_value: float
    remaining_budget: float


class ErrorBudgetConsumption(BaseModel):
    consumption_id: str
    budget_id: str
    consumed_value: float
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    rationale: str


class BurnRateReport(BaseModel):
    report_id: str
    budget_id: str
    short_window_burn_rate: float
    long_window_burn_rate: float
    severity: BurnSeverity
    projected_exhaustion_hours: Optional[float] = None
    caveats: List[str] = []


class ReadinessDecayRecord(BaseModel):
    record_id: str
    domain: ReliabilityDomain
    decay_class: ReadinessDecayClass
    severity_score: float
    evidence_ref: str
    description: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class HealthScorecard(BaseModel):
    scorecard_id: str
    domain: ReliabilityDomain
    verdict: ScorecardVerdict
    blockers: List[str] = []
    caveats: List[str] = []
    evidence_refs: List[str] = []
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class DomainHealthSummary(BaseModel):
    scorecards: Dict[str, HealthScorecard]
    overall_verdict: ScorecardVerdict


class FreezeRecommendation(BaseModel):
    recommendation_id: str
    freeze_class: FreezeClass
    scope: str
    rationale: str
    budget_evidence_refs: List[str] = []
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class HoldRecommendation(BaseModel):
    hold_id: str
    hold_class: OperationalReviewClass
    scope: str
    rationale: str
    expiry_conditions: List[str] = []
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class OperationalReviewRecord(BaseModel):
    review_id: str
    hold_id: str
    decision: ReliabilityVerdict
    notes: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class OperationalCadenceArtifact(BaseModel):
    artifact_id: str
    artifact_type: str  # daily_digest, weekly_review, probation_checkpoint
    domain_summary: DomainHealthSummary
    burn_reports: List[BurnRateReport] = []
    decay_records: List[ReadinessDecayRecord] = []
    freeze_recommendations: List[FreezeRecommendation] = []
    hold_recommendations: List[HoldRecommendation] = []
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ReliabilityTrendReport(BaseModel):
    trend_id: str
    domain: ReliabilityDomain
    trend_class: TrendClass
    repeated_failure_families: List[str] = []
    caveats: List[str] = []
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ReliabilityEvidenceBundle(BaseModel):
    bundle_id: str
    metrics: Dict[str, Any]
    scorecards: List[HealthScorecard]
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ReliabilityAuditRecord(BaseModel):
    audit_id: str
    action: str
    actor: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ReliabilityArtifactManifest(BaseModel):
    manifest_id: str
    artifacts: List[str]
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
