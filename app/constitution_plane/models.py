from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from app.constitution_plane.enums import (
    RuleTaxonomy, VerdictClass, TrustVerdict, ConstitutionClass,
    PrecedenceClass, AuthorityClass, ConflictClass, WaiverClass, OverrideClass,
    EligibilityClass, EquivalenceVerdict
)

class ConstitutionPlaneConfig(BaseModel):
    strict_veto_enforcement: bool = True
    allow_compound_risk: bool = False
    max_cautions_before_review: int = 3

class ConstitutionObject(BaseModel):
    constitution_id: str
    class_type: ConstitutionClass
    authority_scope: str
    precedence_scope: str
    enforcement_class: str
    freshness_posture: str

class ConstitutionObjectRef(BaseModel):
    constitution_id: str
    ref_hash: str

class ConstitutionalRuleRecord(BaseModel):
    rule_id: str
    constitution_id: str
    taxonomy: RuleTaxonomy
    is_non_negotiable: bool = False
    description: str
    proof_notes: str = ""
    lineage_refs: List[str] = []

class RuleTaxonomyRecord(BaseModel):
    taxonomy_class: RuleTaxonomy
    description: str

class PrecedenceRecord(BaseModel):
    precedence_id: str
    dominant_domain: str
    yielding_domain: str
    scope: str
    is_hard_precedence: bool
    proof_notes: str = ""
    lineage_refs: List[str] = []

class AuthorityScopeRecord(BaseModel):
    authority_id: str
    domain: str
    object_scope: str
    action_scope: str
    meta_synthesis_authority: bool
    conflict_notes: str = ""
    lineage_refs: List[str] = []

class DomainVerdictRecord(BaseModel):
    verdict_id: str
    domain: str
    verdict: VerdictClass
    evidence_refs: List[str]
    is_stale: bool = False
    domain_notes: str = ""
    lineage_refs: List[str] = []

class VerdictBundle(BaseModel):
    bundle_id: str
    object_id: str
    action_id: str
    domain_verdicts: List[DomainVerdictRecord]
    missing_domains: List[str]
    sufficiency_notes: str = ""
    lineage_refs: List[str] = []

class ConflictRecord(BaseModel):
    conflict_id: str
    conflict_class: ConflictClass
    conflicting_domains: List[str]
    description: str
    proof_notes: str = ""

class ConflictResolutionRecord(BaseModel):
    resolution_id: str
    conflict_id: str
    resolved_by_precedence: Optional[str]
    resolved_by_freshness: Optional[str]
    resolved_by_authority: Optional[str]
    resolved_by_evidence: Optional[str]
    unresolved_blockers: List[str]
    lineage_refs: List[str] = []

class VetoRecord(BaseModel):
    veto_id: str
    domain: str
    veto_type: str
    release_conditions: str
    lineage_refs: List[str] = []

class CautionAggregationRecord(BaseModel):
    aggregation_id: str
    isolated_cautions: List[str]
    compound_cautions: List[str]
    threshold_exceeded: bool
    saturation_notes: str = ""
    lineage_refs: List[str] = []

class CompoundRiskRecord(BaseModel):
    risk_id: str
    cross_plane_stacking: List[str]
    interacting_cautions: List[str]
    residual_risk_posture: str
    proof_notes: str = ""
    lineage_refs: List[str] = []

class WaiverRecord(BaseModel):
    waiver_id: str
    waiver_class: WaiverClass
    scope: str
    expiry_time: str
    is_stale: bool = False
    evidence_ref: str
    proof_notes: str = ""
    lineage_refs: List[str] = []

class OverrideRecord(BaseModel):
    override_id: str
    override_class: OverrideClass
    justification: str
    is_audited: bool
    residual_burden: str
    prohibited_cases_checked: bool
    proof_notes: str = ""
    lineage_refs: List[str] = []

class FinalVerdictRecord(BaseModel):
    object_id: str
    final_verdict: VerdictClass
    rationale: str
    active_vetoes: List[str]
    applied_waivers: List[str]
    applied_overrides: List[str]
    unresolved_conflicts: List[str]

class EligibilityRecord(BaseModel):
    eligibility_id: str
    eligibility_class: EligibilityClass
    is_eligible: bool
    caveats: List[str]
    lineage_refs: List[str] = []

class PrecedentRecord(BaseModel):
    precedent_id: str
    source_waiver_or_override: str
    analogous_case_notes: str
    misuse_warnings: str
    proof_notes: str = ""
    lineage_refs: List[str] = []

class ConstitutionalFreshnessRecord(BaseModel):
    freshness_id: str
    stale_waivers: List[str]
    stale_overrides: List[str]
    stale_domain_verdicts: List[str]
    sufficiency_notes: str = ""
    lineage_refs: List[str] = []

class ConstitutionalObservationRecord(BaseModel):
    observation_id: str
    observed_conflicts: List[str]
    observed_overrides: List[str]
    observed_waiver_expiries: List[str]
    sufficiency_notes: str = ""
    lineage_refs: List[str] = []

class ConstitutionForecastReport(BaseModel):
    forecast_id: str
    waiver_expiry_forecast: List[str]
    override_risk_forecast: List[str]
    blocker_recurrence_forecast: List[str]
    caution_accumulation_forecast: List[str]
    constitutional_drift_forecast: List[str]
    uncertainty_classes: List[str]

class ConstitutionDebtRecord(BaseModel):
    debt_id: str
    stale_waiver_debt: List[str]
    hidden_override_debt: List[str]
    blocker_dilution_debt: List[str]
    unresolved_conflict_debt: List[str]
    precedent_misuse_debt: List[str]
    debt_severity: str

class ConstitutionEquivalenceReport(BaseModel):
    report_id: str
    action_id: str
    replay_verdict: VerdictClass
    paper_verdict: VerdictClass
    probation_verdict: VerdictClass
    live_verdict: VerdictClass
    equivalence_verdict: EquivalenceVerdict
    divergence_sources: List[str]

class ConstitutionDivergenceReport(BaseModel):
    report_id: str
    divergence_sources: List[str]
    severity: str
    blast_radius: str

class ConstitutionTrustVerdict(BaseModel):
    trust_level: TrustVerdict
    breakdown: Dict[str, str]
    caveats: List[str]

class ConstitutionAuditRecord(BaseModel):
    audit_id: str
    object_id: str
    action_id: str
    timestamp: str
    final_verdict: VerdictClass
    trust_level: TrustVerdict

class ConstitutionArtifactManifest(BaseModel):
    manifest_id: str
    rules_refs: List[str]
    precedence_refs: List[str]
    domain_verdict_refs: List[str]
    conflict_refs: List[str]
    final_verdict_ref: str
    hash: str
