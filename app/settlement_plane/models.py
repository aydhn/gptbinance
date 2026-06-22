from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime
from app.settlement_plane.enums import (
    SettlementClass, ReleaseClass, ReservationClass, CarveOutClass,
    ConsiderationClass, PerformanceClass, ClosureClass, DefaultClass,
    ReopenClass, SurvivalClass, EquivalenceVerdict, TrustVerdict,
    InstructionClass, MatchClass, FinalityClass, FailClass, BuyInClass, ReversalClass, DebtClass
)


class SettlementObjectRef(BaseModel):
    id: str
    type: str
    version: int


class SettlementPlaneConfig(BaseModel):
    strict_ssi_validation: bool = True
    require_match_for_funding: bool = True
    enforce_reversal_windows: bool = True


class SettlementObject(BaseModel):
    id: str
    settlement_class: SettlementClass
    owner: str
    scope_refs: List[str]
    matching_posture: str = "default_posture"
    finality_posture: str = "default_posture"


class SettlementRecord(BaseModel):
    id: str
    settlement_class: SettlementClass
    owner: str
    scope_refs: List[str]
    release_refs: List[str]
    performance_refs: List[str]
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    settlement_object_id: Optional[str] = None
    status: Optional[str] = None
    proof_notes: Optional[str] = None
    lineage_refs: Optional[List[str]] = None


class ReleaseRecord(BaseModel):
    id: str
    settlement_id: str
    release_class: ReleaseClass
    scope: str
    inflation_caution: bool = False


class CovenantRecord(BaseModel):
    id: str
    settlement_id: str
    covenant_type: str
    is_defective: bool = False


class ReservationRecord(BaseModel):
    id: str
    settlement_id: str
    reservation_class: ReservationClass
    description: str


class CarveOutRecord(BaseModel):
    id: str
    settlement_id: str
    carveout_class: CarveOutClass
    details: str


class ConsiderationRecord(BaseModel):
    id: str
    settlement_id: str
    consideration_class: ConsiderationClass
    value: Dict[str, Any]


class ConsiderationMilestoneRecord(BaseModel):
    id: str
    settlement_id: str
    milestone_type: str
    due_date: datetime


class StructuredPerformanceRecord(BaseModel):
    id: str
    settlement_id: str
    performance_class: PerformanceClass
    milestone_refs: List[str]


class InstallmentRecord(BaseModel):
    id: str
    settlement_id: str
    amount: float
    status: str


class AcceptanceRecord(BaseModel):
    id: str
    settlement_id: str
    status: str
    defects: List[str]


class AuthorityToSettleRecord(BaseModel):
    id: str
    settlement_id: str
    authority_type: str
    defects: List[str]


class ScopeRecord(BaseModel):
    id: str
    settlement_id: str
    issues: List[str]
    overreach_caution: bool


class BeneficiaryClosureRecord(BaseModel):
    id: str
    settlement_id: str
    beneficiary_id: str
    closure_type: str


class PartialClosureRecord(BaseModel):
    id: str
    settlement_id: str
    scope_refs: List[str]


class FullFinalClosureRecord(BaseModel):
    id: str
    settlement_id: str
    carveout_refs: List[str]


class ConditionalSettlementRecord(BaseModel):
    id: str
    settlement_id: str
    conditions: List[str]


class ProvisionalSettlementRecord(BaseModel):
    id: str
    settlement_id: str
    review_status: Optional[str] = None
    provisional_type: Optional[str] = None
    is_reversible: Optional[bool] = None
    lineage_refs: Optional[List[str]] = None


class BreachOfSettlementRecord(BaseModel):
    id: str
    settlement_id: str
    breach_type: str


class RescissionRecord(BaseModel):
    id: str
    settlement_id: str
    status: str


class ReopenAfterSettlementRecord(BaseModel):
    id: str
    settlement_id: str
    reopen_class: ReopenClass


class SurvivalRecord(BaseModel):
    id: str
    settlement_id: str
    survival_class: SurvivalClass
    details: str


class SettlementComparisonRecord(BaseModel):
    id: str
    compare_type: Optional[str] = None
    settlement_a: Optional[str] = None
    settlement_b: Optional[str] = None
    differences: Optional[Dict[str, Any]] = None
    result: Optional[Dict[str, Any]] = None
    lineage_refs: Optional[List[str]] = None


class SettlementObservationReport(BaseModel):
    id: str
    observations: List[str]


class SettlementForecastReport(BaseModel):
    id: str
    predictions: Dict[str, float]
    forecast_type: Optional[str] = None


class SettlementDebtRecord(BaseModel):
    id: str
    settlement_id: Optional[str] = None
    debt_type: Optional[str] = None
    debt_class: Optional[DebtClass] = None
    severity: Optional[str] = None
    lineage_refs: Optional[List[str]] = None


class SettlementEquivalenceReport(BaseModel):
    id: str
    verdict: EquivalenceVerdict
    divergence_sources: Optional[List[str]] = None


class SettlementDivergenceReport(BaseModel):
    id: str
    divergences: List[str]
    severity: Optional[str] = None


class SettlementTrustVerdict(BaseModel):
    id: str
    settlement_id: str
    verdict: TrustVerdict
    factors: Dict[str, str]
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class SettlementAuditRecord(BaseModel):
    id: str
    settlement_id: str
    action: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class SettlementArtifactManifest(BaseModel):
    id: str
    settlement_id: str
    hashes: Dict[str, str]
    refs: Optional[Dict[str, List[str]]] = None


class DefaultRecord(BaseModel):
    id: str
    settlement_id: str
    default_class: DefaultClass
    cured: bool = False

# New items from phase 164


class SettlementSubjectRecord(BaseModel):
    id: str
    subject_type: str
    details: str
    lineage_refs: List[str]


class SettlementVenueRecord(BaseModel):
    id: str
    venue_type: str
    details: str
    lineage_refs: List[str]


class SettlementAgentRecord(BaseModel):
    id: str
    agent_type: str
    details: str
    lineage_refs: List[str]


class SettlementBankRecord(BaseModel):
    id: str
    bank_type: str
    details: str
    lineage_refs: List[str]


class CustodianPathRecord(BaseModel):
    id: str
    path_type: str
    hops: List[str]
    lineage_refs: List[str]


class SSIRecord(BaseModel):
    id: str
    status: str
    details: str
    lineage_refs: List[str]


class SSIAuthorityRecord(BaseModel):
    id: str
    ssi_id: str
    authority_type: str
    lineage_refs: List[str]


class InstructionRecord(BaseModel):
    id: str
    instruction_class: InstructionClass
    details: str
    lineage_refs: List[str]


class InstructionAmendmentRecord(BaseModel):
    id: str
    instruction_id: str
    amendment_type: str
    lineage_refs: List[str]


class InstructionCancellationRecord(BaseModel):
    id: str
    instruction_id: str
    cancellation_type: str
    lineage_refs: List[str]


class AffirmationRecord(BaseModel):
    id: str
    instruction_id: str
    status: str
    lineage_refs: List[str]


class ConfirmationRecord(BaseModel):
    id: str
    instruction_id: str
    status: str
    lineage_refs: List[str]


class MatchingRecord(BaseModel):
    id: str
    match_class: MatchClass
    details: str
    lineage_refs: List[str]


class UnmatchedRecord(BaseModel):
    id: str
    unmatched_state: str
    details: str
    lineage_refs: List[str]


class DvPRecord(BaseModel):
    id: str
    dvp_type: str
    principal_risk_bounded: bool
    lineage_refs: List[str]


class PvPRecord(BaseModel):
    id: str
    pvp_type: str
    fx_principal_risk_bounded: bool
    lineage_refs: List[str]


class FoPRecord(BaseModel):
    id: str
    fop_type: str
    risk_acknowledged: bool
    lineage_refs: List[str]


class FundingReadinessRecord(BaseModel):
    id: str
    posture: str
    lineage_refs: List[str]


class DeliveryReadinessRecord(BaseModel):
    id: str
    posture: str
    lineage_refs: List[str]


class SettlementDateRecord(BaseModel):
    id: str
    date_type: str
    value: datetime
    lineage_refs: List[str]


class ValueDateRecord(BaseModel):
    id: str
    value_type: str
    value: datetime
    lineage_refs: List[str]


class CutoffRecord(BaseModel):
    id: str
    cutoff_type: str
    value: datetime
    lineage_refs: List[str]


class RecyclingRecord(BaseModel):
    id: str
    recycle_type: str
    attempts: int
    lineage_refs: List[str]


class PartialSettlementRecord(BaseModel):
    id: str
    partial_type: str
    ratio: float
    lineage_refs: List[str]


class SplitSettlementRecord(BaseModel):
    id: str
    split_type: str
    details: str
    lineage_refs: List[str]


class SettlementFailRecord(BaseModel):
    id: str
    fail_class: FailClass
    details: str
    lineage_refs: List[str]


class FailToDeliverRecord(BaseModel):
    id: str
    fail_id: str
    ftd_type: str
    lineage_refs: List[str]


class FailToReceiveRecord(BaseModel):
    id: str
    fail_id: str
    ftr_type: str
    lineage_refs: List[str]


class FailToPayRecord(BaseModel):
    id: str
    fail_id: str
    ftp_type: str
    lineage_refs: List[str]


class BuyInTriggerRecord(BaseModel):
    id: str
    trigger_type: str
    lineage_refs: List[str]


class BuyInRecord(BaseModel):
    id: str
    buyin_class: BuyInClass
    details: str
    lineage_refs: List[str]


class CashCompensationRecord(BaseModel):
    id: str
    compensation_type: str
    amount: float
    lineage_refs: List[str]


class PenaltyRecord(BaseModel):
    id: str
    penalty_type: str
    amount: float
    lineage_refs: List[str]


class SettlementFinalityRecord(BaseModel):
    id: str
    finality_class: FinalityClass
    details: str
    lineage_refs: List[str]


class ReversalWindowRecord(BaseModel):
    id: str
    window_type: str
    expiry: datetime
    lineage_refs: List[str]


class MistakenSettlementRecord(BaseModel):
    id: str
    mistaken_type: str
    details: str
    lineage_refs: List[str]


class SettlementReversalRecord(BaseModel):
    id: str
    reversal_class: ReversalClass
    details: str
    lineage_refs: List[str]


class DuplicateSettlementRecord(BaseModel):
    id: str
    duplicate_type: str
    details: str
    lineage_refs: List[str]


class WrongDestinationRecord(BaseModel):
    id: str
    wrong_type: str
    details: str
    lineage_refs: List[str]


class SettlementDisciplineRecord(BaseModel):
    id: str
    discipline_type: str
    details: str
    lineage_refs: List[str]


class SettlementDriftRecord(BaseModel):
    id: str
    drift_type: str
    details: str
    lineage_refs: List[str]
