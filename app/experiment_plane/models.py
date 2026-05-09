from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from app.experiment_plane.enums import (
    ExperimentClass,
    ArmClass,
    ObjectiveClass,
    BaselineClass,
    FairnessClass,
    StoppingClass,
    RecommendationClass,
    BiasClass,
    EquivalenceVerdict,
    TrustVerdict,
)


class ExperimentPlaneConfig(BaseModel):
    enforce_strict_fairness: bool = True
    prevent_hidden_drift: bool = True
    allow_pseudo_controls: bool = False


class ExperimentObjective(BaseModel):
    objective_class: ObjectiveClass
    description: str
    target_metrics: List[str]
    non_goals: List[str]
    proof_notes: Optional[str] = None


class ExperimentArm(BaseModel):
    arm_id: str
    arm_class: ArmClass
    description: str
    lineage_refs: Dict[str, str] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class ExperimentBaseline(BaseModel):
    baseline_id: str
    baseline_class: BaselineClass
    description: str
    drift_detected: bool = False


class ExperimentControl(BaseModel):
    control_id: str
    description: str
    is_true_control: bool
    contamination_checked: bool = False


class ExposureAllocationPlan(BaseModel):
    plan_id: str
    split_ratios: Dict[str, float]
    capped_exposure_usd: Optional[float] = None
    sleeve_limits: Dict[str, float] = Field(default_factory=dict)
    symbol_limits: List[str] = Field(default_factory=list)


class FairnessCheckResult(BaseModel):
    fairness_class: FairnessClass
    severity: str
    rationale: str
    imbalances: Dict[str, str] = Field(default_factory=dict)


class ExperimentDriftFinding(BaseModel):
    drift_type: str
    severity: str
    description: str
    lineage_refs: Dict[str, str] = Field(default_factory=dict)


class ExperimentBiasFinding(BaseModel):
    bias_class: BiasClass
    severity: str
    description: str
    next_actions: str


class StoppingRule(BaseModel):
    rule_id: str
    description: str
    condition: str
    action_if_triggered: StoppingClass


class ComparativeAttributionReport(BaseModel):
    report_id: str
    signal_quality_diff: float
    allocation_diff: float
    execution_diff: float
    risk_block_diff: float
    fee_funding_carry_diff: float
    residual_diff: float
    proof_notes: str


class ExperimentRecommendation(BaseModel):
    recommendation_class: RecommendationClass
    confidence_level: str
    rationale: str
    blockers: List[str] = Field(default_factory=list)


class ExperimentDecisionRecord(BaseModel):
    decision_id: str
    stopping_class: StoppingClass
    rationale: str
    evidence_refs: List[str] = Field(default_factory=list)
    recommendation: Optional[ExperimentRecommendation] = None


class ExperimentEquivalenceReport(BaseModel):
    verdict: EquivalenceVerdict
    divergence_sources: List[str]
    proof_notes: str


class ExperimentTrustVerdict(BaseModel):
    verdict: TrustVerdict
    breakdown: Dict[str, str]
    proof_notes: str


class ExperimentDefinition(BaseModel):
    experiment_id: str
    experiment_class: ExperimentClass
    objective: ExperimentObjective
    arms: List[ExperimentArm]
    baseline: ExperimentBaseline
    control: Optional[ExperimentControl] = None
    exposure_plan: ExposureAllocationPlan
    stopping_rules: List[StoppingRule]
    is_production_grade: bool = False


class ExperimentRef(BaseModel):
    experiment_id: str
    description: str


class ComparisonContract(BaseModel):
    contract_id: str
    requires_same_window: bool = True
    requires_same_regime: bool = True
    requires_same_data_truth: bool = True


class ExperimentAuditRecord(BaseModel):
    audit_id: str
    experiment_id: str
    timestamp: str
    action: str
    details: str


class ExperimentArtifactManifest(BaseModel):
    manifest_id: str
    experiment_id: str
    hashes: Dict[str, str]
    lineage_refs: Dict[str, str]
