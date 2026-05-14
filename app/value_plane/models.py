from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime, timezone
from app.value_plane.enums import (
    ValueClass, ObjectiveClass, KpiClass, BenefitClass, ImpactClass,
    BaselineClass, AttributionClass, RoiClass, TradeoffClass, VarianceClass,
    EquivalenceVerdict, TrustVerdict
)

def utcnow():
    return datetime.now(timezone.utc)

class ValueObjectRef(BaseModel):
    value_id: str

class ValueObjectiveRef(BaseModel):
    objective_id: str

class ValueObjective(BaseModel):
    objective_id: str
    objective_class: ObjectiveClass
    description: str
    measurable_success_criteria: str

class KpiDefinition(BaseModel):
    kpi_id: str
    objective_id: str
    kpi_class: KpiClass
    description: str
    denominator: str
    measurement_notes: str
    vanity_metric_warning: Optional[str] = None
    kpi_proof_notes: str

class BaselineRecord(BaseModel):
    baseline_id: str
    baseline_class: BaselineClass
    value: float
    staleness_warning: Optional[str] = None
    description: str

class CounterfactualBaseline(BaseModel):
    counterfactual_id: str
    description: str
    uncertainty_notes: str
    counterfactual_proof_notes: str

class BenefitHypothesis(BaseModel):
    benefit_id: str
    benefit_class: BenefitClass
    description: str
    objective_ref: ValueObjectiveRef

class ExpectedImpactRecord(BaseModel):
    expected_impact_id: str
    benefit_ref: str
    low_scenario_value: float
    base_scenario_value: float
    high_scenario_value: float
    horizon: str
    confidence_linkage: str
    dependency_assumptions: str
    expected_downside_notes: str

class EvidenceLink(BaseModel):
    evidence_id: str
    description: str

class RealizedImpactRecord(BaseModel):
    realized_impact_id: str
    impact_class: ImpactClass
    value: float
    horizon: str
    evidence_linkage: List[EvidenceLink]
    baseline_ref: str
    ambiguity_notes: Optional[str] = None

class AttributionRecord(BaseModel):
    attribution_id: str
    attribution_class: AttributionClass
    target_id: str
    share_percentage: float
    completeness_notes: str

class RoiRecord(BaseModel):
    roi_id: str
    roi_class: RoiClass
    gross_roi: Optional[float] = None
    net_roi: Optional[float] = None
    payback_horizon: str
    denominator_quality: str
    fragility_warnings: Optional[str] = None
    cost_linkage: str
    roi_proof_notes: str

class RiskAdjustedValueRecord(BaseModel):
    record_id: str
    raw_value: float
    downside_adjusted_value: float
    tail_risk_reduced_value: float
    volatility_aware_value: float
    constraint_aware_value: float
    risk_adjusted_proof_notes: str

class OpportunityCostRecord(BaseModel):
    record_id: str
    foregone_value: float
    locked_capacity_opportunity_cost: float
    waiting_cost_notes: str
    opportunity_cost_lineage_refs: List[str]

class CostOfDelayRecord(BaseModel):
    record_id: str
    delay_type: str
    quantified_burden: float
    cost_of_delay_proof_notes: str

class AvoidedLossRecord(BaseModel):
    record_id: str
    loss_type: str
    avoided_value: float
    confidence_notes: str

class StrategicOptionalityRecord(BaseModel):
    record_id: str
    enablement_description: str
    leverage_value_estimate: float
    optionality_proof_notes: str

class TradeoffRecord(BaseModel):
    tradeoff_id: str
    tradeoff_class: TradeoffClass
    description: str
    tradeoff_proof_notes: str
    hidden_sacrifice_warning: Optional[str] = None

class NegativeExternalityRecord(BaseModel):
    externality_id: str
    externality_type: str
    description: str
    operational_drag_notes: str
    externality_lineage_refs: List[str]

class ValueForecastReport(BaseModel):
    forecast_id: str
    expected_future_value: float
    decay_forecast: float
    compounding_benefit_forecast: float
    delayed_payoff_forecast: float
    uncertainty_class: str

class ValueVarianceRecord(BaseModel):
    variance_id: str
    variance_class: VarianceClass
    expected_value: float
    realized_value: float
    description: str
    variance_proof_notes: str

class ValuePortfolioRollup(BaseModel):
    rollup_id: str
    portfolio_type: str
    total_value: float
    crowd_out_notes: str

class ValueDebtRecord(BaseModel):
    debt_id: str
    debt_type: str
    severity: str
    interest: float
    description: str

class ValueEquivalenceReport(BaseModel):
    report_id: str
    environments_compared: List[str]
    verdict: EquivalenceVerdict
    divergence_sources: List[str]
    proof_notes: str

class ValueDivergenceReport(BaseModel):
    report_id: str
    severity: str
    blast_radius: str
    divergence_details: str

class ValueTrustVerdict(BaseModel):
    verdict_id: str
    verdict: TrustVerdict
    breakdown: Dict[str, Any]
    blockers: List[str]
    caveats: List[str]

class ValueObject(BaseModel):
    value_id: str
    value_class: ValueClass
    owner: str
    scope: str
    target_horizon: str
    state: str
    objective_ref: ValueObjectiveRef

class ValuePlaneConfig(BaseModel):
    strict_mode: bool = True
    require_baseline: bool = True

class ValueAuditRecord(BaseModel):
    audit_id: str
    target_id: str
    target_type: str
    timestamp: datetime = Field(default_factory=utcnow)
    notes: str

class ValueArtifactManifest(BaseModel):
    manifest_id: str
    value_object_refs: List[str]
    objective_refs: List[str]
    kpi_refs: List[str]
    benefit_refs: List[str]
    baseline_refs: List[str]
    attribution_refs: List[str]
    roi_refs: List[str]
    outcome_refs: List[str]
    hashes: Dict[str, str]
