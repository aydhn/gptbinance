from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Dict, Optional, Any
from app.shadow_state.enums import (
    ShadowDomain,
    SnapshotSource,
    DriftType,
    DriftSeverity,
    ConvergenceVerdict,
    RemediationClass,
    TruthfulnessClass,
    ConsistencyWindow,
    SnapshotFreshness,
)


class ShadowStateConfig(BaseModel):
    enabled: bool = True
    drift_tolerance_ms: int = 5000
    stale_snapshot_threshold_s: int = 60


class SnapshotMetadata(BaseModel):
    snapshot_id: str
    source: SnapshotSource
    timestamp: datetime
    profile_id: str
    workspace_id: str
    freshness: SnapshotFreshness = SnapshotFreshness.UNKNOWN


class VenueOpenOrder(BaseModel):
    venue_order_id: str
    client_order_id: Optional[str] = None
    symbol: str
    side: str
    status: str
    qty: float
    filled_qty: float
    is_reduce_only: bool = False


class VenueOpenOrdersSnapshot(BaseModel):
    domain: ShadowDomain = ShadowDomain.ORDERS
    orders: List[VenueOpenOrder]


class VenuePosition(BaseModel):
    symbol: str
    size: float
    side: str
    mode: str
    leverage: float


class VenuePositionsSnapshot(BaseModel):
    domain: ShadowDomain = ShadowDomain.POSITIONS
    positions: List[VenuePosition]


class VenueBalance(BaseModel):
    asset: str
    free: float
    locked: float
    borrowed: float = 0.0
    interest: float = 0.0


class VenueBalancesSnapshot(BaseModel):
    domain: ShadowDomain = ShadowDomain.BALANCES
    balances: List[VenueBalance]
    collateral_locked_summary: float = 0.0


class VenueBorrowSnapshot(BaseModel):
    domain: ShadowDomain = ShadowDomain.BORROW
    liabilities: Dict[str, float]


class VenueModeSnapshot(BaseModel):
    domain: ShadowDomain = ShadowDomain.MODES
    futures_position_mode: str
    margin_mode: str


class VenueAccountSnapshot(BaseModel):
    metadata: SnapshotMetadata
    orders: VenueOpenOrdersSnapshot
    positions: VenuePositionsSnapshot
    balances: VenueBalancesSnapshot
    borrow: VenueBorrowSnapshot
    modes: VenueModeSnapshot


class LocalDerivedSnapshot(BaseModel):
    metadata: SnapshotMetadata
    active_attempts: List[Dict[str, Any]]
    ledger_balances: List[Dict[str, Any]]
    crossbook_posture: Dict[str, Any]
    risk_exposure: Dict[str, Any]
    account_mode_belief: Dict[str, Any]
    capital_refs: Dict[str, Any]
    completeness_summary: str


class ShadowTwinSnapshot(BaseModel):
    twin_id: str
    venue_truth: VenueAccountSnapshot
    local_derived: LocalDerivedSnapshot
    assembled_at: datetime


class EventualConsistencyWindow(BaseModel):
    window_type: ConsistencyWindow
    grace_period_ms: int
    is_active: bool


class DriftFinding(BaseModel):
    finding_id: str
    domain: ShadowDomain
    drift_type: DriftType
    severity: DriftSeverity
    description: str
    venue_value: Optional[Any] = None
    local_value: Optional[Any] = None
    evidence_refs: List[str] = Field(default_factory=list)
    magnitude: Optional[float] = None


class DriftCluster(BaseModel):
    cluster_id: str
    domain: ShadowDomain
    findings: List[DriftFinding]


class DriftSeveritySummary(BaseModel):
    info: int = 0
    warning: int = 0
    critical: int = 0
    blocker: int = 0


class ConvergenceResult(BaseModel):
    domain: ShadowDomain
    verdict: ConvergenceVerdict
    findings: List[DriftFinding]
    is_clean: bool


class ConvergenceRun(BaseModel):
    run_id: str
    twin_ref: str
    timestamp: datetime
    domain_results: Dict[str, ConvergenceResult]
    global_verdict: ConvergenceVerdict
    drift_summary: DriftSeveritySummary


class RemediationStep(BaseModel):
    step_id: str
    remediation_class: RemediationClass
    description: str
    required_approval: Optional[str] = None
    is_destructive: bool = False


class RemediationPlan(BaseModel):
    plan_id: str
    run_ref: str
    steps: List[RemediationStep]
    requires_review: bool = True


class TruthfulnessReport(BaseModel):
    report_id: str
    run_ref: str
    overall_class: TruthfulnessClass
    blockers: List[str]
    warnings: List[str]
    next_actions: List[str]


class ShadowAuditRecord(BaseModel):
    audit_id: str
    timestamp: datetime
    action: str
    details: str


class ShadowArtifactManifest(BaseModel):
    manifest_id: str
    twin_snapshot_id: str
    convergence_run_id: str
    remediation_plan_id: Optional[str] = None
    truthfulness_report_id: str
