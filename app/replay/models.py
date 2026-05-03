from datetime import datetime
from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field

from app.replay.enums import (
    ReplayScope,
    ReplaySourceType,
    ReplayMode,
    CounterfactualType,
    DiffSeverity,
    ReplayVerdict,
    ReproducibilityStatus,
    ForensicSeverity,
    TimelineEventType,
    SnapshotFidelity,
)


class ReplaySourceRef(BaseModel):
    source_type: ReplaySourceType
    ref_id: str
    metadata: Dict[str, Any] = Field(default_factory=dict)


class ReplayWindow(BaseModel):
    start_time: datetime
    end_time: datetime


class PointInTimeSnapshot(BaseModel):
    timestamp: datetime
    bundle_id: Optional[str] = None
    model_version: Optional[str] = None
    schema_version: Optional[str] = None
    trust_verdict: Optional[str] = None
    risk_profile: Dict[str, Any] = Field(default_factory=dict)
    portfolio_state: Dict[str, Any] = Field(default_factory=dict)
    approval_state: Dict[str, Any] = Field(default_factory=dict)
    health_status: Dict[str, Any] = Field(default_factory=dict)
    fidelity: SnapshotFidelity = SnapshotFidelity.UNKNOWN
    missing_refs: List[str] = Field(default_factory=list)


class CounterfactualSpec(BaseModel):
    type: CounterfactualType
    parameters: Dict[str, Any] = Field(default_factory=dict)
    description: str


class ReplayConfig(BaseModel):
    scope: ReplayScope
    sources: List[ReplaySourceRef]
    window: Optional[ReplayWindow] = None
    mode: ReplayMode = ReplayMode.HISTORICAL
    counterfactual_specs: List[CounterfactualSpec] = Field(default_factory=dict)
    include_forensics: bool = False


class TimelineEvent(BaseModel):
    event_id: str
    timestamp: datetime
    sequence_id: int
    event_type: TimelineEventType
    component_ref: str
    payload: Dict[str, Any]
    causation_id: Optional[str] = None


class EventTimeline(BaseModel):
    events: List[TimelineEvent] = Field(default_factory=list)
    gaps_detected: bool = False
    suspicious_overlaps: bool = False
    missing_refs: List[str] = Field(default_factory=list)
    source_coverage: float = 0.0


class DecisionPathSnapshot(BaseModel):
    stage: str
    timestamp: datetime
    inputs: Dict[str, Any]
    decision: Dict[str, Any]
    evidence_refs: List[str] = Field(default_factory=list)


class ReplayDiff(BaseModel):
    stage: str
    original_value: Any
    replayed_value: Any
    severity: DiffSeverity
    description: str
    numerical_delta: Optional[float] = None
    evidence_refs: List[str] = Field(default_factory=list)


class ReplayabilityScore(BaseModel):
    source_completeness: float
    lineage_completeness: float
    snapshot_fidelity: float
    schema_compatibility: float
    decision_path_coverage: float
    diff_magnitude: float
    deterministic_reproducibility: float
    forensic_evidence_completeness: float
    overall_score: float
    verdict: ReplayVerdict
    blockers: List[str] = Field(default_factory=list)
    next_actions: List[str] = Field(default_factory=list)


class ReproducibilityVerdict(BaseModel):
    status: ReproducibilityStatus
    confidence: float
    reasoning: str


class CounterfactualResult(BaseModel):
    spec: CounterfactualSpec
    historical_outcome: Dict[str, Any]
    counterfactual_outcome: Dict[str, Any]
    diffs: List[ReplayDiff]
    explanation: str


class ReplayFinding(BaseModel):
    severity: ForensicSeverity
    description: str
    layer: str
    evidence_refs: List[str]


class ForensicBundle(BaseModel):
    incident_ref: Optional[str]
    timeline: EventTimeline
    decision_path: List[DecisionPathSnapshot]
    findings: List[ReplayFinding]
    likely_root_causes: List[str]
    next_investigation_steps: List[str]


class ReplayEvidenceRef(BaseModel):
    ref_id: str
    type: str
    uri: str


class DecisionReplayResult(BaseModel):
    run_id: str
    config: ReplayConfig
    snapshot: PointInTimeSnapshot
    timeline: EventTimeline
    decision_path: List[DecisionPathSnapshot]
    diffs: List[ReplayDiff]
    reproducibility: ReproducibilityVerdict
    counterfactual_results: List[CounterfactualResult] = Field(default_factory=list)
    forensic_bundle: Optional[ForensicBundle] = None
    replayability_score: ReplayabilityScore


class ReplayAuditRecord(BaseModel):
    run_id: str
    timestamp: datetime
    config: ReplayConfig
    verdict: ReproducibilityVerdict
    has_critical_diffs: bool


class ReplayArtifactManifest(BaseModel):
    run_id: str
    artifacts: List[ReplayEvidenceRef]


class ReplayRun(BaseModel):
    run_id: str
    timestamp: datetime
    config: ReplayConfig
    result: Optional[DecisionReplayResult] = None
    status: str
