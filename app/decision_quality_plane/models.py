from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime, timezone
from app.decision_quality_plane.enums import (
    DecisionClass, OptionClass, ConfidenceClass, OutcomeClass, TrustVerdict,
    RecommendationClass, EvidenceClass, AssumptionClass, UncertaintyClass,
    CalibrationClass, EquivalenceVerdict
)

class DecisionDefinition(BaseModel):
    decision_id: str
    decision_class: DecisionClass
    owner: str
    intent: str
    context: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    lineage_refs: List[str] = Field(default_factory=list)

class RecommendationRecord(BaseModel):
    recommendation_id: str
    recommendation_class: RecommendationClass
    decision_id: str
    source_ref: str
    confidence_caveats: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class OptionRecord(BaseModel):
    option_id: str
    option_class: OptionClass
    description: str
    reversibility: str
    blast_radius: str

class OptionComparison(BaseModel):
    comparison_id: str
    decision_id: str
    base_option_id: str
    compared_option_id: str
    trade_off_analysis: str
    downside_risk: str
    dependency_comparison: str
    proof_notes: str

class EvidenceBundleRef(BaseModel):
    evidence_id: str
    evidence_class: EvidenceClass
    source: str
    summary: str
    is_contradictory: bool = False

class AssumptionRecord(BaseModel):
    assumption_id: str
    assumption_class: AssumptionClass
    description: str
    fragility_notes: str
    expiry_condition: str

class HypothesisRecord(BaseModel):
    hypothesis_id: str
    description: str
    invalidation_criteria: str
    confidence_linkage: str
    lineage_refs: List[str] = Field(default_factory=list)

class RationaleRecord(BaseModel):
    rationale_id: str
    chosen_option_id: str
    rejected_option_ids: List[str]
    justification: str
    non_goals: List[str]
    proof_notes: str = ""
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class UncertaintyRecord(BaseModel):
    uncertainty_id: str
    uncertainty_class: UncertaintyClass
    description: str
    burden_notes: str

class ConfidenceRecord(BaseModel):
    confidence_id: str
    confidence_level: ConfidenceClass
    justification: str
    overconfidence_warning: bool = False
    lineage_refs: List[str] = Field(default_factory=list)

class CounterargumentRecord(BaseModel):
    counterargument_id: str
    critique: str
    downside_thesis: str
    rebuttal_quality_notes: str

class PremortemRecord(BaseModel):
    premortem_id: str
    failure_mode: str
    trigger: str
    mitigation_option: Optional[str] = None
    completeness_notes: str = ""

class DecisionChecklistRecord(BaseModel):
    checklist_id: str
    required_evidence_checked: bool
    required_risk_checked: bool
    required_policy_checked: bool
    skipped_items: List[str] = Field(default_factory=list)

class PrecommitmentRecord(BaseModel):
    commitment_id: str
    stop_loss_criteria: str
    re_evaluation_date: datetime
    confidence_decay_triggers: str

class StopConditionRecord(BaseModel):
    stop_id: str
    invalidation_stops: str
    budget_risk_stops: str
    reliability_security_stops: str

class DecisionActionRecord(BaseModel):
    action_id: str
    decision_id: str
    chosen_action_ref: str
    is_deferred: bool = False
    is_rejected: bool = False

class DecisionOutcomeRecord(BaseModel):
    outcome_id: str
    decision_id: str
    outcome_class: OutcomeClass
    expected_vs_actual: str
    ambiguity_notes: str
    reviewed_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class CounterfactualReviewRecord(BaseModel):
    review_id: str
    decision_id: str
    baseline_option_id: str
    hypothetical_outcome: str
    proof_notes: str

class CalibrationRecord(BaseModel):
    calibration_id: str
    decision_id: str
    calibration_class: CalibrationClass
    realized_hit_rate: str
    repeated_bias_notes: str

class DecisionRecurrenceRecord(BaseModel):
    recurrence_id: str
    decision_id: str
    repeated_missing_option: bool = False
    repeated_hidden_assumption: bool = False
    repeated_overconfidence: bool = False
    recurrence_notes: str

class DecisionEquivalenceReport(BaseModel):
    report_id: str
    decision_id: str
    verdict: EquivalenceVerdict
    proof_notes: str
    blockers: List[str] = Field(default_factory=list)

class DecisionDivergenceReport(BaseModel):
    report_id: str
    decision_id: str
    divergence_source: str
    severity: str

class DecisionTrustVerdict(BaseModel):
    decision_id: str
    verdict: TrustVerdict
    breakdown: Dict[str, str]
    blockers: List[str] = Field(default_factory=list)

class DecisionManifest(BaseModel):
    decision: DecisionDefinition
    recommendations: List[RecommendationRecord] = Field(default_factory=list)
    options: List[OptionRecord] = Field(default_factory=list)
    comparisons: List[OptionComparison] = Field(default_factory=list)
    evidence: List[EvidenceBundleRef] = Field(default_factory=list)
    assumptions: List[AssumptionRecord] = Field(default_factory=list)
    hypotheses: List[HypothesisRecord] = Field(default_factory=list)
    rationale: List[RationaleRecord] = Field(default_factory=list)
    uncertainty: List[UncertaintyRecord] = Field(default_factory=list)
    confidence: Optional[ConfidenceRecord] = None
    counterarguments: List[CounterargumentRecord] = Field(default_factory=list)
    premortems: List[PremortemRecord] = Field(default_factory=list)
    checklists: List[DecisionChecklistRecord] = Field(default_factory=list)
    precommitments: List[PrecommitmentRecord] = Field(default_factory=list)
    stop_conditions: List[StopConditionRecord] = Field(default_factory=list)
    action: Optional[DecisionActionRecord] = None
    outcome: Optional[DecisionOutcomeRecord] = None
    counterfactuals: List[CounterfactualReviewRecord] = Field(default_factory=list)
    calibration: Optional[CalibrationRecord] = None
    recurrence: Optional[DecisionRecurrenceRecord] = None
    equivalence: Optional[DecisionEquivalenceReport] = None
    divergence: Optional[DecisionDivergenceReport] = None
    trust_verdict: Optional[DecisionTrustVerdict] = None
