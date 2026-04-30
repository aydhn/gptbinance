from typing import List, Dict, Optional, Any
from pydantic import BaseModel, Field
from datetime import datetime, timezone
from app.governance.enums import (
    RefreshTriggerType,
    BundleType,
    BundleStage,
    DecaySeverity,
    DegradationType,
    RollbackStatus,
    GovernanceVerdict,
    PromotionReadiness,
)


class GovernanceConfig(BaseModel):
    max_active_bundles: int = 1
    require_rollback_ref: bool = True
    decay_threshold_severity: DecaySeverity = DecaySeverity.MEDIUM


class RefreshTrigger(BaseModel):
    trigger_type: RefreshTriggerType
    source: str
    details: Dict[str, Any] = Field(default_factory=dict)
    triggered_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class RefreshPlan(BaseModel):
    name: str
    components: List[str]
    is_deep: bool = False
    risk_level: str = "low"


class RefreshRun(BaseModel):
    run_id: str
    plan: RefreshPlan
    trigger: RefreshTrigger
    started_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    status: str = "running"


class DecayReport(BaseModel):
    report_id: str
    bundle_id: str
    degradation_type: DegradationType
    severity: DecaySeverity
    evidence: Dict[str, Any]
    recommended_actions: List[str]
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class DegradationSignal(BaseModel):
    signal_type: DegradationType
    severity: DecaySeverity
    details: Dict[str, Any]


class CandidateBundleSpec(BaseModel):
    strategy_preset_refs: List[str] = Field(default_factory=list)
    model_refs: List[str] = Field(default_factory=list)
    feature_set_refs: List[str] = Field(default_factory=list)
    risk_profile_refs: List[str] = Field(default_factory=list)
    portfolio_profile_refs: List[str] = Field(default_factory=list)


class CandidateBundleVersion(BaseModel):
    major: int
    minor: int
    patch: int

    def __str__(self):
        return f"{self.major}.{self.minor}.{self.patch}"


class BundleLineage(BaseModel):
    parent_bundle_id: Optional[str]
    refresh_run_id: str
    creation_reason: str


class RollbackReference(BaseModel):
    bundle_id: str
    status: RollbackStatus
    known_good_since: datetime


class BundleStageState(BaseModel):
    stage: BundleStage
    entered_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    notes: str = ""


class CandidateBundle(BaseModel):
    bundle_id: str
    bundle_type: BundleType
    version: CandidateBundleVersion
    spec: CandidateBundleSpec
    lineage: BundleLineage
    stage_state: BundleStageState
    rollback_ref: Optional[RollbackReference] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class PromotionCandidateReport(BaseModel):
    bundle_id: str
    readiness: PromotionReadiness
    stage_recommendation: BundleStage
    blockers: List[str]
    warnings: List[str]
    next_actions: List[str]
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class GovernanceAuditRecord(BaseModel):
    record_id: str
    action: str
    bundle_id: Optional[str] = None
    details: Dict[str, Any]
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ActivationReadinessReport(BaseModel):
    bundle_id: str
    target_mode: str
    is_ready: bool
    checks: Dict[str, bool]
    warnings: List[str]


class RefreshArtifactManifest(BaseModel):
    run_id: str
    artifacts: List[str]


class RefreshSummary(BaseModel):
    run_id: str
    status: str
    components_refreshed: List[str]
    new_bundles: List[str]
    decay_reports: List[str]
    completed_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class RefreshResult(BaseModel):
    run_id: str
    summary: RefreshSummary
    manifest: RefreshArtifactManifest
