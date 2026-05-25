from datetime import timezone
from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime
from app.performance_security_plane.enums import (
    SecurityClass, SecuredObligationClass, CollateralClass, GuaranteeClass,
    FundingClass, DrawClass, ReleaseClass, ImpairmentClass, PriorityClass,
    ExhaustionClass, SecurityEquivalenceVerdict, SecurityTrustVerdict
)

class PerformanceSecurityPlaneConfig(BaseModel):
    enabled: bool = True
    enforce_funding_integrity: bool = True
    block_phantom_collateral: bool = True
    block_premature_release: bool = True

class PerformanceSecurityObjectRef(BaseModel):
    security_id: str
    class_type: SecurityClass

class PerformanceSecurityObject(BaseModel):
    security_id: str
    class_type: SecurityClass
    owner: str
    scope: str
    secured_obligation_posture: str
    draw_release_posture: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class PerformanceSecurityRecord(BaseModel):
    security_id: str
    state: str  # active, impaired, exhausted, released
    proof_notes: str
    lineage_refs: List[str]

class SecuredObligationRecord(BaseModel):
    obligation_id: str
    security_refs: List[str]
    posture: SecuredObligationClass
    lineage_refs: List[str]

class EscrowRecord(BaseModel):
    escrow_id: str
    security_id: str
    type: str # funded, conditional, beneficiary_draw, mischaracterized
    lineage_refs: List[str]

class ReserveRecord(BaseModel):
    reserve_id: str
    security_id: str
    type: str # segregated, internal, replenishable, depleted
    lineage_refs: List[str]

class HoldbackRecord(BaseModel):
    holdback_id: str
    security_id: str
    type: str # payment, release, milestone, hidden_risk
    lineage_refs: List[str]

class CollateralRecord(BaseModel):
    collateral_id: str
    security_id: str
    type: CollateralClass
    lineage_refs: List[str]

class CollateralPoolRecord(BaseModel):
    pool_id: str
    type: str # pooled, ring_fenced, shared, over_allocated
    opacity_caution: Optional[str] = None
    lineage_refs: List[str]

class PledgedAssetRecord(BaseModel):
    asset_id: str
    security_id: str
    type: str # eligible, ineligible, stale_valued, released
    lineage_refs: List[str]

class GuaranteeRecord(BaseModel):
    guarantee_id: str
    security_id: str
    type: GuaranteeClass
    lineage_refs: List[str]

class SupportUndertakingRecord(BaseModel):
    undertaking_id: str
    security_id: str
    type: str # parent_like, partner, standby, defective
    lineage_refs: List[str]

class BeneficiaryRecord(BaseModel):
    beneficiary_id: str
    security_id: str
    type: str # primary, shared, subordinated, mismatched
    lineage_refs: List[str]

class PriorityRecord(BaseModel):
    security_id: str
    beneficiary_id: str
    type: PriorityClass
    lineage_refs: List[str]

class FundingStatusRecord(BaseModel):
    security_id: str
    status: FundingClass
    lineage_refs: List[str]

class SegregationRecord(BaseModel):
    security_id: str
    status: str # segregated, designated_but_not_segregated, commingled, control_defective
    lineage_refs: List[str]

class ValuationRecord(BaseModel):
    security_id: str
    type: str # current, stale, haircut_adjusted, disputed
    value: float
    freshness_note: str
    lineage_refs: List[str]

class ImpairmentRecord(BaseModel):
    security_id: str
    type: ImpairmentClass
    lineage_refs: List[str]

class DrawRightRecord(BaseModel):
    draw_id: str
    security_id: str
    type: DrawClass
    lineage_refs: List[str]

class DrawEventRecord(BaseModel):
    event_id: str
    security_id: str
    type: str # valid, partial, wrongful, exhausted
    amount: float
    lineage_refs: List[str]

class ReleaseTriggerRecord(BaseModel):
    trigger_id: str
    security_id: str
    type: str # milestone, verification, lapse_based, invalid
    lineage_refs: List[str]

class ReleaseRecord(BaseModel):
    release_id: str
    security_id: str
    type: ReleaseClass
    lineage_refs: List[str]

class ReplenishmentDutyRecord(BaseModel):
    duty_id: str
    security_id: str
    type: str # mandatory, threshold, failed, delayed
    lineage_refs: List[str]

class SubstituteCollateralRecord(BaseModel):
    substitution_id: str
    original_security_id: str
    new_security_id: str
    type: str # valid, degraded, partial, invalid
    lineage_refs: List[str]

class ExhaustionRecord(BaseModel):
    security_id: str
    type: ExhaustionClass
    lineage_refs: List[str]

class ResidualUndersecurityRecord(BaseModel):
    security_id: str
    type: str # unsecured_remainder, residual_secured_exposure, surviving_draw_risk
    gap_amount: float
    lineage_refs: List[str]

class SecurityComparisonRecord(BaseModel):
    comparison_id: str
    target_a_id: str
    target_b_id: str
    type: str # escrow_vs_reserve, release_vs_depletion, funded_vs_drawable, local_vs_federated
    verdict: str

class SecurityObservationReport(BaseModel):
    pass

class SecurityForecastReport(BaseModel):
    forecast_id: str
    security_id: str
    type: str # depletion_risk, default_to_draw, release_before_performance, substitute_degradation, stale_valuation
    uncertainty_class: str

class SecurityDebtRecord(BaseModel):
    debt_id: str
    security_id: str
    type: str # phantom_collateral, under_security, premature_release, stale_valuation, beneficiary_access
    severity: str

class SecurityEquivalenceReport(BaseModel):
    report_id: str
    security_id: str
    verdict: SecurityEquivalenceVerdict
    blockers: List[str]

class SecurityDivergenceReport(BaseModel):
    report_id: str
    security_id: str
    divergences: List[Dict[str, Any]]

class SecurityTrustVerdictRecord(BaseModel):
    security_id: str
    verdict: SecurityTrustVerdict
    factors: Dict[str, str]

class SecurityAuditRecord(BaseModel):
    audit_id: str
    security_id: str
    action: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class SecurityArtifactManifest(BaseModel):
    manifest_id: str
    security_refs: List[str]
    hash: str
