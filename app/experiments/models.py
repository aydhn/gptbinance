from datetime import datetime, timezone
from pydantic import BaseModel, Field
from typing import Dict, List, Optional, Any
from app.experiments.enums import (
    HypothesisClass,
    ExperimentType,
    ArmType,
    EvaluationSurface,
    ComparisonVerdict,
    FragilityClass,
    EvidenceConfidence,
    PromotionClass,
    ScopeType,
)


class ExperimentGovernanceConfig(BaseModel):
    allow_live_evaluation: bool = False
    require_baseline_for_candidates: bool = True
    enforce_regime_split: bool = True
    strict_policy_adherence: bool = True


class HypothesisFindingLink(BaseModel):
    finding_id: str
    source_layer: str  # decision_quality, remediation, market_truth, policy
    summary: str


class HypothesisVersion(BaseModel):
    version_id: int
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    rationale: str
    author: str


class HypothesisRecord(BaseModel):
    hypothesis_id: str
    h_class: HypothesisClass
    title: str
    description: str
    affected_domains: List[str]
    expected_measurable_signals: List[str]
    disallowed_interpretations: List[str]
    required_evidence: List[str]
    risk_notes: str
    status: str = "registered"  # registered, active, closed, proven, rejected
    findings: List[HypothesisFindingLink] = []
    versions: List[HypothesisVersion] = []


class BaselineReference(BaseModel):
    baseline_id: str
    strategy_id: str
    profile_id: str
    frozen_at: datetime
    manifest_hash: str


class CandidateReference(BaseModel):
    candidate_id: str
    hypothesis_id: str
    changed_surfaces: List[str]
    diff_summary: str
    unsafe_flags: List[str] = []


class ExperimentArm(BaseModel):
    arm_id: str
    arm_type: ArmType
    reference_id: str  # maps to baseline_id or candidate_id
    configuration_overrides: Dict[str, Any] = {}


class ParameterSurface(BaseModel):
    surface_id: str
    domain: str
    current_value: Any
    allowed_range: Optional[Dict[str, Any]] = None


class AblationPlan(BaseModel):
    plan_id: str
    target_components: List[str]
    disable_methods: Dict[str, str]


class SensitivityScan(BaseModel):
    scan_id: str
    target_parameter: str
    sweep_values: List[Any]


class ExperimentScope(BaseModel):
    scope_type: ScopeType
    allowed_profiles: List[str]
    allowed_symbols: List[str]
    time_windows: List[Dict[str, datetime]]
    forbidden_surfaces: List[str] = []


class ExperimentDefinition(BaseModel):
    definition_id: str
    hypothesis_id: str
    experiment_type: ExperimentType
    scope: ExperimentScope
    arms: List[ExperimentArm]
    metrics: List[str]


class ExperimentPack(BaseModel):
    pack_id: str
    definition: ExperimentDefinition
    baseline: BaselineReference
    candidates: List[CandidateReference]
    ablation_plan: Optional[AblationPlan] = None
    sensitivity_scan: Optional[SensitivityScan] = None
    status: str = "draft"


class ExperimentRun(BaseModel):
    run_id: str
    pack_id: str
    started_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    completed_at: Optional[datetime] = None
    evaluation_surface: EvaluationSurface
    status: str = "running"
    results: Dict[str, Any] = {}


class ExperimentComparison(BaseModel):
    comparison_id: str
    run_id: str
    baseline_arm_id: str
    candidate_arm_id: str
    verdict: ComparisonVerdict
    confidence: EvidenceConfidence
    metrics_delta: Dict[str, float]
    caveats: List[str]


class ExperimentFragilityReport(BaseModel):
    report_id: str
    run_id: str
    fragility_classes: List[FragilityClass]
    overfit_suspicion: bool
    sample_size_warning: bool
    regime_concentration: Optional[str] = None
    summary: str


class ExperimentPromotionCandidate(BaseModel):
    candidacy_id: str
    run_id: str
    candidate_id: str
    promotion_class: PromotionClass
    blocked_reason: Optional[str] = None
    evidence_bundle_ref: str


class ExperimentAuditRecord(BaseModel):
    audit_id: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    action: str
    entity_id: str
    entity_type: str
    details: Dict[str, Any]


class ExperimentArtifactManifest(BaseModel):
    manifest_id: str
    run_id: str
    artifacts: List[Dict[str, str]]
