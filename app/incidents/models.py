from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime, timezone
from .enums import *


class IncidentSignal(BaseModel):
    signal_id: str
    type: SignalType
    source_domain: str
    scope_type: IncidentScopeType
    scope_ref: str
    severity_hint: IncidentSeverity
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    details: Dict[str, Any] = Field(default_factory=dict)
    evidence_refs: List[str] = Field(default_factory=list)


class IncidentScope(BaseModel):
    type: IncidentScopeType
    ref: str
    blast_radius_summary: str


class IncidentSnapshot(BaseModel):
    snapshot_id: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    market_truth_refs: List[str]
    shadow_state_refs: List[str]
    lifecycle_refs: List[str]
    capital_posture_refs: List[str]
    policy_refs: List[str]
    is_complete: bool


class IncidentTimelineEvent(BaseModel):
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    event_type: str
    description: str


class ContainmentPlan(BaseModel):
    intent: ContainmentIntentType
    rationale: str
    affected_scope: IncidentScope
    recommended_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class DegradedModePlan(BaseModel):
    mode: DegradedModeType
    constraints: str
    affected_scope: IncidentScope


class RecoveryPlan(BaseModel):
    verdict: RecoveryVerdict
    unresolved_blockers: List[str]
    cleared_gates: List[str]


class PostmortemSeed(BaseModel):
    incident_id: str
    summary: str
    trigger_chain: List[str]
    frozen_evidence_refs: List[str]
    unresolved_questions: List[str]
    follow_up_seeds: List[str]


class IncidentRecord(BaseModel):
    incident_id: str
    state: IncidentState = IncidentState.OPEN
    severity: IncidentSeverity
    scope: IncidentScope
    signals: List[IncidentSignal] = Field(default_factory=list)
    timeline: List[IncidentTimelineEvent] = Field(default_factory=list)
    snapshots: List[IncidentSnapshot] = Field(default_factory=list)
    containment_plan: Optional[ContainmentPlan] = None
    degraded_mode_plan: Optional[DegradedModePlan] = None
    recovery_plan: Optional[RecoveryPlan] = None
    postmortem_seed: Optional[PostmortemSeed] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
