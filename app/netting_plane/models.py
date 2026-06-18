from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from .enums import *

class NettingPlaneConfig(BaseModel):
    strict_mutuality_check: bool = True
    enforce_stay_blocks: bool = True

class NettingObjectRef(BaseModel):
    netting_id: str
    class_name: NettingClass

class NettingObject(BaseModel):
    netting_id: str
    class_name: NettingClass
    owner: str
    scope: str
    mutuality_posture: MutualityClass
    closeout_posture: CloseoutClass

class NettingRecord(BaseModel):
    record_id: str
    netting_id: str
    status: str
    proof_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class NettingSubjectRecord(BaseModel):
    subject_id: str
    subject_type: str
    hidden_gap: bool = False
    lineage_refs: List[str] = Field(default_factory=list)

class CounterpartyPairRecord(BaseModel):
    pair_id: str
    party_a: str
    party_b: str
    pair_type: str
    hidden_defect: bool = False
    lineage_refs: List[str] = Field(default_factory=list)

class CounterpartyCapacityRecord(BaseModel):
    capacity_id: str
    posture: str
    fiduciary_mismatch: bool = False
    lineage_refs: List[str] = Field(default_factory=list)

class MutualObligationRecord(BaseModel):
    obligation_id: str
    obligation_class: ObligationClass
    ineligible: bool = False
    lineage_refs: List[str] = Field(default_factory=list)

class NettingSetRecord(BaseModel):
    set_id: str
    set_type: str
    hidden_drift: bool = False
    lineage_refs: List[str] = Field(default_factory=list)

class ObligationEligibilityRecord(BaseModel):
    eligibility_id: str
    status: str
    lineage_refs: List[str] = Field(default_factory=list)

class MutualityRecord(BaseModel):
    mutuality_id: str
    status: MutualityClass
    lineage_refs: List[str] = Field(default_factory=list)

class MaturityRecord(BaseModel):
    maturity_id: str
    status: str
    lineage_refs: List[str] = Field(default_factory=list)

class DuePayableRecord(BaseModel):
    due_id: str
    posture: str
    lineage_refs: List[str] = Field(default_factory=list)

class ContingentObligationRecord(BaseModel):
    contingent_id: str
    posture: str
    lineage_refs: List[str] = Field(default_factory=list)

class DisputedObligationRecord(BaseModel):
    disputed_id: str
    posture: str
    lineage_refs: List[str] = Field(default_factory=list)

class StayedObligationRecord(BaseModel):
    stayed_id: str
    posture: str
    lineage_refs: List[str] = Field(default_factory=list)

class CurrencyConversionRecord(BaseModel):
    conversion_id: str
    posture: str
    lineage_refs: List[str] = Field(default_factory=list)

class ValuationRecord(BaseModel):
    valuation_id: str
    status: ValuationClass
    lineage_refs: List[str] = Field(default_factory=list)

class CloseoutValuationRecord(BaseModel):
    closeout_id: str
    status: CloseoutClass
    lineage_refs: List[str] = Field(default_factory=list)

class SetoffRightRecord(BaseModel):
    setoff_id: str
    status: SetoffClass
    lineage_refs: List[str] = Field(default_factory=list)

class ContractualSetoffRecord(BaseModel):
    contractual_id: str
    posture: str
    lineage_refs: List[str] = Field(default_factory=list)

class StatutorySetoffRecord(BaseModel):
    statutory_id: str
    posture: str
    lineage_refs: List[str] = Field(default_factory=list)

class EquitableSetoffRecord(BaseModel):
    equitable_id: str
    posture: str
    lineage_refs: List[str] = Field(default_factory=list)

class PaymentNettingRecord(BaseModel):
    payment_netting_id: str
    posture: str
    lineage_refs: List[str] = Field(default_factory=list)

class SettlementNettingRecord(BaseModel):
    settlement_netting_id: str
    posture: str
    lineage_refs: List[str] = Field(default_factory=list)

class CloseoutNettingRecord(BaseModel):
    closeout_netting_id: str
    posture: str
    lineage_refs: List[str] = Field(default_factory=list)

class NovationNettingRecord(BaseModel):
    novation_id: str
    posture: str
    lineage_refs: List[str] = Field(default_factory=list)

class CrossProductNettingRecord(BaseModel):
    cross_product_id: str
    posture: str
    lineage_refs: List[str] = Field(default_factory=list)

class InsolvencySafeNettingRecord(BaseModel):
    insolvency_id: str
    posture: str
    lineage_refs: List[str] = Field(default_factory=list)

class StayBlockRecord(BaseModel):
    stay_block_id: str
    posture: str
    lineage_refs: List[str] = Field(default_factory=list)

class PartialNettingRecord(BaseModel):
    partial_id: str
    posture: str
    lineage_refs: List[str] = Field(default_factory=list)

class ResidualExposureRecord(BaseModel):
    residual_id: str
    status: ResidualClass
    lineage_refs: List[str] = Field(default_factory=list)

class MistakenSetoffRecord(BaseModel):
    mistaken_id: str
    posture: str
    lineage_refs: List[str] = Field(default_factory=list)

class SetoffReversalRecord(BaseModel):
    reversal_id: str
    posture: str
    lineage_refs: List[str] = Field(default_factory=list)

class AntiDuplicationRecord(BaseModel):
    anti_duplication_id: str
    posture: str
    lineage_refs: List[str] = Field(default_factory=list)

class GrossLegAuditRecord(BaseModel):
    gross_leg_id: str
    posture: str
    lineage_refs: List[str] = Field(default_factory=list)

class NettingDebtRecord(BaseModel):
    debt_id: str
    debt_class: DebtClass
    severity: str
    lineage_refs: List[str] = Field(default_factory=list)

class NettingDriftRecord(BaseModel):
    drift_id: str
    posture: str
    lineage_refs: List[str] = Field(default_factory=list)

class NettingComparisonRecord(BaseModel):
    comparison_id: str
    posture: str
    lineage_refs: List[str] = Field(default_factory=list)

class NettingObservationReport(BaseModel):
    report_id: str
    summary: str
    records: List[Any] = Field(default_factory=list)

class NettingForecastReport(BaseModel):
    forecast_id: str
    forecast_type: str
    uncertainty_class: str
    details: str

class NettingEquivalenceReport(BaseModel):
    report_id: str
    verdict: EquivalenceVerdict
    divergence_sources: List[str] = Field(default_factory=list)

class NettingDivergenceReport(BaseModel):
    report_id: str
    severity: str
    blast_radius: str
    details: str

class NettingTrustVerdict(BaseModel):
    verdict_id: str
    netting_id: str
    verdict: TrustVerdict
    obligation_clarity: bool
    mutuality_sufficiency: bool
    valuation_sufficiency: bool
    setoff_sufficiency: bool
    closeout_sufficiency: bool
    residual_cleanliness: bool
    contradiction_cleanliness: bool
    posture_notes: str

class NettingAuditRecord(BaseModel):
    audit_id: str
    netting_id: str
    details: str
    lineage_refs: List[str] = Field(default_factory=list)

class NettingArtifactManifest(BaseModel):
    manifest_id: str
    netting_id: str
    hashes: Dict[str, str] = Field(default_factory=dict)
    lineage_refs: List[str] = Field(default_factory=list)
