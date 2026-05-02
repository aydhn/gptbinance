from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime
from app.resilience.enums import (
    ExperimentType,
    FaultType,
    TargetComponent,
    StressType,
    AssertionVerdict,
    ResilienceSeverity,
    GateVerdict,
    DegradationMode,
    ExperimentStatus,
    SafeScope,
)


class TargetComponentRef(BaseModel):
    component: TargetComponent
    identifier: Optional[str] = None


class FaultInjectionSpec(BaseModel):
    fault_type: FaultType
    target: TargetComponentRef
    duration_ms: int = Field(..., gt=0)
    parameters: Dict[str, Any] = Field(default_factory=dict)


class StressSpec(BaseModel):
    stress_type: StressType
    target: TargetComponentRef
    duration_ms: int = Field(..., gt=0)
    parameters: Dict[str, Any] = Field(default_factory=dict)


class AssertionSpec(BaseModel):
    id: str
    description: str
    expected_behavior: str
    timeout_ms: int = Field(..., gt=0)
    critical: bool = True


class ExperimentDefinition(BaseModel):
    id: str
    name: str
    description: str
    experiment_type: ExperimentType
    allowed_scopes: List[SafeScope]
    target_components: List[TargetComponentRef]
    fault_specs: List[FaultInjectionSpec] = Field(default_factory=list)
    stress_specs: List[StressSpec] = Field(default_factory=list)
    assertions: List[AssertionSpec]
    recovery_assertions: List[AssertionSpec]
    expected_degradation_mode: DegradationMode


class ExperimentScope(BaseModel):
    safe_scope: SafeScope
    environment: str
    is_live_mainnet: bool


class ExperimentGateReport(BaseModel):
    verdict: GateVerdict
    reason: str
    blocked_by: Optional[str] = None


class AssertionResult(BaseModel):
    spec_id: str
    verdict: AssertionVerdict
    message: str
    evaluated_at: datetime
    evidence_refs: List[str] = Field(default_factory=list)


class RecoveryAssertion(BaseModel):
    spec_id: str
    verdict: AssertionVerdict
    message: str
    evaluated_at: datetime
    evidence_refs: List[str] = Field(default_factory=list)


class ChaosEventRecord(BaseModel):
    event_id: str
    timestamp: datetime
    event_type: str
    details: Dict[str, Any]


class StressMetricsSnapshot(BaseModel):
    timestamp: datetime
    metrics: Dict[str, float]


class ResilienceFinding(BaseModel):
    severity: ResilienceSeverity
    description: str
    component_ref: Optional[TargetComponentRef] = None


class ResilienceScore(BaseModel):
    overall_score: int = Field(..., ge=0, le=100)
    detection_score: int
    containment_score: int
    recovery_score: int
    assertions_pass_rate: float


class DegradationSummary(BaseModel):
    mode_entered: Optional[DegradationMode] = None
    time_to_degrade_ms: Optional[int] = None
    time_in_degraded_state_ms: Optional[int] = None


class RecommendedFix(BaseModel):
    id: str
    description: str
    severity: ResilienceSeverity
    target_component: TargetComponentRef


class ExperimentSummary(BaseModel):
    run_id: str
    definition_id: str
    scope: SafeScope
    status: ExperimentStatus
    start_time: datetime
    end_time: Optional[datetime] = None
    gate_report: ExperimentGateReport
    assertion_results: List[AssertionResult] = Field(default_factory=list)
    recovery_results: List[RecoveryAssertion] = Field(default_factory=list)
    resilience_score: Optional[ResilienceScore] = None
    degradation_summary: Optional[DegradationSummary] = None
    findings: List[ResilienceFinding] = Field(default_factory=list)
    recommended_fixes: List[RecommendedFix] = Field(default_factory=list)


class ExperimentRun(BaseModel):
    id: str
    definition: ExperimentDefinition
    scope: ExperimentScope
    status: ExperimentStatus
    summary: Optional[ExperimentSummary] = None


class ExperimentArtifactManifest(BaseModel):
    run_id: str
    timestamp: datetime
    artifacts: Dict[str, str]


class ExperimentAuditRecord(BaseModel):
    run_id: str
    timestamp: datetime
    action: str
    operator: str
    details: Dict[str, Any]
