from pydantic import BaseModel, Field
from typing import Dict, Any, List, Optional
from datetime import datetime, timezone
import uuid

from app.execution_plane.enums import (
    VenueClass,
    ProductClass,
    ExecutionClass,
    RoutingClass,
    OrderType,
    TIFClass,
    FillQualityClass,
    SlippageSeverityClass,
    EquivalenceVerdictClass,
    TrustedExecutionVerdictClass,
)


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class ExecutionPlaneConfig(BaseModel):
    is_live: bool = False
    default_venue_class: VenueClass = VenueClass.PAPER
    max_slippage_bps: float = 50.0
    require_equivalence_check: bool = True
    default_retry_budget: int = 3


class VenueConstraint(BaseModel):
    constraint_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    min_notional: float
    min_qty: float
    step_size: float
    tick_size: float
    price_band_pct: float
    reduce_only_allowed: bool
    margin_modes_allowed: List[str]
    is_fresh: bool
    evidence_ref: str


class VenueDefinition(BaseModel):
    venue_id: str
    venue_class: VenueClass
    product_class: ProductClass
    constraints: VenueConstraint
    is_active: bool = True
    metadata: Dict[str, Any] = Field(default_factory=dict)


class ExecutionCandidateRef(BaseModel):
    candidate_id: str
    allocation_intent_id: str


class ExecutionCandidate(BaseModel):
    candidate_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    allocation_intent_id: str
    symbol: str
    target_size: float
    side: str
    is_reduce_only: bool
    venue_eligibility: List[str]
    instrument_compatibility: bool
    size_viable: bool
    reject_reason: Optional[str] = None
    defer_reason: Optional[str] = None
    created_at: datetime = Field(default_factory=utc_now)


class OrderSpecRef(BaseModel):
    spec_id: str


class OrderSpec(BaseModel):
    spec_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    candidate_id: str
    venue_id: str
    symbol: str
    side: str
    order_type: OrderType
    tif: TIFClass
    qty: float
    price: Optional[float] = None
    stop_price: Optional[float] = None
    is_post_only: bool = False
    is_reduce_only: bool = False
    client_order_id: str
    created_at: datetime = Field(default_factory=utc_now)


class RoutingPolicy(BaseModel):
    routing_class: RoutingClass
    urgency: str
    rationale: str
    max_slippage_bps: float


class SlicePlan(BaseModel):
    slice_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    total_qty: float
    slice_count: int
    min_viable_slice: float
    time_spacing_ms: int
    rationale: str
    lineage_ref: str


class ExecutionPlanEntry(BaseModel):
    entry_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    candidate_id: str
    order_spec: OrderSpec
    routing_policy: RoutingPolicy
    slice_plan: Optional[SlicePlan] = None
    guard_refs: List[str] = Field(default_factory=list)


class ExecutionPlan(BaseModel):
    plan_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    source_allocation_intent_id: str
    entries: List[ExecutionPlanEntry]
    venue_scope: List[str]
    created_at: datetime = Field(default_factory=utc_now)


class SendAttempt(BaseModel):
    attempt_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    spec_id: str
    idempotency_key: str
    venue_id: str
    sent_at: datetime = Field(default_factory=utc_now)
    is_successful: bool
    reject_reason: Optional[str] = None
    receipt_ref: Optional[str] = None


class IdempotencyRecord(BaseModel):
    record_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    idempotency_key: str
    intent_ref: str
    created_at: datetime = Field(default_factory=utc_now)
    retry_window_ms: int
    is_stale: bool = False
    audit_ref: str


class CancelReplaceChain(BaseModel):
    chain_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    original_spec_id: str
    replaced_spec_ids: List[str] = Field(default_factory=list)
    is_ambiguous: bool = False
    stale_reason: Optional[str] = None
    lineage_ref: str


class FillQualityReport(BaseModel):
    report_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    spec_id: str
    fill_qty: float
    total_qty: float
    avg_price: float
    maker_taker_mix: Dict[str, float]
    quality_class: FillQualityClass
    anomalies: List[str] = Field(default_factory=list)


class SlippageReport(BaseModel):
    report_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    spec_id: str
    expected_slippage_bps: float
    realized_slippage_bps: float
    severity: SlippageSeverityClass
    evidence_ref: str


class MarkoutReport(BaseModel):
    report_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    spec_id: str
    window_ms: int
    markout_bps: float
    is_favorable: bool
    lineage_ref: str


class ExecutionDiffRecord(BaseModel):
    diff_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    baseline_manifest_id: str
    candidate_manifest_id: str
    divergence_reason: str


class ExecutionEquivalenceReport(BaseModel):
    report_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    runtime_manifest_id: str
    replay_manifest_id: str
    verdict: EquivalenceVerdictClass
    blockers: List[str] = Field(default_factory=list)
    proof_notes: str


class TrustedExecutionVerdict(BaseModel):
    verdict_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    manifest_id: str
    verdict: TrustedExecutionVerdictClass
    factors: Dict[str, str] = Field(default_factory=dict)
    breakdown: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=utc_now)


class ExecutionAuditRecord(BaseModel):
    audit_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    action: str
    ref_id: str
    details: Dict[str, Any]
    created_at: datetime = Field(default_factory=utc_now)


class ExecutionArtifactManifest(BaseModel):
    manifest_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    plan_id: str
    order_specs: List[OrderSpecRef]
    routing_refs: List[str]
    slice_refs: List[str]
    filter_refs: List[str]
    idempotency_refs: List[str]
    guard_refs: List[str]
    hash_signature: str
    lineage_ref: str
    created_at: datetime = Field(default_factory=utc_now)
