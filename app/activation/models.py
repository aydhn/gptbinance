from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime, timezone
from app.activation.enums import (
    ActivationClass,
    ActivationStage,
    ProbationVerdict,
    ExpansionVerdict,
    HaltSeverity,
    RevertClass,
    ActiveSetStatus,
)


class ActivationScope(BaseModel):
    allowed_symbols: List[str] = Field(default_factory=list)
    allowed_profiles: List[str] = Field(default_factory=list)
    allowed_sessions: List[str] = Field(default_factory=list)
    allowed_capital_tiers: List[str] = Field(default_factory=list)
    ttl_seconds: Optional[int] = None
    is_no_new_exposure: bool = False


class ActivationIntentRef(BaseModel):
    intent_id: str
    board_decision_ref: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ActivationIntent(BaseModel):
    intent_id: str
    activation_class: ActivationClass
    board_decision_ref: str
    candidate_id: str
    scope: ActivationScope
    forbidden_expansions: List[str] = Field(default_factory=list)
    probation_requirements: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ProbationMetric(BaseModel):
    metric_name: str
    value: float
    threshold: float
    is_breached: bool
    description: str


class ProbationStatus(BaseModel):
    intent_id: str
    verdict: ProbationVerdict
    metrics: List[ProbationMetric] = Field(default_factory=list)
    evaluated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    blockers: List[str] = Field(default_factory=list)


class ProbationWindow(BaseModel):
    start_time: datetime
    end_time: datetime
    required_metrics: List[str] = Field(default_factory=list)
    status: ProbationVerdict = ProbationVerdict.PENDING


class ActivationPlanStep(BaseModel):
    stage: ActivationStage
    preconditions: List[str] = Field(default_factory=list)
    success_criteria: List[str] = Field(default_factory=list)
    probation_window: Optional[ProbationWindow] = None
    halt_triggers: List[str] = Field(default_factory=list)


class ActivationPlan(BaseModel):
    intent_id: str
    steps: List[ActivationPlanStep] = Field(default_factory=list)
    current_stage: ActivationStage = ActivationStage.PREFLIGHT
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ActiveSetRecord(BaseModel):
    record_id: str
    intent_id: str
    candidate_id: str
    scope: ActivationScope
    stage: ActivationStage
    status: ActiveSetStatus = ActiveSetStatus.ACTIVE
    activated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ActiveSetSnapshot(BaseModel):
    snapshot_id: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    active_records: List[ActiveSetRecord] = Field(default_factory=list)


class ExpansionDecision(BaseModel):
    intent_id: str
    verdict: ExpansionVerdict
    recommended_stage: Optional[ActivationStage] = None
    blockers: List[str] = Field(default_factory=list)


class HaltDecision(BaseModel):
    intent_id: str
    severity: HaltSeverity
    triggers: List[str] = Field(default_factory=list)
    affected_scopes: ActivationScope


class RevertPlan(BaseModel):
    intent_id: str
    revert_class: RevertClass
    prior_active_set_ref: Optional[str] = None
    steps: List[str] = Field(default_factory=list)
    risks: List[str] = Field(default_factory=list)


class ActivationEvidenceBundle(BaseModel):
    intent_id: str
    board_decision_ref: str
    policy_proof_refs: List[str] = Field(default_factory=list)
    candidate_freeze_ref: str
    probation_evidence_refs: List[str] = Field(default_factory=list)


class ActivationMemo(BaseModel):
    intent_id: str
    rationale: str
    constraints: List[str] = Field(default_factory=list)
    next_checks: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ActivationHistoryRecord(BaseModel):
    record_id: str
    intent_id: str
    event_type: str  # e.g., "STAGE_TRANSITION", "HALT", "REVERT", "PROBATION_UPDATE"
    details: Dict[str, Any] = Field(default_factory=dict)
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class RolloutSegment(BaseModel):
    segment_id: str
    scope: ActivationScope
    stage: ActivationStage
