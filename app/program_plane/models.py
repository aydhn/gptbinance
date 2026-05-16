from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
from app.program_plane.enums import (
    ProgramClass, MilestoneClass, DeliverableClass, DependencyClass, BlockerClass,
    HandoffClass, CadenceClass, SlipClass, EscalationClass, EquivalenceVerdict, TrustVerdict
)

class ProgramPlaneConfig(BaseModel):
    enabled: bool = True
    strict_acceptance: bool = True

class ProgramObjectRef(BaseModel):
    program_id: str
    milestone_id: Optional[str] = None
    deliverable_id: Optional[str] = None

class ProgramObject(BaseModel):
    program_id: str
    program_class: ProgramClass
    owner: str
    scope: str
    delivery_class: str

class ProgramRecord(BaseModel):
    program_id: str
    program_class: ProgramClass
    owner: str
    scope: str
    delivery_class: str
    target_horizon: str
    delivery_intent: str
    lifecycle_state: str
    lineage_refs: List[str] = Field(default_factory=list)

class MilestoneRecord(BaseModel):
    milestone_id: str
    program_id: str
    milestone_class: MilestoneClass
    completion_criteria: str
    is_completed: bool = False
    acceptance_posture: str = "pending"

class DeliverableRecord(BaseModel):
    deliverable_id: str
    milestone_id: str
    deliverable_class: DeliverableClass
    acceptance_criteria: str
    proof_notes: Optional[str] = None

class DependencyEdge(BaseModel):
    dependency_id: str
    source_id: str
    target_id: str
    dependency_class: DependencyClass
    is_accepted: bool = False

class BlockerRecord(BaseModel):
    blocker_id: str
    program_id: str
    blocker_class: BlockerClass
    severity: str
    age_seconds: int = 0
    is_resolved: bool = False

class HandoffRecord(BaseModel):
    handoff_id: str
    source_program_id: str
    target_program_id: str
    handoff_class: HandoffClass
    state: str = "requested"
    cross_team_notes: Optional[str] = None

class AcceptanceRecord(BaseModel):
    acceptance_id: str
    deliverable_id: str
    state: str = "pending"
    rejection_reasons: List[str] = Field(default_factory=list)

class CriticalPathReport(BaseModel):
    report_id: str
    program_id: str
    path_nodes: List[str]
    path_confidence: float
    near_critical_items: List[str] = Field(default_factory=list)
    path_drift: bool = False
    proof_notes: Optional[str] = None

class SlackRecord(BaseModel):
    slack_id: str
    program_id: str
    milestone_slack_days: int
    dependency_slack_days: int
    zero_slack_warnings: List[str] = Field(default_factory=list)
    lineage_refs: List[str] = Field(default_factory=list)

class CadenceRecord(BaseModel):
    cadence_id: str
    program_id: str
    cadence_class: CadenceClass
    misses: int = 0
    proof_notes: Optional[str] = None

class CommitmentWindow(BaseModel):
    window_id: str
    program_id: str
    target_by: datetime
    must_land_by: datetime
    canary_window: Optional[datetime] = None
    activation_window: Optional[datetime] = None
    is_rebaselined: bool = False
    proof_notes: Optional[str] = None

class SlippageRecord(BaseModel):
    slippage_id: str
    program_id: str
    slip_class: SlipClass
    cascading_slip: bool = False
    deadline_miss: bool = False
    root_cause_refs: List[str] = Field(default_factory=list)

class ReplanRecord(BaseModel):
    replan_id: str
    program_id: str
    scope_preserving: bool
    capacity_driven: bool
    is_accepted: bool = False
    lineage_refs: List[str] = Field(default_factory=list)

class EscalationRecord(BaseModel):
    escalation_id: str
    program_id: str
    escalation_class: EscalationClass
    is_resolved: bool = False
    freshness_seconds: int = 0

class StaffingRealityRecord(BaseModel):
    staffing_id: str
    program_id: str
    nominal_staffing: int
    effective_staffing: int
    owner_gap: bool = False
    reviewer_bottleneck: bool = False
    staffing_drift: bool = False

class DeliveryRiskRecord(BaseModel):
    risk_id: str
    program_id: str
    risk_type: str
    mitigation_notes: Optional[str] = None

class ProgramForecastReport(BaseModel):
    forecast_id: str
    program_id: str
    completion_forecast_days: int
    uncertainty_class: str

class ProgramVarianceRecord(BaseModel):
    variance_id: str
    program_id: str
    plan_vs_actual_days: int
    variance_proof_notes: Optional[str] = None

class ProgramDebtRecord(BaseModel):
    debt_id: str
    program_id: str
    stale_blocker_debt: bool = False
    replan_debt: bool = False
    fake_complete_debt: bool = False
    handoff_churn_debt: bool = False
    debt_severity: str

class ProgramEquivalenceReport(BaseModel):
    report_id: str
    program_id: str
    replay_equivalent: bool
    paper_equivalent: bool
    live_equivalent: bool
    verdict: EquivalenceVerdict
    divergence_sources: List[str] = Field(default_factory=list)

class ProgramDivergenceReport(BaseModel):
    divergence_id: str
    program_id: str
    divergence_severity: str
    blast_radius: str

class ProgramTrustVerdict(BaseModel):
    verdict_id: str
    program_id: str
    verdict: TrustVerdict
    breakdown: Dict[str, Any] = Field(default_factory=dict)

class ProgramAuditRecord(BaseModel):
    audit_id: str
    program_id: str
    action: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class ProgramArtifactManifest(BaseModel):
    manifest_id: str
    program_id: str
    artifact_hash: str
