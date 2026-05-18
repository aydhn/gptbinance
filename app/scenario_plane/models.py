from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from app.scenario_plane.enums import *

class ScenarioObjectRef(BaseModel):
    ref_id: str
    ref_type: str

class ScenarioPlaneConfig(BaseModel):
    is_enabled: bool = True

class ScenarioObject(BaseModel):
    scenario_id: str
    scenario_class: ScenarioClass
    owner: str
    scope: str
    objective: str
    status: str = "active"

class ScenarioBaselineRecord(BaseModel):
    baseline_id: str
    scenario_id: str
    baseline_class: BaselineClass
    comparability_notes: str

class AssumptionRecord(BaseModel):
    assumption_id: str
    assumption_class: AssumptionClass
    description: str

class AssumptionSetRecord(BaseModel):
    set_id: str
    scenario_id: str
    assumptions: List[AssumptionRecord]
    hidden_warnings: List[str]

class ShockRecord(BaseModel):
    shock_id: str
    scenario_id: str
    shock_class: ShockClass
    realism_notes: str

class InterventionRecord(BaseModel):
    intervention_id: str
    scenario_id: str
    intervention_class: InterventionClass
    side_effect_notes: str

class BranchPointRecord(BaseModel):
    branch_id: str
    scenario_id: str
    branch_class: BranchClass
    conditions: Dict[str, Any]

class ScenarioTimelineRecord(BaseModel):
    timeline_id: str
    scenario_id: str
    stages: List[str]

class CounterfactualRecord(BaseModel):
    counterfactual_id: str
    scenario_id: str
    description: str
    credibility_notes: str

class CascadeRecord(BaseModel):
    cascade_id: str
    scenario_id: str
    impacts: List[str]

class SecondOrderEffectRecord(BaseModel):
    effect_id: str
    scenario_id: str
    impact_area: str

class ScenarioOutcomeRecord(BaseModel):
    outcome_id: str
    scenario_id: str
    outcome_class: OutcomeClass
    confidence_notes: str

class RobustnessRecord(BaseModel):
    robustness_id: str
    scenario_id: str
    robustness_class: RobustnessClass
    proof_notes: str

class FragilityRecord(BaseModel):
    fragility_id: str
    scenario_id: str
    surface: str

class RecoveryCredibilityRecord(BaseModel):
    credibility_id: str
    scenario_id: str
    optimism_warnings: List[str]

class PolicyStressRecord(BaseModel):
    stress_id: str
    scenario_id: str
    stress_class: StressClass

class ConstitutionalStressRecord(BaseModel):
    stress_id: str
    scenario_id: str
    veto_collisions: List[str]

class ScenarioComparisonRecord(BaseModel):
    comparison_id: str
    scenarios: List[str]
    caveats: str

class ScenarioForecastReport(BaseModel):
    report_id: str
    scenario_id: str
    branch_likelihoods: Dict[str, float]

class ScenarioDebtRecord(BaseModel):
    debt_id: str
    scenario_id: str
    severity: str

class ScenarioReadinessRecord(BaseModel):
    readiness_id: str
    scenario_id: str
    readiness_class: str

class ScenarioEquivalenceReport(BaseModel):
    report_id: str
    scenario_id: str
    verdict: EquivalenceVerdict
    divergence_sources: List[str]

class ScenarioDivergenceReport(BaseModel):
    report_id: str
    scenario_id: str
    divergence_items: List[str]

class ScenarioTrustVerdict(BaseModel):
    verdict_id: str
    scenario_id: str
    verdict: TrustVerdict
    breakdown: Dict[str, str]

class ScenarioAuditRecord(BaseModel):
    audit_id: str
    scenario_id: str
    timestamp: str

class ScenarioArtifactManifest(BaseModel):
    manifest_id: str
    scenario_id: str
    components: Dict[str, str]

class ScenarioRecord(BaseModel):
    scenario_id: str
    name: str

class ScenarioTaxonomyRecord(BaseModel):
    taxonomy_id: str
    scenario_id: str
    taxonomy_class: TaxonomyClass
