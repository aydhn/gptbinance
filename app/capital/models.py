from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime
from app.capital.enums import (
    CapitalTierClass,
    CapitalPostureState,
    EscalationVerdict,
    ReductionVerdict,
    FreezeStatus,
    BudgetSeverity,
    EvidenceFreshness,
    LossWindow,
    CapitalDecisionClass,
    ScopeType,
)


class LossBudget(BaseModel):
    window: LossWindow
    max_loss_amount: float = Field(..., ge=0.0)
    severity: BudgetSeverity = BudgetSeverity.HARD


class ExposureBudget(BaseModel):
    max_concurrent_positions: int = Field(..., ge=1)
    max_symbol_concentration: float = Field(..., ge=0.0, le=1.0)
    max_leverage: float = Field(..., ge=1.0)
    loss_budgets: List[LossBudget] = Field(default_factory=list)
    max_deployable_capital: float = Field(..., ge=0.0)
    correlated_cluster_exposure_cap: float = Field(..., ge=0.0, le=1.0)


class CapitalTier(BaseModel):
    id: str
    name: str
    tier_class: CapitalTierClass
    budget: ExposureBudget
    allowed_product_types: List[str]
    requires_approval: bool = True
    required_evidence_types: List[str] = Field(default_factory=list)


class CapitalTierRef(BaseModel):
    tier_id: str
    assigned_at: datetime


class CapitalTranche(BaseModel):
    tranche_id: str
    size_amount: float = Field(..., ge=0.0)
    required_conditions: List[str] = Field(default_factory=list)


class CapitalTrancheActivation(BaseModel):
    tranche_id: str
    activated_at: datetime
    active: bool = True
    deactivated_at: Optional[datetime] = None


class CapitalLadder(BaseModel):
    ladder_id: str
    tiers: List[CapitalTier]
    allowed_transitions: Dict[str, List[str]]  # from tier_id -> [allowed next tier_ids]
    downgrade_paths: Dict[
        str, List[str]
    ]  # from tier_id -> [allowed downgrade tier_ids]


class CapitalReadinessReport(BaseModel):
    is_ready: bool
    verdict: EscalationVerdict
    blockers: List[str] = Field(default_factory=list)
    warnings: List[str] = Field(default_factory=list)
    next_tier_recommendation: Optional[str] = None


class CapitalEscalationCheck(BaseModel):
    check_id: str
    timestamp: datetime
    current_tier_id: str
    target_tier_id: str
    readiness: CapitalReadinessReport


class CapitalReductionCheck(BaseModel):
    check_id: str
    timestamp: datetime
    current_tier_id: str
    verdict: ReductionVerdict
    reasons: List[str] = Field(default_factory=list)


class CapitalFreezeState(BaseModel):
    status: FreezeStatus
    frozen_at: Optional[datetime] = None
    reasons: List[str] = Field(default_factory=list)
    thaw_prerequisites: List[str] = Field(default_factory=list)


class CapitalPostureSnapshot(BaseModel):
    snapshot_id: str
    timestamp: datetime
    active_tier_id: str
    posture_state: CapitalPostureState
    deployed_capital: float
    reserved_capital: float
    frozen_capital: float
    available_headroom: float
    active_tranches: List[CapitalTrancheActivation] = Field(default_factory=list)
    budget_utilization: Dict[str, float] = Field(default_factory=dict)


class CapitalEvidenceBundle(BaseModel):
    bundle_id: str
    timestamp: datetime
    evidence_refs: Dict[str, str] = Field(default_factory=dict)
    freshness: EvidenceFreshness
    missing_items: List[str] = Field(default_factory=list)


class CapitalDecisionReason(BaseModel):
    reason_code: str
    description: str


class CapitalDecision(BaseModel):
    decision_id: str
    timestamp: datetime
    decision_class: CapitalDecisionClass
    verdict: str
    reasons: List[CapitalDecisionReason] = Field(default_factory=list)


class ScaleTransitionPlan(BaseModel):
    plan_id: str
    current_tier_id: str
    target_tier_id: str
    is_upgrade: bool
    required_approvals: List[str] = Field(default_factory=list)
    required_checks: List[str] = Field(default_factory=list)
    safe_activation_order: List[str] = Field(default_factory=list)
    dry_run_summary: Dict[str, Any] = Field(default_factory=dict)


class CapitalGovernanceConfig(BaseModel):
    ladder_enabled: bool = True
    enforce_evidence_freshness: bool = True
    stale_evidence_timeout_minutes: int = 60


class CapitalGuardResult(BaseModel):
    passed: bool
    reasons: List[str] = Field(default_factory=list)


class CapitalAuditRecord(BaseModel):
    audit_id: str
    timestamp: datetime
    action: str
    actor: str
    details: Dict[str, Any] = Field(default_factory=dict)


class CapitalArtifactManifest(BaseModel):
    manifest_id: str
    created_at: datetime
    artifacts: List[str] = Field(default_factory=list)
